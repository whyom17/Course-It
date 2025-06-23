import streamlit as st

# Set page config
st.set_page_config(
    page_title="Tech Giants",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Define custom CSS that replicates the style from your HTML
css = """
<style>
    /* Global Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Arial', sans-serif;
    }
    
    body {
        border-radius: 20px;
        background-color: #282B2C;
        color: #fff;
    }
    
    h1 {
        margin-bottom: 40px;
        text-align: center;
        color: #FF4B4B;
        font-size: 2.5rem;
    }
    
    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Card Styles */
    .card {
        background-color: #333639;
        width: 100%;
        height: 400px;
        border-radius: 15px;
        overflow: hidden;
        transition: all 0.3s ease;
        position: relative;
        cursor: pointer;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
    }
    
    .card:hover {
        transform: translateY(-15px);
        box-shadow: 0 15px 30px rgba(255, 75, 75, 0.3);
    }
    
    .card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background-color: #FF4B4B;
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.3s ease;
    }
    
    .card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .card-content {
        padding: 25px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        text-align: center;
    }
    
    .logo {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .logo img {
        width: 60px;
        height: 60px;
        object-fit: contain;
    }
    
    .card h2 {
        margin-bottom: 10px;
        color: #fff;
        font-size: 1.8rem;
    }
    
    .card p {
        color: #ccc;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    .footer {
        margin-top: 40px;
        text-align: center;
        color: #999;
        font-size: 0.8rem;
    }
    
    /* Company name link styles */
    h2 a {
        color: #FF4B4B;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    h2 a:hover {
        color: #ff7878;
        text-decoration: underline;
    }
    
    /* Custom Streamlit Styling */
    .stApp {
        background-color: #282B2C;
    }
    
    /* Hide the default Streamlit elements we don't want */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    /* Center the container div */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
"""

# Apply CSS
st.markdown(css, unsafe_allow_html=True)

# Title
st.markdown("<h1>Tech Giants</h1>", unsafe_allow_html=True)

# Create three equal columns for the cards
col1, col2, col3 = st.columns(3)

# Google Card
with col1:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="logo">
                <img src="https://static.vecteezy.com/system/resources/previews/010/353/285/non_2x/colourful-google-logo-on-white-background-free-vector.jpg" alt="Google Logo" />
            </div>
            <h2><a href="google">Google</a></h2>
            <p>A leading technology company specializing in internet-related services, including search engines, cloud computing, and software.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Microsoft Card
with col2:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="logo">
                <img src="https://static.vecteezy.com/system/resources/previews/028/339/965/original/microsoft-icon-logo-symbol-free-png.png" alt="Microsoft Logo" />
            </div>
            <h2><a href="micro">Microsoft</a></h2>
            <p>A multinational technology company focused on software development, consumer electronics, and personal computers.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Facebook Card
with col3:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="logo">
                <img src="https://clipartspub.com/images/facebook-logo-clipart-png-format.png" alt="Facebook Logo" />
            </div>
            <h2><a href="face">Facebook</a></h2>
            <p>A social media and technology company that builds products to enable community connection and communication.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>Click on any company name to visit the company page</p></div>', unsafe_allow_html=True)

# Add custom JavaScript to make the entire card clickable
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Get all card elements
    var cards = document.querySelectorAll('.card');
    
    // Add click event listeners to each card
    cards.forEach(function(card) {
        card.addEventListener('click', function() {
            // Find the link within this card and navigate to its href
            var link = this.querySelector('h2 a');
            if (link) {
                window.location.href = link.getAttribute('href');
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)
