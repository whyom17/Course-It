import streamlit as st
import random
import json
import time

# Add CSS for transitions and animations
st.markdown("""
<style>    
/* Hide sidebar and header */
section[data-testid="stSidebar"], header, .stAppHeader {
    display: none;
}

/* Global styles */
* {
    background-color: #282b2c;
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
    color: #fff;
}

/* Center H1 */
.k {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
    margin-bottom: 20px;
}

h1 {
    color: #FF4B4B;
    font-size: 2.5rem;
}

hr {
    border-color: #333639;
    margin: 20px 0;
}

/* Page transition animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
    from { opacity: 1; transform: translateY(0); }
    to { opacity: 0; transform: translateY(-20px); }
}

.fade-in {
    animation: fadeIn 0.5s ease forwards;
}

.content-container {
    animation: fadeIn 0.5s ease forwards;
    padding: 20px;
    border-radius: 15px;
    background-color: #333639;
    margin-bottom: 20px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

/* Button styling */
.stButton button {
    background-color: #FF4B4B !important;
    color: white !important;
    border: none !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 15px rgba(255, 75, 75, 0.3) !important;
}

.stButton button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4) !important;
}

.stButton button:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 10px rgba(255, 75, 75, 0.3) !important;
}

/* Progress bar styling */
.stProgress > div > div {
    background-color: #FF4B4B !important;
}

/* Skills styling */
.skill-item {
    padding: 8px;
    margin: 5px 0;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.skill-item:hover {
    transform: translateX(5px);
}

.has-skill {
    color: #00E676;
}

.missing-skill {
    color: #FF4B4B;
}

/* Page transition overlay */
.page-transition-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #282B2C;
    z-index: 9999;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.page-transition-overlay.active {
    opacity: 1;
}
</style>

<!-- Add page transition overlay div -->
<div id="page-transition-overlay" class="page-transition-overlay"></div>

<script>
// Function to trigger page transition
function triggerPageTransition(targetUrl) {
    // Show overlay
    const overlay = document.getElementById('page-transition-overlay');
    overlay.classList.add('active');
    
    // Wait for animation to complete, then navigate
    setTimeout(function() {
        window.location.href = targetUrl;
    }, 300);
    
    return false;
}

// Add transition to all buttons with class 'nav-button'
document.addEventListener('DOMContentLoaded', function() {
    // Apply to any button that should have transition
    const navButtons = document.querySelectorAll('.nav-button');
    navButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Get the data-target attribute or use default
            const targetUrl = this.getAttribute('data-target') || this.href;
            if (targetUrl) {
                e.preventDefault();
                triggerPageTransition(targetUrl);
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)

# Initialize session state for tracking animations
if 'page_loaded' not in st.session_state:
    st.session_state.page_loaded = False

# Title with fade-in effect
st.markdown('<div class="k fade-in"><h1>Checking Skill Gap</h1></div>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# Add short delay to simulate page loading
if not st.session_state.page_loaded:
    # Simulate loading
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.01)
    progress_bar.empty()
    st.session_state.page_loaded = True

st.markdown('<div class="content-container">', unsafe_allow_html=True)
st.subheader("Let's Check Your Skill Gap:")

# Sample data - in real app, this would be loaded from your json file
data = {
    "Machine Learning": [
        "Python", "R", "SQL", "TensorFlow", "PyTorch", "Scikit-learn", 
        "NumPy", "Pandas", "Matplotlib", "Seaborn", "Docker", "Kubernetes"
    ],
    
    "Web Dev": [
        "HTML", "CSS", "JavaScript", "TypeScript", "PHP", "React", "Angular", 
        "Vue.js", "Node.js", "Express", "Django", "Flask", "Spring Boot", "FastAPI", 
        ".NET", "Laravel", "Ruby on Rails", "Docker", "GitHub Actions"
    ],
    
    "Data Structures": [
        "Python", "Java", "C", "C++", "C#", "SQL"
    ],
    
    "Game Dev": [
        "C++", "C#", "Python", "JavaScript", "Unity", "Unreal Engine", 
        "Godot", "Pygame"
    ],
    
    "Cyber Security": [
        "Python", "Bash", "SQL", "C", "C++", "Docker", "Kubernetes", 
        "Metasploit", "Nmap", "Wireshark", "Burp Suite", "Scapy"
    ]
}

# For demonstration, assume these are in session state
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = "Machine Learning"
    
if 'user_skills' not in st.session_state:
    st.session_state.user_skills = ["Python", "NumPy", "Pandas"]

# Define job_title and user_skills
job_title = st.session_state.selected_option
user_skills = st.session_state.user_skills

# Simulate loading job data from JSON file
def load_job_skills():
    # In real app, you'd read from file
    job_data = {}
    for title, skills in data.items():
        job_data[title] = {"required_skills": skills}
    return job_data

# Function to analyze skill gap
def analyze_skill_gap(user_skills, job_title):
    job_data = load_job_skills()
    
    if job_title not in job_data:
        return [], [], 0
    
    required_skills = job_data[job_title]["required_skills"]
    
    # Convert both lists to lowercase for case-insensitive comparison
    user_skills_lower = [skill.lower() for skill in user_skills]
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Find missing skills
    missing_skills = [skill for skill, skill_lower in zip(required_skills, required_skills_lower) 
                     if skill_lower not in user_skills_lower]
    
    # Find matching skills
    matching_skills = [skill for skill, skill_lower in zip(required_skills, required_skills_lower) 
                      if skill_lower in user_skills_lower]
    
    # Calculate match percentage
    match_percentage = len(matching_skills) / len(required_skills) * 100 if required_skills else 0
    
    return missing_skills, matching_skills, float(match_percentage)

# Get missing skills, matching skills, and match percentage
missing_skills, matching_skills, match_percentage = analyze_skill_gap(user_skills, job_title)

# Display results with nice animations
st.markdown('</div>', unsafe_allow_html=True)  # Close first container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

st.subheader("Analysis Results")

# Progress bar for skill match with animation
st.markdown(f"**Skill Match: {match_percentage:.1f}%**")
st.progress(match_percentage / 100)

# Display matching and missing skills with animations
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Skills You Have:**")
    for i, skill in enumerate(matching_skills):
        # Add a small delay effect between items
        st.markdown(f'<div class="skill-item has-skill" style="animation-delay: {i*0.1}s;">✅ {skill}</div>', unsafe_allow_html=True)

with col2:
    st.markdown("**Skills You Need:**")
    for i, skill in enumerate(missing_skills):
        st.markdown(f'<div class="skill-item missing-skill" style="animation-delay: {i*0.1}s;">❌ {skill}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close second container

# Navigation buttons with transition effects
col1, col2 = st.columns(2)

with col1:
    if st.button("Go Back", key="back_btn"):
        # Add JavaScript to trigger transition before navigation
        st.markdown("""
        <script>
            triggerPageTransition("pages/skills.py");
        </script>
        """, unsafe_allow_html=True)
        time.sleep(0.5)  # Small delay
        st.switch_page("pages/skills.py")

with col2:
    if st.button("Continue", key="continue_btn"):
        # Add JavaScript to trigger transition before navigation
        st.markdown("""
        <script>
            triggerPageTransition("todo/page_3.py");
        </script>
        """, unsafe_allow_html=True)
        time.sleep(0.5)  # Small delay
        st.switch_page("pages/todo.py")

# Store user skills in session state for next page
st.session_state.user_skills = user_skills
st.session_state.missing_skills = missing_skills