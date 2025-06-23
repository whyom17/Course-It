import streamlit as st

# Hide sidebar and header
st.markdown("""
    <style>
    /* Style for the 'Go Back' button */
    div.stButton > button:first-child {
        background-color: #FF4B4B; /* Red from file 1 */
        color: white;
        border-radius: 15px; /* Match file 1 border-radius */
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease; /* Match file 1 transitions */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Match file 1 shadow */
    }

    /* Fixing text background issue */
    div.stButton > button:first-child:hover {
        background-color: #d14343; /* Darker Red on Hover */
        transform: translateY(-5px); /* Match file 1 hover effect */
        box-shadow: 0 10px 20px rgba(255, 75, 75, 0.3); /* Match file 1 hover shadow */
    }

    /* Remove unwanted text background */
    div.stButton > button {
        background: none !important;
        box-shadow: none !important;
    }

    /* Style for the 'Continue' button */
    div.stButton > button:nth-child(2) {
        background-color: #FF4B4B !important; /* Red from file 1 to match theme */
        color: white;
        border-radius: 15px; /* Match file 1 border-radius */
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease; /* Match file 1 transitions */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Match file 1 shadow */
    }

    div.stButton > button:nth-child(2):hover {
        background-color: #d14343 !important; /* Darker Red on Hover */
        transform: translateY(-5px); /* Match file 1 hover effect */
        box-shadow: 0 10px 20px rgba(255, 75, 75, 0.3); /* Match file 1 hover shadow */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>    
section[data-testid="stSidebar"], header, .stAppHeader {
    display: none;
}
* {
    background-color: #282B2C; /* Match file 1 background */
    margin: 0; /* Remove default browser margin */
    padding: 0;
    font-family: 'Arial', sans-serif; /* Match file 1 font */
    color: #fff; /* Match file 1 text color */
}

/* Center H1 */
.k {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
    margin-bottom: 40px; /* Match file 1 spacing */
}

/* Style for H1 */
.k h1 {
    color: #FF4B4B; /* Match file 1 heading color */
    font-size: 2.5rem; /* Match file 1 heading size */
}

/* Style for subheaders */
.stSubheader {
    color: #fff !important;
    font-size: 1.5rem !important;
    margin-top: 20px !important;
    margin-bottom: 20px !important;
}

/* Style for horizontal rules */
hr {
    border-color: #333639; /* Match file 1 card color */
    margin: 30px 0;
}

/* Style for radio buttons */
.stRadio > div {
    background-color: #333639 !important; /* Match file 1 card color */
    border-radius: 15px !important; /* Match file 1 border-radius */
    padding: 15px !important;
    margin-top: 10px !important;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3) !important; /* Match file 1 shadow */
    transition: all 0.3s ease !important; /* Match file 1 transitions */
}

.stRadio > div:hover {
    transform: translateY(-5px) !important; /* Match file 1 hover effect */
    box-shadow: 0 15px 30px rgba(255, 75, 75, 0.3) !important; /* Match file 1 hover shadow */
}

/* Style for regular text */
p, .stRadio label, .stMultiSelect label {
    color: #ccc !important; /* Match file 1 paragraph text color */
    font-size: 0.9rem !important;
    line-height: 1.5 !important;
}

/* Style for columns */
[data-testid="column"] {
    display: flex;
    justify-content: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="k"><h1>Skill Assessment</h1></div>', unsafe_allow_html=True)

# Horizontal rule
st.markdown("""<hr>""", unsafe_allow_html=True)

st.subheader("Let us know your current skills")

# Apply custom CSS for multiselect to match file 1 styling
st.markdown("""
<style>
    /* Add extra margin above the multiselect container */
    .stMultiSelect {
        margin-top: 20px;
    }

    /* Style for multiselect container */
    .stMultiSelect [data-baseweb="select"] {
        background-color: #333639 !important; /* Match file 1 card color */
        border-radius: 15px !important; /* Match file 1 border-radius */
        padding: 10px !important;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3) !important; /* Match file 1 shadow */
        transition: all 0.3s ease !important; /* Match file 1 transitions */
        border: none !important;
    }
    
    .stMultiSelect [data-baseweb="select"]:hover {
        transform: translateY(-5px) !important; /* Match file 1 hover effect */
        box-shadow: 0 15px 30px rgba(255, 75, 75, 0.3) !important; /* Match file 1 hover shadow */
    }

    /* Style for dropdown menu */
    .stMultiSelect [data-baseweb="menu"] {
        background-color: #333639 !important;
        border-radius: 15px !important;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3) !important;
    }

    /* Style for selected tags */
    .stMultiSelect [data-baseweb="tag"] {
        background-color: #FF4B4B !important; /* Match file 1 accent color */
        color: #ffffff !important;
        border-radius: 10px !important;
    }

    /* Style for dropdown options on hover */
    .stMultiSelect [role="option"]:hover {
        background-color: rgba(255, 75, 75, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# List of common skills
common_skills = [
 "Python", "JavaScript", "Java", "C", "C++", "C#", "HTML", "CSS", "TypeScript", "PHP",
    "SQL", "R", "Kotlin", "Swift", "Dart", "Go", "Bash", "YAML",
    "React", "Angular", "Vue.js", "Node.js", "Express", "Django", "Flask", "Spring Boot", "FastAPI",
    ".NET", "Laravel", "Ruby on Rails",
    "TensorFlow", "PyTorch", "Scikit-learn", "NumPy", "Pandas", "Matplotlib", "Seaborn",
    "Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible", "GitHub Actions",
    "Unity", "Unreal Engine", "Godot", "Pygame",
    "Metasploit", "Nmap", "Wireshark", "Burp Suite", "Scapy",
    "Jetpack Compose", "React Native", "SwiftUI", "Flutter"
]

# Create the multiselect with the common skills list
user_skills = st.multiselect("Select your skills", options=common_skills)

# Display the selected skills

# Horizontal rule
st.markdown("""<hr>""", unsafe_allow_html=True)

# Experience level
st.subheader("What is your experience level?")
experience = st.radio(
    "Select your overall experience level",
    ["Beginner(0-3months)", "Intermediate(3-12months)", "Professional(1Year+)"]
)

st.session_state.experience = experience

# Horizontal rule
st.markdown("""<hr>""", unsafe_allow_html=True)

# Preferred Language
st.subheader("Prefered Language?")
lang = st.radio(
    "Select your prefered language",
    ["Hindi", "English"]
)

# Horizontal rule
st.markdown("""<hr>""", unsafe_allow_html=True)

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Go Back"):
        st.switch_page("./my_app.py")

with col2:
    if st.button("Continue"):
        st.switch_page("pages/page_3.py")
        
st.session_state.user_skills = user_skills
