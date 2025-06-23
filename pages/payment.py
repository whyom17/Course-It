import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Expert Connect",
    page_icon="👨‍🏫",
    layout="wide"
)

# Custom styling for the page
st.markdown("""
    <style>
    /* Import font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    
header, .stAppHeader {
        display: none;
    }
  
    
    /* Heading styling */
    .main-heading {
        color: #FF4B4B;
        font-weight: 600;
        font-size: 40px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    /* Expert card styling */
    .expert-card {
        background-color: rgba(40, 43, 44, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    .expert-name {
        color: white;
        font-size: 24px;
        font-weight: 600;
        margin: 10px 0;
    }
    
    .expert-price {
        color: #32B98B;
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 15px;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #FF4B4B !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Field selector button */
    .corner-button {
        position: absolute;
        top: 20px;
        right: 20px;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data for demonstration - using the fields from the document
experts_data = {
    "Web Dev": [
        {
            "name": "Abhinav Mishra",
            "price": "$120/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
        },

    ],
    "Machine Learning": [
        {
            "name": "Vyom Pant",
            "price": "$150/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
        },
   
    ],
    "Data Structures": [
        {
            "name": "Vyom Pant",
            "price": "$150/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
       },

    ],
    "Game Dev": [
        {
            "name": "Vyom Pant",
            "price": "$150/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
      },
        {
             "name": "Abhinav Mishra",
            "price": "$120/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
               }
    ],
    "Cyber Security": [
        {
             "name": "Abhinav Mishra",
            "price": "$120/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
               },
        {
            "name": "Abhinav Mishra",
            "price": "$120/hour",
            "photo_url": "https://img.freepik.com/premium-vector/pixel-art-male-character-portrait-with-brown-hair-blue-hoodie-facing-forward_1292377-15514.jpg"
              }
    ]
}

# Main heading
st.markdown("<div class='main-heading'>Expert Connect Platform</div>", unsafe_allow_html=True)

# Button in the top-right corner
st.markdown("<div class='corner-button'></div>", unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col2:
    field_button = st.button("Select Field ▼", use_container_width=True)

# Only show the dropdown if the button is clicked
if field_button or 'show_dropdown' in st.session_state:
    st.session_state['show_dropdown'] = True
    
    # Extract fields from data
    fields = list(experts_data.keys())
    selected_field = st.selectbox("Choose a field of expertise:", fields)
    
    # Display the experts for the selected field
    if selected_field:
        st.markdown(f"<h2 style='text-align: center; color: #32B98B; margin-top: 30px;'>{selected_field} Experts</h2>", unsafe_allow_html=True)
        
        # Create columns for the two experts
        expert_cols = st.columns(2)
        
        # Display each expert in their own column with custom styling
        for i, expert in enumerate(experts_data[selected_field]):
            with expert_cols[i]:
                st.markdown(f"""
                    <div class="expert-card">
                        <img src="{expert["photo_url"]}" width="200">
                        <div class="expert-name">{expert["name"]}</div>
                        <div class="expert-price">{expert["price"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                st.button(f"Connect with {expert['name'].split()[0]}", key=f"connect_{i}")

# Optional informational text when no field is selected
if not ('show_dropdown' in st.session_state):
    st.info("Click the 'Select Field' button in the top-right corner to start exploring experts.")

# Add footer
st.markdown("""
    <div class="footer">
        <p>© 2025 Expert Connect Platform - Find your perfect mentor today</p>
    </div>
    """, unsafe_allow_html=True)
