import streamlit as st

st.set_page_config(layout='wide')
# Custom CSS for the timeline

st.markdown("""
<style>
/* Default Light Mode */
:root {
    --text-color: black;
    --bg-color: white;
    --timeline-line: #e5e5e5;
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
    :root {
        --text-color: white;
        --bg-color: #1e1e1e;
        --timeline-line: #555;
    }
}

.timeline {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.timeline::after {
    content: '';
    position: absolute;
    width: 2px;
    background-color: var(--timeline-line);
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -1px;
}

.container {
    padding: 10px 40px;
    position: relative;
    width: 50%;
    box-sizing: border-box;
    color: var(--text-color); /* Apply text color */
}

.container.left {
    left: 0;
    text-align: left;
}

.container.right {
    left: 50%;
    text-align: left;
}

.container::after {
    content: '💼';
    position: absolute;
    width: 25px;
    height: 25px;
    background-color: var(--bg-color);
    border-radius: 50%;
    top: 15px;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-color);
}

.container.left::after {
    right: -12px;
}

.container.right::after {
    left: -12px;
}

.content {
    padding: 15px;
    background-color: var(--bg-color);
    border-radius: 6px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.content h2 {
    font-size: 1.2em;
    font-weight: bold;
    color: var(--text-color); /* Adjust for dark mode */
    margin-bottom: -15px; 
}

.content h3 {
    font-size: 1em;
    color: var(--text-color);
}

.content .date {
    color: var(--text-color);
    font-size: 1em;
    margin-top: -13px;
}

.content p {
    color: var(--text-color); /* Ensure text is visible */
    font-size: 12px;
}

@media screen and (max-width: 600px) {
    .timeline::after {
        left: 31px;
    }
    
    .container {
        width: 100%;
        padding-left: 70px;
        padding-right: 25px;
    }
    
    .container.left, .container.right {
        left: 0;
        text-align: left;
    }
    
    .container.left::after, .container.right::after {
        left: 15px;
    }
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 35px;'>My Experience</h1>", unsafe_allow_html=True)

# Add a button to download the recommendation letter
def read_pdf(path):
    with open(path, "rb") as file:
        pdf_file = file.read()
        return pdf_file

st.download_button(
    label="Download Resume",
    data=read_pdf("media/ValentinoResumeDS.pdf"),
    file_name="media/ValentinoResumeDS.pdf",
    mime="application/pdf",
    type="primary"
)

st.download_button(
    label="Download Recommendation Letter",
    data=read_pdf("media/GalenGrowth_Recommendation_Letter.pdf"),
    file_name="media/GalenGrowth_Recommendation_Letter.pdf",
    mime="application/pdf",
    type="primary"
)

# Timeline HTML
timeline_html = """
<div class="timeline">
    <div class="container left">
        <div class="content">
            <h2>AI Intern</h2>
            <h3>NCS</h3>
            <div class="date">May 2024 - August 2024</div>
            <p style='font-size:12px;'>Developed a Gen AI-powered tender analysis solution for an overseas client, reducing manual processing time of tens of thousands of pages by 95%. Led the end-to-end project delivery, including requirements gathering, implementation planning, and presentations of final proof of concepts and performance. Designed and implemented the system using the Retrieval-Augmented Generation (RAG) framework and advanced prompt engineering.</p>
        </div>
    </div>
    <div class="container right">
        <div class="content">
            <h2>Data Scientist Intern</h2>
            <h3>Galen Growth</h3>
            <div class="date">June 2023 - August 2023</div>
            <p style='font-size:12px;'>Developed machine learning models for multi-label classification, achieving 90% accuracy and eliminating manual classification tasks. Automated web scraping processes using Python, BeautifulSoup, and Selenium, reducing data extraction time by 80%. Performed EDA using Numpy, Pandas, MySQL, and Excel. Designed database schemas and implemented workflows to insert thousands of venture data records efficiently.</p>
        </div>
    </div>
</div>
"""

st.markdown(timeline_html, unsafe_allow_html=True)
st.divider()

col4, col5 = st.columns(2, gap='small',border=True)
with col4:
    st.markdown("<h1 style='text-align: center; font-size: 35px;'>Education</h1>", unsafe_allow_html=True)
    # Add Education Information with a logo
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Singapore_Management_University_Logo.png" alt="Logo" style="width: 75px; margin-right: 10px;">
            <div>
                <h4 style="margin: 0; font-size:17px">Singapore Management University</h4>
                <p style="margin-top: -15px;font-size:13px;"><strong>Bachelor of Computer Science</strong></p>
                <p style="margin-top: -20px;font-size:13px;"><strong>Aug 2021 – May 2025</strong></p>
                <p style="margin-top: -13px;font-size:13px;"><strong>Grade: Magna Cum Laude/Highest Distinction  </strong></p>
                <p style="margin-top: -17px;font-size:13px;"><strong>Majors: AI & Business Analyst  </strong></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
        .small-font {
            font-size: 13px !important;
        }
        .small-font h5 {
            font-size: 15px !important;
            margin-bottom: -10px;
        }
    </style>
    <div class="small-font">
        <h5>Award</h5>
        <ul>
            <li>Dean's list AY23-24</li>
            <li>Trailblazer ASEAN Scholarship - 2024, 2023, 2022 and 2021</li>
            <li>Ellipsis Tech Series 2024 Most creative award</li>
        </ul>
        <h5>Teaching Assistant</h5>
        <ul>
            <li>Intro to AI (AY23/24 and AY24/25)</li>
            <li>Analytics Foundation (AY24/25)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
with col5:
    st.markdown("<h1 style='text-align: center; font-size: 35px;'>Certification</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .small-font {
            font-size: 13px !important;
        }
    </style>
    <div class="small-font">
        <ul>
            <li><a href='https://www.udemy.com/certificate/UC-0483838d-0194-410a-ab12-574e0f4ed73b/'> Udemy: Taming Big Data with Apache Spark and Python </a></li>
            <li><a href='https://www.udemy.com/certificate/UC-b2f06e50-b19f-4702-8402-5077ac08e51c/'> Udemy: Python for Data Science and Machine Learning Bootcamp </a></li>
            <li><a href='https://www.credly.com/badges/f3f6189e-2bb3-40b3-b328-6fbeecb97171/linked_in_profile'> AWS: AWS Certified Solutions Architect Associate </a></li>
            <li><a href='https://www.credly.com/badges/5e09b040-7d6f-464d-9e65-90dec66a3c82/linked_in_profile'> Coursera: Google Data Analytics Certificate </a></li>
            <li><a href='https://www.credly.com/badges/cc029f2c-01bd-4181-a58d-04b7cab7eae3/public_url'> Oracle: Oracle Certified Foundations Associate, Java </a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)