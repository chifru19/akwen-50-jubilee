import streamlit as st
from datetime import date

# Page Setup
st.set_page_config(page_title="Akwen's 50th Jubilee", page_icon="🌴")

# Theme Styling
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    h1 { color: #B8860B; text-align: center; font-family: 'serif'; margin-bottom: 5px; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #B8860B; }
    .footer { text-align: center; padding: 20px; color: #888; font-size: 14px; border-top: 1px solid #eee; margin-top: 50px; }
    .footer a { color: #B8860B; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("✨ Akwen’s Golden Jubilee ✨")

# 1. THE HERO IMAGE (Header)
try:
    st.image("hero.jpg", use_container_width=True)
except:
    st.info("📌 Header image 'hero.jpg' not found in folder.")

# 2. COUNTDOWN
event_date = date(2026, 9, 2)
days_left = (event_date - date.today()).days
st.metric(label="Countdown to Zanzibar ✈️", value=f"{days_left} Days")

st.divider()

# --- DETAILS SECTION (The other 3 images) ---
st.header("Event Details & Guides")

col1, col2 = st.columns(2)

with col1:
    try:
        st.image("itinerary.jpg", caption="📅 The Official Program", use_container_width=True)
    except:
        st.warning("itinerary.jpg missing")

    try:
        st.image("packing.jpg", caption="🧳 What to Pack", use_container_width=True)
    except:
        st.warning("packing.jpg missing")

with col2:
    try:
        st.image("jubilee.jpg", caption="💠 The Golden Jubilee Bash", use_container_width=True)
    except:
        st.warning("jubilee.jpg missing")
    
    st.success("""
    **Location:** Kendwa Rocks Hotel  
    **Theme:** Tropical Paradise  
    **Vibe:** Elegant, Exotic, & Unforgettable
    """)

st.divider()

# --- INTERACTIVE SECTION ---
st.header("Guest Tools")
tab1, tab2, tab3 = st.tabs(["📅 Live Schedule", "✅ Packing Checklist", "📸 Guest Gallery"])

with tab1:
    st.write("### Quick Schedule Reference")
    st.write("**Sept 2:** Welcome Dinner (Green 💚)")
    st.write("**Sept 3:** Spice Tour & Sunset Cruise (White T-shirts ⚪)")
    st.write("**Sept 4:** Blue Lagoon & Snorkeling (Orange/Yellow 🧡)")
    st.write("**Sept 5:** The Big 50th Celebration (Jelly Mint 💠)")
    st.write("**Sept 6:** Farewell Pool Party (All White 🤍)")

with tab2:
    st.write("### Tick off as you pack!")
    items = ["Sunscreen (SPF 50)", "Insect Repellent", "Universal Adapter", "Swimwear", "Formal Gowns", "Walking Shoes"]
    for item in items:
        st.checkbox(item, key=f"check_{item}")

with tab3:
    st.write("### Share your Jubilee moments")
    st.file_uploader("Upload Photos", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# --- FOOTER SECTION (Your Branding) ---
st.markdown(f"""
    <div class="footer">
        <p>Built with ❤️ by <b>Frank Fru</b></p>
        <p>
            <a href="https://frankfru.com" target="_blank">frankfru.com</a> | 
            <a href="https://github.com/chifru19" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/" target="_blank">LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)