import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Embedded CSS
st.markdown("""
<style>
/* Container for the hero section */
.hero-container {
    padding: 50px 40px;
    max-width: 600px;
    margin: auto; /* center the container */
    text-align: center;
    background-color: #FFD1DC; /* light gray background */
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

/* Main title styling */
.hero-title {
    font-size: 36px;
    font-weight: 700;
    color: #1ecad3;
    line-height: 1.2;
}

/* Highlight part of the title */
.hero-title span {
    font-weight: 900;
    color: #ff5733; /* orange color */
}

/* Paragraph text */
.hero-text {
    margin-top: 20px;
    font-size: 16px;
    color: #555;
    line-height: 1.5;
}

/* Button styling */
.hero-btn {
    margin-top: 25px;
}

.hero-btn a {
    text-decoration: none;
    border: 2px solid #1ecad3;
    padding: 10px 20px;
    font-size: 14px;
    color: #1ecad3;
    border-radius: 5px;
    font-weight: 500;
    transition: 0.3s ease;
}

.hero-btn a:hover {
    background-color: #1ecad3;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# HTML structure
st.markdown("""
<div class="hero-container">
    <div class="hero-title">
        WELCOME TO <span>STREAMLIT</span>
    </div>
    <div class="hero-text">
        This is a simple web page designed using Streamlit with embedded CSS. 
        You can change styles and content easily.
    </div>
    <div class="hero-btn">
        <a href="https://www.youtube.com/shorts/JdEKc__7WnQ">Click Me!</a>
    </div>
</div>
""", unsafe_allow_html=True)
