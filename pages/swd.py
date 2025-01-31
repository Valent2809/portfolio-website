import streamlit as st

st.set_page_config(layout='wide')
left,col1,right = st.columns([0.2,2,0.2])
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
        padding: 8px 16px;
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
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: -10px; 
        }

        .content h3 {
            font-size: 1em;
            color: #666;
        }
    </style>
    """,unsafe_allow_html=True)
    col2.markdown("""
    <div class="content">
            <h2>Capstone Project: Twinsies</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
                  <img src="https://img.icons8.com/?size=100&id=wPohyHO_qO1a&format=png&color=000000" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://www.vectorlogo.zone/logos/mysql/mysql-official.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
                  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
            </div>
            <p> Full-stack developer utilizing FastAPI and ReactJS, developed Gen AI-powered digital twin for personalized education, delivering tailored learning recommendations across various grading components</p>
            <p> As the project lead, led a cross-functional team using Agile Scrum and acted as the primary liaison with sponsors, ensuring the team understood the requirements clearly.</p>
            <p> Deployed with docker and implemented a CI/CD pipeline with comprehensive integration tests </p>
            <p> spearheaded Gen AI tasks, including prompt engineering and output optimization to enhance recommendation accuracy. </p>
            <div class="link-icons">
                <a href="https://www.youtube.com/watch?v=bazoeIyg1ls&feature=youtu.be" target="_blank">
                <img src="https://img.icons8.com/?size=100&id=19318&format=png&color=000000" alt="demo twinsies" style="width: 25px; height: auto">
                Demo 
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col3.image('media/Twinsies.PNG',use_container_width=True)

    container5 = st.container(border=True)
    col10,col11 = container5.columns(2)
    col10.markdown("""
    <div class="content">
            <h2>Ellipsis Tech series Hackathon 2024: Petal</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg" alt="Tool 1" style="width: 60px; height: auto; margin-right: 10px;">
                  <img src="https://img.icons8.com/?size=100&id=wPohyHO_qO1a&format=png&color=000000" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg" alt="Tool 1" style="width: 55px; height: auto; margin-right: 10px;">
            </div>
            <p><strong>Won most creative award at the hackathon.</strong> Petal is a mobile app that melds AI-driven waste classification, personal chatbot, personalised 3Rs guidance, and a rewarding system with a local recycling centre locator</p>
            <p>Designed and implemented the personalize chatbot feature with RAG capability powered by Google Gemini. Designed and contributed in implementing the AI waste classification feature that enable users to accurately identify waste types through photos, offering immedaite disposal instructions and personalized recycling advice.</p>
            <div class="link-icons">
                <a href="https://youtu.be/WxJZmMxkVxc" target="_blank">
                <img src="https://img.icons8.com/?size=100&id=19318&format=png&color=000000" style="width: 25px; height: auto;">
                Demo
                </a>
                <a href="https://www.linkedin.com/feed/update/urn:li:activity:7237831769532612608/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" style="width: 20px; height: auto;">
                Post
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col11.image('media/Petal.PNG')

    container2 = st.container(border=True)
    col4,col5 = container2.columns(2)
    col4.markdown("""
    <div class="content">
            <h2>Unfairprice</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
                  <img src="https://www.vectorlogo.zone/logos/mysql/mysql-official.svg" alt="Tool 1" style="width: 50px; height: auto; margin-right: 10px;">
                  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Tool 1" style="width: 30px; height: auto; margin-right: 10px;">
            </div>
            <p>As a backend developer, developed an e-commerce web app offering a complete buying and selling experience, built with a strong focus on DevOps practices. Designed RESTful services for products, orders, and shopping carts using FastAPI, and built an integration test infrastructure with automated UI testing via Selenium. Deployed the application with Docker and Kubernetes, implementing a complete CI/CD pipeline while ensuring clean, maintainable Python code</p>
            <div class="link-icons">
                <a href="https://docs.google.com/presentation/d/1mmsaOuY3U1d12dsOmil7EzcK-x_Btajm/edit?usp=sharing&ouid=114827466311946016594&rtpof=true&sd=true" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Microsoft_PowerPoint_Logo.png" style="width: 25px; height: auto">
                Presentation Slides
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col5.image('media/Unfairprice.jpg',use_container_width=True)

    container3 = st.container(border=True)
    col6,col7 = container3.columns(2)
    col6.markdown("""
    <div class="content">
            <h2>Ascenda Admin Portal using AWS</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" alt="Tool 1" style="width: 40px; height: auto; margin-right: 10px;">
            </div>
            <p>Developed and deployed the Ascenda Admin Portal, a platform fully utilizing AWS services. Led the backend team, creating AWS Lambda functions and API Gateway for point ledger and user storage services. Set up CloudWatch for monitoring and Aurora for database management. Organized and facilitated all team meeting agendas to ensure smooth project execution.</p>
        </div>
    """,unsafe_allow_html=True)
    col7.markdown("#####")
    col7.image('media/AscendaAdmin.jfif')

    container4 = st.container(border=True)
    col8,col9 = container4.columns(2)
    col8.markdown("""
    <div class="content">
            <h2>MINDS Mobile App</h2>
            <div style="display: flex; align-items: center;"> 
                  <h3>Made with:</h3>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/17/Google-flutter-logo.png" alt="Tool 1" style="width: 80px; height: auto; margin-right: 10px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg" alt="Tool 1" style="width: 55px; height: auto; margin-right: 10px;">
            </div>
            <p>One-stop activity management solution alongside companion IoT Wearable device for MINDS.</p>
            <p>Designed and implemented the automated item checklist feature powered by Google Gemini, enabling clients to verify essential items through image. Developed interactive dashboards, presenting key insights through visualizations like stacked bar charts. Integrated SQL queries to dynamically retrieve metrics, supporting data-driven decisions for activity management. Additionally, contributed to the overall UI design to enhance user experience and accessibility. </p>
            <div class="link-icons">
                <a href="https://medium.com/@ryanlwk99/cs462-iot-g1t5-598e23b91e4c" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Medium_%28website%29_logo.svg" style="width: 70px; height: auto;">
                Article
                </a>
            </div>
        </div>
    """,unsafe_allow_html=True)
    col9.image('media/IotScanner.PNG')
    col9.caption("Screenshot of Gen AI automated item scanner and dashboards features")


    st.markdown('###')
