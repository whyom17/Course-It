import streamlit as st
import requests
from PIL import Image
import re
import random

# Set page config
st.set_page_config(
    page_title="Meta (Facebook) - Learning Resources",
    page_icon="📱",
    layout="centered"
)

# Custom CSS to match Meta's theme (blue)
st.markdown("""
<style>
    .stApp {
        background-color: #282B2C;
        color: #fff;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    
header, .stAppHeader {
        display: none;
    }
    
    h1, h2, h3 {
        color: #1877F2 !important;
    }
    
    .card {
        background-color: #333639;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(24, 119, 242, 0.3);
    }
    
    .youtube-card {
        background-color: #333639;
        border-radius: 15px;
        padding: 20px;
        margin-top: 40px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        text-align: center;
        border-top: 4px solid #FF0000;
    }
    
    .video-container {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
        height: 0;
        overflow: hidden;
        margin-top: 15px;
        margin-bottom: 15px;
        border-radius: 10px;
    }
    
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 10px;
    }
    
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    
    .logo {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        padding: 15px;
    }
    
    .card-title {
        font-size: 1.8rem;
        margin-bottom: 10px;
        color: white !important;
    }
    
    .card-text {
        color: #ccc;
        font-size: 0.9rem;
    }
    
    .youtube-logo {
        display: inline-block;
        vertical-align: middle;
        margin-right: 10px;
    }
    
    .views-badge {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-top: 10px;
        display: inline-block;
    }
    
    .footer {
        margin-top: 40px;
        text-align: center;
        color: #999;
        font-size: 0.8rem;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Add GitHub icon */
    .github-icon {
        margin-right: 10px;
        vertical-align: middle;
    }
    
    /* Add GeeksforGeeks icon */
    .gfg-icon {
        margin-right: 10px;
        vertical-align: middle;
    }
</style>
""", unsafe_allow_html=True)

# Function to get featured YouTube videos
def get_featured_video(topic):
    # Predefined videos related to Meta/Facebook interviews and preparation
    featured_videos = {
        "main": {
            "id": "t3HIcFt3Bvk",
            "title": "Facebook Coding Interview with a PhD Student",
            "views": "3.8M",
            "channel": "Clément Mihailescu"
        },
        "dsa": {
            "id": "wCl9kvQGHPI",
            "title": "How to Use Data Structures & Algorithms to Ace Your Meta Interview",
            "views": "879K",
            "channel": "Meta Careers"
        },
        "interview": {
            "id": "4NIb9l3imAo",
            "title": "Decoding the Facebook Software Engineering Interview",
            "views": "1.2M",
            "channel": "TechLead"
        }
    }
    
    return featured_videos.get(topic, featured_videos["main"])

# Display Meta/Facebook header with logo
st.markdown("""
<div style="text-align: center; margin-bottom: 40px;">
    <div class="logo-container">
        <div class="logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1200px-Facebook_Logo_%282019%29.png" width="80" height="80">
        </div>
    </div>
    <h1>Meta (Facebook) Learning Resources</h1>
    <p style="color: #ccc; margin-bottom: 30px;">Prepare for Meta interviews with these curated resources</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state if not already done
if 'page' not in st.session_state:
    st.session_state.page = "main"

# Display different pages based on state
if st.session_state.page == "main":
    # Create two columns for the cards
    col1, col2 = st.columns(2)
    
    # DSA Questions Card - Linking to GitHub
    with col1:
        st.markdown("""
        <a href="https://github.com/rachitiitr/meta-interview-prep" target="_blank" style="text-decoration: none;">
            <div class="card" id="dsa-card">
                <h2 class="card-title">
                    <svg class="github-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="white">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                    Recommended DSA Questions
                </h2>
                <p class="card-text">A collection of data structures and algorithms questions commonly asked in Meta interviews.</p>
            </div>
        </a>
        """, unsafe_allow_html=True)
    
    # Interview Questions Card - Linking to GeeksforGeeks
    with col2:
        st.markdown("""
        <a href="https://www.geeksforgeeks.org/meta-facebook-interview-questions/" target="_blank" style="text-decoration: none;">
            <div class="card" id="interview-card">
                <h2 class="card-title">
                    <svg class="gfg-icon" width="24" height="24" viewBox="0 0 24 24" fill="white">
                        <path d="M12 2L1 21h22L12 2zm0 4.6L19.1 19H4.9L12 6.6zm-1 5.9h2v2h-2v-2zm0-4h2v3h-2V8.5z"/>
                    </svg>
                    Famous Interview Questions
                </h2>
                <p class="card-text">Real interview questions from Meta that test problem-solving skills and technical knowledge.</p>
            </div>
        </a>
        """, unsafe_allow_html=True)
    
    # Featured YouTube Video Card
    featured_video = get_featured_video("main")
    st.markdown(f"""
    <div class="youtube-card">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
            <svg class="youtube-logo" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="#FF0000">
                <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
            </svg>
            <h2 class="card-title" style="margin: 0 0 0 10px;">Featured Video</h2>
        </div>
        <p class="card-text">{featured_video["title"]}</p>
        <p class="card-text">by {featured_video["channel"]}</p>
        <div class="views-badge">{featured_video["views"]} views</div>
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{featured_video["id"]}?rel=0" 
                    frameborder="0" allowfullscreen>
            </iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "dsa":
    st.markdown("## Recommended DSA Questions for Meta")
    st.markdown("""
    ### Data Structures
    1. **Arrays and Strings**
       - Valid Parentheses
       - Product of Array Except Self
       - Minimum Window Substring
    
    2. **Linked Lists**
       - Merge K Sorted Lists
       - Reverse Nodes in k-Group
       - Flatten a Multilevel Doubly Linked List
    
    3. **Trees and Graphs**
       - Binary Tree Right Side View
       - Serialize and Deserialize Binary Tree
       - Alien Dictionary
    
    ### Algorithms
    1. **Sorting and Searching**
       - Kth Largest Element in an Array
       - Find First and Last Position of Element in Sorted Array
       - Search in Rotated Sorted Array
    
    2. **Dynamic Programming**
       - Regular Expression Matching
       - Longest Valid Parentheses
       - Decode Ways
    
    3. **Graph Algorithms**
       - Clone Graph
       - Accounts Merge
       - Minimum Height Trees
    """)
    
    # Featured YouTube Video for DSA
    featured_video = get_featured_video("dsa")
    st.markdown(f"""
    <div class="youtube-card">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
            <svg class="youtube-logo" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="#FF0000">
                <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
            </svg>
            <h2 class="card-title" style="margin: 0 0 0 10px;">Top DSA Tutorial</h2>
        </div>
        <p class="card-text">{featured_video["title"]}</p>
        <p class="card-text">by {featured_video["channel"]}</p>
        <div class="views-badge">{featured_video["views"]} views</div>
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{featured_video["id"]}?rel=0" 
                    frameborder="0" allowfullscreen>
            </iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Go Back", key="dsa_back"):
        st.session_state.page = "main"
        st.experimental_rerun()

elif st.session_state.page == "interview":
    st.markdown("## Famous Meta (Facebook) Interview Questions")
    st.markdown("""
    ### Coding Questions
    1. **LRU Cache**
       - Design and implement a data structure for Least Recently Used (LRU) cache
    
    2. **Flatten Nested List Iterator**
       - Design an iterator to flatten a nested list of integers
    
    3. **Add Strings**
       - Given two non-negative integers represented as string, return their sum
    
    ### System Design
    1. **Design Facebook Newsfeed**
       - How would you design the Facebook news feed algorithm?
    
    2. **Design Instagram**
       - How would you design a photo-sharing social network?
    
    3. **Design Facebook Messenger**
       - How would you design a scalable messaging platform?
    
    ### Behavioral Questions
    1. "Tell me about a time when you faced a significant technical challenge."
    2. "How do you handle disagreements with team members?"
    3. "Describe a situation where you took ownership of a project."
    """)
    
    # Featured YouTube Video for Interview
    featured_video = get_featured_video("interview")
    st.markdown(f"""
    <div class="youtube-card">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
            <svg class="youtube-logo" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="#FF0000">
                <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
            </svg>
            <h2 class="card-title" style="margin: 0 0 0 10px;">Top Interview Video</h2>
        </div>
        <p class="card-text">{featured_video["title"]}</p>
        <p class="card-text">by {featured_video["channel"]}</p>
        <div class="views-badge">{featured_video["views"]} views</div>
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{featured_video["id"]}?rel=0" 
                    frameborder="0" allowfullscreen>
            </iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Go Back", key="interview_back"):
        st.session_state.page = "main"
        st.experimental_rerun()

# Footer
st.markdown("""
<div class="footer">
    <p>Click on any card to explore the resources</p>
</div>
""", unsafe_allow_html=True)
