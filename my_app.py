import streamlit as st

import os
st.set_page_config(
    page_title="AI Job Gap Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
    )

import streamlit as st




st.markdown("""
    <style>
    
    
    
    
    /* Global styles */
 
        .stApp {
            position: relative;
            min-height: 100vh;
            background-size: 95%;
            opacity:0.8;
            background-position: center;
            background-image: url('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F4218996.jpg&f=1&nofb=1&ipt=3cfac50a373b092d098073f5f02155ed5be54d7a93870d0239492250bea91bf5&ipo=images');
        }

        /* Ensure overlays are behind the content */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-image: inherit;
            background-size: inherit;
            background-position: inherit;
            background-repeat: inherit;
            filter: blur(3px);
            pointer-events: none;
            z-index: -2; /* Send behind all content */
        }

        .stApp::after {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: rgba(0, 0, 0, 0.3); /* Lighter overlay */
            pointer-events: none;
            z-index: -1; /* Behind content but above the background */
        }

        .stApp > .streamlit-expanderHeader, .stApp > .stMarkdown {
            position: relative;
        }






    
    
    /* Hide sidebar and header */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    header, .stAppHeader {
        display: none;
    }
    
    /* Import font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

    * {
        background-color: transparent;
        margin: 0;
        padding: 0;   
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Navbar styling */
    .navbar {
        overflow: hidden;
        display: flex;
        padding: 15px;
        justify-content: center;
        position: relative;
         transform: translateX(30%);
        top: -80px;
        font-family: 'Poppins', sans-serif;
        background-color: rgba(40, 43, 44, 0.8);
        border-radius: 10px;
        margin-bottom: 5px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
   
    
             width:60%;
    }
    
    .navbar a {
        
    
        color: white;
        padding: 12px 18px;
        text-decoration: none;
        font-size: 16px;
        border-radius: 10px;
        margin: 0 20px;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
    }
    
    .navbar a:hover {
        background-color: #FF4B4B;
        transform: translateY(-3px);
    }
    
    .p {
        background-color: #FF4B4B;
        color: white;
        font-weight: 500;
    }
    </style>

    <div class="navbar">
        <a class="p" href="?page=home">Home</a>
        <a href="?page=about">About</a>
        <a href="?page=contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Selectbox styling */
    div[data-testid="stSelectbox"] label {
        color: #32B98B !important;
        font-weight: 500;
        font-size: 18px !important;
        margin: 10px;
    }
    
    /* Center the selectbox container */
    div[data-testid="stSelectbox"] {
        max-width: 300px !important;
        margin: 0 auto !important;
        color: #32B98B;
        background-color: rgba(91, 91, 91, 0.6);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stSelectbox"]:hover {
        transform: translateY(-5px);
    }

    /* Target the container that renders the select control */
    div[data-testid="stSelectbox"] > div {
        background-color: #5b5b5b !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* Target the arrow icon if present */
    div[data-testid="stSelectbox"] svg {
        fill: #32B98B !important;
    }

    /* When focused, adjust the styling */
    div[data-testid="stSelectbox"] > div:focus {
        outline: none !important;
        border: 2px solid #32B98B !important;
        background-color: rgba(91, 91, 91, 0.8) !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Ensure the hover effect applies to the correct part of the selectbox */
    div[data-testid="stSelectbox"] div[role="combobox"]:hover {
        background-color: rgba(91, 91, 91, 0.8) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Ensure the hover effect applies to the correct part of the selectbox */
    div[data-testid="stSelectbox"] div[role="combobox"]:hover {
        background-color: rgba(91, 91, 91, 0.8) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Heading styling */

    .m {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FF4B4B;
        font-weight: 700;
        font-size: 50px;
        margin-bottom: 50px;
        cursor: pointer;
        transition: transform 0.4s ease;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .m:hover {
        transform: scale(1.03);
    }
    
    /* Text input styling */
    div[data-testid="stTextInput"] {
        max-width: 100% !important;
    }

    
    div[data-testid="stTextInput"] input[type="text"] {
        background-color: #5B5B5B !important; 
        color: white !important; 
        border-radius: 6px !important;
        padding: 8px !important;
    }
    
    /* Style the placeholder text */
    div[data-testid="stTextInput"] input[type="text"]::placeholder {
        color: #999 !important;
        opacity: 1 !important;
        font-weight: 300;
    }
    
    div[data-testid="stTextInput"] input[type="text"]:focus {
        border: 2px solid #32B98B !important; 
        outline: none !important; 
        cursor: pointer;
    }
    
    /* "Choose:" label styling */
    .l {
        color: #FF4B4B;
        font-weight: 600;
        font-size: 20px;
        text-align: center;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
        background-color: transparent;
    }
    </style>
    
    <div class="m">
        What would you like to Learn?
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="l">
    Choose:
    </div>
    """, unsafe_allow_html=True)

# Initialize session state variable if it doesn't exist
if "selected_option" not in st.session_state:
    st.session_state.selected_option = ""

# Selectbox with session state storage
selected_option = st.selectbox(
    "",
    ("Select an option", "Web Dev", "Machine Learning", "Data Structures", "Game Dev", "Cyber Security"),
)

# Store the selection in session state
st.session_state.selected_option = selected_option

# Navigate only when a valid option is chosen
if selected_option and selected_option != "Select an option":
    st.switch_page("pages/skills.py")
        

# Add footer
st.markdown("""
    <style>
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #999;
        font-size: 0.9rem;
    }
    </style>
    
    <div class="footer">
        <p>© 2025 AI Job Gap Analyzer - Select a learning path to continue</p>
    </div>
    """, unsafe_allow_html=True)
   
html_file = "index.html"  # Ensure this file is in the same directory as your app

col1, col2,col3 = st.columns([1,3,1])  # Create two equal-width columns

with col1:
    if st.button("Looking for a Job?"):
        st.switch_page("pages/index.py")

with col3:
    if st.button("Contact Mentor"):
        st.switch_page("pages/payment.py")
  
# if st.button("Looking for a Job?"):
#     st.markdown(
#     """
#     <style>
#     hr {
#         margin: 20px auto;
#         width: 80%;
#         border: 1px solid #ccc;
#             }
#         </style>
#         <hr>
#         """,
#         unsafe_allow_html=True
#         )

#         # Read and display the HTML file
#     st.switch_page("pages/google.py")
    
