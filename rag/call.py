import chromadb
from rag.chromadb_create import GeminiEmbeddingFunction
import google.generativeai as genai
from dotenv import load_dotenv
import os
from google.api_core.exceptions import ResourceExhausted
import streamlit as st

load_dotenv()

def load_chroma_collection(path, name):
    """
    Loads an existing Chroma collection from the specified path with the given name.

    Parameters:
    - path (str): The path where the Chroma database is stored.
    - name (str): The name of the collection within the Chroma database.

    Returns:
    - chromadb.Collection: The loaded Chroma Collection.
    """
    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())

    return db

def get_relevant_passage(query, db, n_results):
  passage = db.query(query_texts=[query], n_results=n_results)['documents'][0]
  return passage


def make_rag_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = ("""You are a helpful and informative bot that answers questions about me in my portfolio website using text from the reference passage included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information, do not use the irrelevant background information to the query. \
  Avoid using irrelevant information. If the passage doesn't provide enough context to answer the question, return: "Sorry🙇, unable to reply to your question!" \
  Your audience is non-technical and potentially someone that can hire me, so explain any complicated concepts in simple terms and aim for a friendly, approachable tone. Think of explaining it to someone who has no technical background. \
  Do not overwhelm the user with too much information. Focus only on what’s necessary and directly related to the query. Do not use "I" but "He"
#   QUESTION: '{query}'
#   PASSAGE: '{relevant_passage}'
#   ANSWER:
#   """).format(query=query, relevant_passage=escaped)

  return prompt

def prompt_gemini(prompt):
    gemini_api_key = st.secrets["gemini_api_key"]
    if not gemini_api_key:
        raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    answer = model.generate_content(prompt)
    return answer.text

def generate_answer(query):
    #retrieve top 5 relevant text chunks
    db=load_chroma_collection(path="rag/rag_resource", name="rag_experiment")
    relevant_text = get_relevant_passage(query,db,n_results=5)
    try:
      prompt = make_rag_prompt(query, 
                              relevant_passage="".join(relevant_text)) # joining the relevant chunks to create a single passage
      answer = prompt_gemini(prompt)

      return answer
    except ResourceExhausted as e:
       return f"There seem to be an error {e}, please try again in 1 minute!"

