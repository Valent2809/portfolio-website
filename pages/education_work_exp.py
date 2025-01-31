import streamlit as st

st.set_page_config(layout='wide')
# Custom CSS for the timeline
st.markdown("""
<style>
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
    background-color: #e5e5e5;
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
    background-color: white;
    border-radius: 50%;
    top: 15px;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

.container.left::after {
    right: -12px;
}

.container.right::after {
    left: -12px;
}

.content {
    padding: 20px;
    background-color: white;
    border-radius: 6px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.content h2 {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: -15px; 
}

.content h3 {
    font-size: 1em;
    color: #666;
}

.content .date {
    color: #666;
    font-size: 1em;
    margin-top: -10px;
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
st.markdown("<h1 style='text-align: center;'>My Experience</h1>", unsafe_allow_html=True)

# Add a button to download the recommendation letter
with open("media/GalenGrowth_Recommendation_Letter.pdf", "rb") as file:
    pdf_data = file.read()

st.download_button(
    label="Download Recommendation Letter",
    data=pdf_data,
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
            <p>Developed a Gen AI-powered tender analysis solution for an overseas client, reducing manual processing time of tens of thousands of pages by 95%. Led the end-to-end project delivery, including requirements gathering, implementation planning, and presentations of final proof of concepts and performance. Designed and implemented the system using the Retrieval-Augmented Generation (RAG) framework and advanced prompt engineering.</p>
        </div>
    </div>
    <div class="container right">
        <div class="content">
            <h2>Data Scientist Intern</h2>
            <h3>Galen Growth</h3>
            <div class="date">June 2023 - August 2023</div>
            <p>Developed machine learning models for multi-label classification, achieving 90% accuracy and eliminating manual classification tasks. Automated web scraping processes using Python, BeautifulSoup, and Selenium, reducing data extraction time by 80%. Performed EDA using Numpy, Pandas, MySQL, and Excel. Designed database schemas and implemented workflows to insert thousands of venture data records efficiently.</p>
        </div>
    </div>
</div>
"""

st.markdown(timeline_html, unsafe_allow_html=True)
st.divider()

col4, col5 = st.columns(2, gap='small',border=True)
with col4:
    st.title('Education') 
    # Add Education Information with a logo
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Singapore_Management_University_Logo.png" alt="Logo" style="width: 100px; margin-right: 10px;">
            <div>
                <h4 style="margin: 0;">Singapore Management University</h4>
                <p style="margin: 0;"><strong>Bachelor of Computer Science (Magna Cum Laude / Highest Distinction)</strong></p>
                <p style="margin: 0;"><strong>Aug 2021 – May 2025</strong></p>
                <p style="margin: 0;"><strong>Majors: AI & Business Analyst  </strong></p>
                <p style="margin: 0;"><strong>GPA: 3.61 / 4.00  </strong></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
            #### Award
            - Dean’s list AY23-24
            - Trailblazer ASEAN Scholarship - 2024, 2023, 2022 and 2021  
            - Ellipsis Tech Series 2024 Most creative award
            #### Teaching Assistant
            - Intro to AI (AY23/24 and AY24/25)
            - Analytics Foundation (AY24/25)"""
    )

with col5:
    st.title('Certification')
    st.markdown(
    """
    - [Udemy: Taming Big Data with Apache Spark and Python](https://www.udemy.com/certificate/UC-0483838d-0194-410a-ab12-574e0f4ed73b/)
    - [Udemy: Python for Data Science and Machine Learning Bootcamp](https://www.udemy.com/certificate/UC-b2f06e50-b19f-4702-8402-5077ac08e51c/)
    - [AWS: AWS Certified Solutions Architect Associate](https://www.credly.com/badges/f3f6189e-2bb3-40b3-b328-6fbeecb97171/linked_in_profile)
    - [Coursera: Google Data Analytics Certificate](https://www.credly.com/badges/5e09b040-7d6f-464d-9e65-90dec66a3c82/linked_in_profile)
    - [Oracle: Oracle Certified Foundations Associate, Java](https://www.credly.com/badges/cc029f2c-01bd-4181-a58d-04b7cab7eae3/public_url)
    """,
    unsafe_allow_html=True
)