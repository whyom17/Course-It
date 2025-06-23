import streamlit as st
import random
import time
import google.generativeai as genai

# Configure Gemini API
try:
    genai.configure(api_key="AIzaSyDM8U4hZcRfby4a2-N7wZwk2x5E6urPLO8")
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")

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

/* Task item styling */
.task-item {
    background-color: #424548;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.task-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.task-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.task-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #FF4B4B;
}

.task-description {
    margin: 10px 0;
    font-size: 0.9rem;
    color: #ccc;
}

.video-link {
    background-color: #1F2123;
    border-radius: 5px;
    padding: 10px;
    margin-top: 10px;
    transition: all 0.3s ease;
}

.video-link:hover {
    background-color: #2A2D30;
}

.video-link a {
    color: #FF4B4B;
    text-decoration: none;
}

.progress-container {
    margin-top: 10px;
}

.complete-button {
    background-color: #00E676 !important;
    margin-top: 10px;
}

/* Checkbox styling */
.stCheckbox > div > div {
    border-radius: 50%;
}

/* Expander styling */
.stExpander {
    background-color: #333639;
    border-radius: 15px;
    overflow: hidden;
    margin-bottom: 20px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.stExpander:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
}

/* Spinner styling */
.stSpinner > div {
    border-top-color: #FF4B4B !important;
}
</style>
""", unsafe_allow_html=True)

# Title with fade-in effect
st.markdown('<div class="k fade-in"><h1>Learning Path</h1></div>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'youtube_links' not in st.session_state:
    st.session_state.youtube_links = {}

if 'completed_tasks' not in st.session_state:
    st.session_state.completed_tasks = set()

if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Ensure we have selected_option (job_title) from page_3
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = "Machine Learning"  # Default fallback

# Ensure we have missing_skills from page_3
if 'missing_skills' not in st.session_state:
    # This is a fallback - ideally it should come from page_3
    st.session_state.missing_skills = ["TensorFlow", "PyTorch", "Scikit-learn"]

# Ensure we have user_skills from page_3
if 'user_skills' not in st.session_state:
    # This is a fallback - ideally it should come from page_3
    st.session_state.user_skills = ["Python", "NumPy", "Pandas"]

# Mark a task as completed
def mark_completed(skill_index):
    st.session_state.completed_tasks.add(skill_index)
    total_skills = len(st.session_state.missing_skills)
    st.session_state.progress = len(st.session_state.completed_tasks) / total_skills * 100 if total_skills > 0 else 0

# Function to get YouTube links using Gemini AI
def get_youtube_link(skill):
    if skill in st.session_state.youtube_links:
        return st.session_state.youtube_links[skill]
    
    try:
        prompt = f"provide me with only ONE direct YouTube video link for the best tutorial about {skill} from either freeCodeCamp, Bro Code, or LearnCode Academy. Format your response as just the complete YouTube URL with absolutely nothing else - no descriptions, no explanations, just the plain URL leading directly to the tutorial video. For example: https://www.youtube.com/watch?v=VideoID"
        
        response = model.generate_content(prompt)
        link = response.text.strip()
        
        # Ensure we got a valid YouTube URL
        if not link.startswith("https://www.youtube.com/"):
            link = f"https://www.youtube.com/results?search_query={skill}+tutorial"
        
        st.session_state.youtube_links[skill] = link
        return link
    except Exception as e:
        st.error(f"Error getting YouTube link for {skill}: {e}")
        return f"https://www.youtube.com/results?search_query={skill}+tutorial"

# Main function to display the learning path
def display_learning_path():
    # Get missing_skills and job_title from session state
    missing_skills = st.session_state.missing_skills
    job_title = st.session_state.selected_option
    
    # Display overall progress
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.subheader(f"Your Learning Progress for {job_title}")
    
    progress = st.session_state.progress
    st.progress(progress/100)
    st.markdown(f"**{progress:.1f}% Complete**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display learning path
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.subheader("Your Learning Path")
    
    if not missing_skills:
        st.success("Congratulations! You already have all the required skills for this position.")
    else:
        # Create tabs for different views
        tab1, tab2 = st.tabs(["Learning Tasks", "Weekly Plan"])
        
        with tab1:
            # Display tasks for each missing skill
            for i, skill in enumerate(missing_skills):
                skill_index = f"{job_title}_{skill}"
                completed = skill_index in st.session_state.completed_tasks
                
                # Get YouTube link for the current skill (with loading indicator)
                if skill not in st.session_state.youtube_links:
                    with st.spinner(f"Finding the best learning resource for {skill}..."):
                        youtube_link = get_youtube_link(skill)
                else:
                    youtube_link = st.session_state.youtube_links[skill]
                
                # Create a task container
                st.markdown(f"""
                <div class="task-item" style="opacity: {'0.6' if completed else '1'}">
                    <div class="task-header">
                        <div class="task-title">
                            {'✅' if completed else f'{i+1}.'} {skill}
                        </div>
                        <div>{"Completed" if completed else "Pending"}</div>
                    </div>
                    <div class="task-description">
                        Master the fundamentals of {skill} to enhance your {job_title} skills.
                    </div>
                    <div class="video-link">
                        <a href="{youtube_link}" target="_blank">📺 Watch Tutorial</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add complete button
                if not completed:
                    if st.button(f"Mark as Complete", key=f"complete_{skill}", use_container_width=True):
                        mark_completed(skill_index)
                        st.success(f"✅ {skill} marked as completed!")
                        time.sleep(1)
                        st.rerun()
        
        with tab2:
            # Create a weekly learning plan
            weeks = {}
            skills_per_week = 2
            
            for i, skill in enumerate(missing_skills):
                week_num = i // skills_per_week + 1
                if week_num not in weeks:
                    weeks[week_num] = []
                weeks[week_num].append(skill)
            
            for week_num, skills in weeks.items():
                with st.expander(f"Week {week_num}"):
                    for skill in skills:
                        skill_index = f"{job_title}_{skill}"
                        completed = skill_index in st.session_state.completed_tasks
                        
                        st.markdown(f"""
                        <div class="task-item" style="opacity: {'0.6' if completed else '1'}">
                            <div class="task-header">
                                <div class="task-title">
                                    {'✅' if completed else '🔄'} {skill}
                                </div>
                            </div>
                            <div class="task-description">
                                Estimated time: {random.randint(3, 10)} hours
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Debug section to show session state (can be removed in production)
    with st.expander("Debug Info"):
        st.write("Session State Variables:")
        st.write(f"Job Title: {st.session_state.selected_option}")
        st.write(f"Missing Skills: {st.session_state.missing_skills}")
        st.write(f"User Skills: {st.session_state.user_skills}")
        st.write(f"Progress: {st.session_state.progress}%")
        st.write(f"Completed Tasks: {st.session_state.completed_tasks}")
    
    # Add navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Go Back", key="back_btn"):
            st.switch_page("pages/page_3.py")
    
    with col2:
        if st.button("Go Home", key="home_btn"):
            st.switch_page("my_app.py")

# Run the main function
display_learning_path()