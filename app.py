import streamlit as st
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

about_page = st.Page(
    page = "pages/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
)

data_science_project_page = st.Page(
    page = "pages/data_science.py",
    title = "Data Science/ML Project",
    icon = ":material/insert_chart:",
)

software_development_page = st.Page(
    page = "pages/swd.py",
    title = "Software Dev Project",
    icon = ":material/code:",
)

education_work_exp_page = st.Page(
    page = "pages/education_work_exp.py",
    title = "Work Experience & Education",
    icon = ":material/work_history:",
)

chatbot_page = st.Page(
    page = "pages/chatbot.py",
    title = "Talk to my Chatbot",
    icon = ":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info":[about_page, education_work_exp_page,chatbot_page],
        "Projects":[data_science_project_page,software_development_page]
    }
)

pg.run()