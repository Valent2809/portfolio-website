import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout='wide')
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl('https://lottie.host/0e6cb557-2b89-48c7-9eb6-ba09a35b7011/37jvcEAeTs.json')

col1, col2 = st.columns([1.3,1], gap='small')
with col1:
    st.markdown(
        """
        <style>
        .gradient-text {
            font-size: 35px;
            font-weight: bold;
            background: linear-gradient(90deg, #FF5733, #FFBD33, #75FF33);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0; /* Removes extra margins */
            padding: 0;
        }
        .normal-text {
            font-size: 35px;  /* Ensure this applies to "Hello. I'm" */
            font-weight: bold;
            margin: 0; /* Removes extra margins */
            padding: 0;
        }
        .text-container {
            line-height: -19; /* Adjusts spacing between lines */
        }
        </style>
        <div class="text-container">
            <h1> <span class="normal-text">Hello. I'm </span> <span class="gradient-text">Valentino Ong</span></h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('##### Aspiring Data Analyst/Scientist')
    st.markdown("""
    <style>
        .small-font {
            font-size: 12px; /* Adjust the font size here */
        }
    </style>
    <div class="small-font">
        I’m a Year 4 Computer Science student at Singapore Management University, specializing in AI and Business Analytics. I am deeply passionate about transforming data into actionable insights that solve real-world problems. Equipped with skills in Python, SQL, data visualization, and machine learning, I thrive on uncovering patterns and delivering impactful solutions. With a strong foundation in teamwork and leadership, I am eager to drive innovation and create meaningful change through the power of data.
    </div>
    """, unsafe_allow_html=True)


    # Contact Me Section
    st.markdown(
        """
    <style>
    .contact-icons {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 6px; /* Space between elements */
        margin-top: 10px;
        font-size: 12px;
    }
    .contact-icons a {
        text-decoration: none;
        color: #333;
        background-color: #f0f0f0;
        padding: 4px 8px;
        border-radius: 15px;
        display: inline-flex;
        align-items: center;
        transition: background-color 0.3s;
        font-size: 12px;
    }
    .contact-icons a:hover {
        background-color: #e0e0e0;
    }
    .contact-icons img {
        width: 13px;
        height: 13px;
        margin-right: 5px;
    }
    .contact-icons p {
        margin: 0;
        display: flex;
        align-items: center;
        font-size: 12px;
    }
    .contact-icons .email {
        text-decoration: none;
        color: #0073e6; /* Email link color */
        font-weight: normal;
        font-size: 12px;
    }

    .contact-icons .email:hover {
        text-decoration: underline;
    }

    .contact-icons .email {
    background-color: transparent; /* Remove button styling */
    padding: 0; /* Remove padding */
    border-radius: 0; /* Remove rounded edges */
    color: #0073e6; /* Email link color */
    font-weight: normal;
    }

    .contact-icons .email:hover {
        background-color: transparent; /* No hover background */
        text-decoration: underline; /* Add underline on hover */
    }
    </style>
    <div class="contact-icons">
        <!-- LinkedIn Button -->
        <a href="https://www.linkedin.com/in/valentino-ong-396603218/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
            LinkedIn
        </a>
        <!-- GitHub Button -->
        <a href="https://github.com/Valent2809" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
            GitHub
        </a>
        <!-- Phone Number -->
        <p>📞 +65 9164 2003</p>
        <a href="mailto:valentinoo.2021@scis.smu.edu.sg" class="email">📧 valentinoo.2021@scis.smu.edu.sg</a>
    </div>

    """,
    unsafe_allow_html=True
    )

with col2:
    st.lottie(lottie_coder)

st.divider()

# Layout for Skills Section
st.markdown(
    """
    <style>
    h2 {
        font-weight: bold !important;  /* Makes the text bold */
    }
    </style>
    ## My Skills
    """,
    unsafe_allow_html=True
)
# Skills and corresponding logos
skills = [
    ("Python", "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"),
    ("Java", "https://www.vectorlogo.zone/logos/java/java-icon.svg"),
    ("MySQL", "https://www.vectorlogo.zone/logos/mysql/mysql-official.svg"),
    ("Pyspark", "https://www.vectorlogo.zone/logos/apache_spark/apache_spark-ar21.svg"),
    ("Pandas", "https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg"),
    ("Tableau", "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png"),
    ("Scikit-Learn", "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"),
    ("TensorFlow", "https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg"),
    ("Docker", "https://www.vectorlogo.zone/logos/docker/docker-icon.svg"),
    ("Kubernetes", "https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg"),
    ("FastAPI", "https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg"),
    ("SpringBoot", "https://www.vectorlogo.zone/logos/springio/springio-ar21.svg"),
    ("AWS", "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"),
    ("Git", "https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg"),
    ("Selenium", "https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png"),
    ("Streamlit", "https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png"),
]

# Define columns dynamically
left, *cols, right = st.columns([0.5] + [1] * 6 + [0.5])

# Loop through each skill and assign to a column
for idx, (skill, logo_url) in enumerate(skills):
    if idx > 11:
        new_idx = (idx % 6) + 1
        col = cols[new_idx]
        html = f"""
        <div style="text-align: center; font-family: system-ui, -apple-system, sans-serif; padding-bottom:15px">
            <img src="{logo_url}" alt="{skill} Logo" style="height: 75px; object-fit: contain;">
            <div>
                <span style="font-size: 1.5rem;">{skill}</span>
            </div>
        </div>
        """
        col.markdown(html, unsafe_allow_html=True)
    else:
        new_idx = idx % 6
        col = cols[new_idx]
        html = f"""
        <div style="text-align: center; font-family: system-ui, -apple-system, sans-serif; padding-bottom:15px">
            <img src="{logo_url}" alt="{skill} Logo" style="height: 75px; object-fit: contain;">
            <div>
                <span style="font-size: 1.125rem;">{skill}</span>
            </div>
        </div>
        """
        col.markdown(html, unsafe_allow_html=True)

st.divider()

col3, col4 = st.columns(2, gap='small')
with col3:
    images = [
        'media/DewaUnited.PNG',
        'media/DewaUnited2.jpg',
        'media/watermelon.PNG',
    ]

    # Initialize session state if not already initialized
    if 'img_index' not in st.session_state:
        st.session_state.img_index = 0  # Set initial image index

    # Function to navigate images
    def navigate_image():
        # Layout for the navigation buttons and image
        col4, col5, col6 = st.columns([1, 8, 1])  # Adjust column sizes
        
        with col4:
            # Update index on previous button press
            if st.button('◀'):
                st.session_state.img_index = (st.session_state.img_index - 1) % len(images)

        with col5:
            # Display current image
            st.image(images[st.session_state.img_index])

        with col6:
            # Update index on next button press
            if st.button('▶'):
                st.session_state.img_index = (st.session_state.img_index + 1) % len(images)

    # Call the function to navigate through images
    navigate_image()

with col4:
    st.markdown(
    """
    <style>
    h2 {
        font-weight: bold !important;  /* Makes the text bold */
    }
    </style>
    ## Interest & Hobby
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
        <style>
            .small-font {
                font-size: 14px; /* You can adjust the font size as needed */
            }
        </style>
        <div class="small-font">
            Being an inquisitive individual, I like to learn and explore new things such as through various certifications and teach as well! I also used to be a tchoukball and rugby player representing my school. Additionally, I enjoy going to the gym and playing games.
        </div>
    """, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .fun-fact {
            background-color: #f2f2f2;  /* Light background */
            border-left: 5px solid #FF5733;  /* Colorful left border */
            padding: 10px 20px;
            font-size: 13px;
            margin-top: 20px;
            font-style: italic;
            color: #333; /* Dark text color */
        }
        .fun-fact strong {
            font-weight: bold;
        }
        </style>
        <div class="fun-fact">
            <strong>Fun Fact:</strong> I used to be an Esports player for the game Wild Rift for 2 years. My in game name is Aelmejor as it means being the best.
        </div>
        """,
        unsafe_allow_html=True
    )
