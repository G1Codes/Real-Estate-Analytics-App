import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Real Estate Analytics App",
    page_icon="🏡",
    layout="wide"  # Makes the layout wider for a better look
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #4B5EAA;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #F0F8FF;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    .tab-info {
        font-size: 1.1rem;
        color: #333;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-title">Welcome to Real Estate Analytics 🏡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your One-Stop Solution for Property Insights in Gurgaon</div>', unsafe_allow_html=True)

# Info box with description
st.markdown("""
<div class="info-box">
    <p style="font-size: 1.2rem; color: #2F4F4F;">
        Explore the real estate market in Gurgaon with our advanced analytics tools. Whether you're looking to predict property prices or analyze market trends, we've got you covered!
    </p>
    <p class="tab-info">
        <b>Price Predictor Tab:</b> Enter details like sector, number of bedrooms, area, and more to get an accurate price prediction for your flat.
    </p>
    <p class="tab-info">
        <b>Analysis Tab:</b> Dive into detailed graphs, including price analysis, sector comparisons, and more, to understand market trends.
    </p>
</div>
""", unsafe_allow_html=True)

# Optional: Add a call-to-action
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 1.1rem; color: #4682B4;">
        Navigate to the tabs on the left to get started!
    </p>
</div>
""", unsafe_allow_html=True)