import streamlit as st

st.set_page_config(layout='wide')
left,col1,right = st.columns([0.001,2,0.001])
st.markdown(
        """
    <style>
    .link-icons {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px; /* Space between elements */
        font-size: 15px;
        margin-bottom: 10px; /* Add spacing at the bottom */
    }
    .link-icons a {
        text-decoration: none;
        color: #333;
        background-color: #f0f0f0;
        padding: 6px 12px;
        border-radius: 20px;
        display: inline-flex;
        align-items: center;
        transition: background-color 0.3s;
    }
    .link-icons a:hover {
        background-color: #e0e0e0;
    }
    .link-icons img {
        width: 17px;
        height: 17px;
        margin-right: 6px;
    }
    .link-icons p {
        margin: 0;
        display: flex;
        align-items: center;
        font-size: 15px;
        color: #333;
    }
    </style>
    """,unsafe_allow_html=True
    )

with col1:
    container1 = st.container(border=True)
    col2,col3 = container1.columns(2)
    col1.markdown("""
    <style>
        .content h2 {
        font-size: 1.25em;
        font-weight: bold;
        margin-bottom: -15px; 
        }

        .content h3 {
            font-size: 1em;
            margin-top: 10px;
        }

        .content p {
            font-size: 0.8em;
        }

    </style>
    """,unsafe_allow_html=True)
    col2.markdown("""
    <div class="content">
            <h2>AIP National AI Student Challenge 2024</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://logo.svgcdn.com/l/seaborn.png" alt="Tool 1" style="width: 60px; height: auto; margin-right: 10px;">
            </div>
            <p>Shortlisted for final stage in Track 1 predicting pet adoption rates. Developed an end-to-end Machine Learning pipeline that include data preprocessing and utilizes machine learning algorithms such as XGBoost and Random Forest to predict pet adoption rates, cleaning and processing a dataset of 14,993 rows with 49 features.</p>
            <div class="link-icons">
                <a href="https://github.com/Valent2809/National-AI-Student-Challenge-2024-Track-1-AIP" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="github aip" style="width: 17px; height: auto;">
                <span style="font-size: 0.8em;">Github</span>
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col3.image('media/AIP.PNG',use_container_width=True)

    container2 = st.container(border=True)
    col4,col5 = container2.columns(2)
    col4.markdown("""
    <div class="content">
            <h2>LinkedOut: Resume & Job Matching Recommendation System</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg" alt="Tool 1" style="width: 45px; height: auto; margin-right: 10px;">
            </div>
            <p>Designed and implemented a semantic recommendation system to streamline the recruitment process by matching resumes with job descriptions and vice versa. The core of the system leveraged Doc2Vec embeddings to capture contextual relationships in textual data and FAISS for fast and scalable similarity search. This enabled both job seekers and recruiters to perform intelligent searches—candidates could discover relevant opportunities, while recruiters could efficiently identify suitable applicants. Developed and deployed backend RESTful APIs using FastAPI, enabling seamless integration of resume-to-job and job-to-resume matching functionality into recruitment platforms.</p>
            <div class="link-icons">
                <a href="https://docs.google.com/presentation/d/1x-BbGk6MEI_4fY5JWqOma4WJn38Kq0vM/edit?usp=sharing&ouid=114827466311946016594&rtpof=true&sd=true" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Microsoft_PowerPoint_Logo.png" style="width: 20px; height: auto">
                <span style="font-size: 0.8em;">Presentation Slides</span> 
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col5.image('media/LinkedOutFlow.PNG',use_container_width=True)
    col5.image('media/LinkedOutSearch.PNG',use_container_width=True)

    container2 = st.container(border=True)
    col4,col5 = container2.columns(2)
    col4.markdown("""
    <div class="content">
            <h2>Social Analytics of reviews for Lazada</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://logo.svgcdn.com/l/seaborn.png" alt="Tool 1" style="width: 60px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
            </div>
            <p>Conducted a comprehensive web scraping and analysis of Lazada reviews from App store, Play store and other platforms to gain actionable insights into customer satisfaction, pain points, and strategies for improving app retention. Performed data cleaning, timeline analysis, and created word clouds to identify trends in customer feedback. Leveraged sentiment analysis using VADER to assess customer opinions and validate rating accuracy, and applied Topic Modeling (LDA) to uncover key themes and highlight areas for improvement.</p>
            <div class="link-icons">
                <a href="https://github.com/Valent2809/Social-Analytics-on-Lazada-reviews" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="github aip" style="width: 17px; height: auto;">
                <span style="font-size: 0.8em;">Github</span>
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col5.image('media/SocialAnalyticsSentiment.PNG',use_container_width=True)
    col5.image('media/SocialAnalytics.PNG',use_container_width=True)

    container4 = st.container(border=True)
    col8,col9 = container4.columns(2)
    col8.markdown("""
    <div class="content">
            <h2>LinkedIn Skills Scraper & Visualization</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <h3 style='font-size:13px;'> BeautifulSoup</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://logo.svgcdn.com/l/seaborn.png" alt="Tool 1" style="width: 60px; height: auto; margin-right: 10px;">
            </div>
            <p>Developed a solution to streamline job research by web scraping LinkedIn postings for desired roles and visualizing the top 20 in-demand skills. Leveraged Selenium and BeautifulSoup for automated data collection, eliminating the need for manual research. Conducted exploratory data analysis (EDA) and created visualizations to uncover trends in job requirements, providing actionable insights for targeted upskilling and informed career planning.</p>
            <div class="link-icons">
                <a href="https://github.com/Valent2809/LinkedIn-scraper-and-visualisation" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="github aip" style="width: 17px; height: auto;">
                <span style="font-size: 0.8em;">Github</span>
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col9.image('media/LinkedInSkills.png')
    col9.caption("Top 20 in demand skills for Data Analyst based on LinkedIn job postings")


    container3 = st.container(border=True)
    col6,col7 = container3.columns(2)
    col6.markdown("""
    <div class="content">
            <h2>Finetune T5 model for a medical chatbot</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://cdn.brandfetch.io/idGqKHD5xE/theme/dark/symbol.svg?c=1dxbfHSJFAPEGdCLU4o5B" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
            </div>
            <p>Finetuned T5 and Flan-T5 base model using various methods including full parameter, LoRA and QLoRA with <a href="https://www.kaggle.com/datasets/saifulislamsarfaraz/medical-chatbot-dataset"> medical chatbot dataset</a> from Kaggle to develop a local LLM tailored for use in medical chatbot application to answer patient queries accurately as well as with enhanced privacy as inputs from users are not saved. Fine-tuned model achieved at least 400% improvement in performance compared to base model using BLEU and ROGUE metrics for comparison. </p>
            <div class="link-icons">
                <a href="https://github.com/Valent2809/Finetuned-Flan-T5-Base-For-Medical-Chatbot" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="github aip" style="width: 17px; height: auto;">
                <span style="font-size: 0.8em;">Github</span>
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col7.image('media/FinetuneProj.PNG')
    col7.caption("Gradio Interface for medical chatbot to effectively compare all models output")
    col7.image('media/resultPercentage.PNG')
    col7.caption("Comparison of performance metrics in % compared to base model")


    container5 = st.container(border=True)
    col10,col11 = container5.columns(2)
    col10.markdown("""
    <div class="content">
            <h2>AI generated vs Real Image Classification</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://cdn.brandfetch.io/idGqKHD5xE/theme/dark/symbol.svg?c=1dxbfHSJFAPEGdCLU4o5B" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
            </div>
            <p>Finetuned HuggingFace Vision Transformer model as well as utilise and train various deep learning models such as manually created, ResNet-50 etc with the <a href='https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images/data'> CIFAKE image dataset </a>to develop a machine learning model that is tailored to classify if an image is real or AI generated. Implemented an Ensemble classifier that combines all the trained classification model to get the average result. </p>
            <div class="link-icons">
                <a href="https://huggingface.co/Valent2809/ai_vs_real_image" target="_blank">
                <img src="https://cdn.brandfetch.io/idGqKHD5xE/theme/dark/symbol.svg?c=1dxbfHSJFAPEGdCLU4o5B" alt="github" style="width: 17px; height: auto;">
                <span style="font-size: 0.8em;">HuggingFace</span>
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col11.markdown("####")
    col11.image('media/ImageClassification.PNG')
    col11.caption("Comparison of test performance metrics across various models, HuggingFace VIT performs best")