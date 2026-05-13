import streamlit as st
from datetime import date

# Page Setup
st.set_page_config(page_title="Akwen's 50th Anniversary", page_icon="🌴")

# --- CONFIGURATION ---
whatsapp_number = "4915217200085"
whatsapp_link = f"https://wa.me/{whatsapp_number}?text=Hi,%20I%20have%20an%20enquiry%20regarding%20Akwen's%20Anniversary"

# Theme Styling
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    h1 { color: #B8860B; text-align: center; font-family: 'serif'; margin-bottom: 5px; }
    h2 { color: #B8860B; font-family: 'serif'; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #B8860B; }
    .whatsapp-button {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
    .footer { text-align: center; padding: 20px; color: #888; font-size: 14px; border-top: 1px solid #eee; margin-top: 50px; }
    .footer a { color: #B8860B; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("✨ Akwen’s Golden Anniversary ✨")

# --- SLIDESHOW SECTION (Moved to top) ---
st.markdown("<h3 style='text-align: center; color: #B8860B;'>Akens Past & Present: An Anniversary Slide Show</h3>", unsafe_allow_html=True)
try:
    # This will play the renamed video file
    st.video("slideshow.mp4")
except:
    st.info("📌 'slideshow.mp4' not found. Please ensure the video is renamed and uploaded.")

# 1. THE HERO IMAGE
try:
    st.image("hero.jpg", use_container_width=True)
except:
    st.info("📌 Header image 'hero.jpg' not found.")

# 2. COUNTDOWN & QUICK CONTACT
col_count, col_wa = st.columns([2, 1])

with col_count:
    event_date = date(2026, 9, 2)
    days_left = (event_date - date.today()).days
    st.metric(label="Countdown to Zanzibar ✈️", value=f"{days_left} Days")

with col_wa:
    st.markdown(f'<a href="{whatsapp_link}" class="whatsapp-button" target="_blank">💬 WhatsApp Support</a>', unsafe_allow_html=True)
    st.caption("For enquiries & confirmations")

st.divider()

# --- DETAILS SECTION ---
st.header("Event Details & Guides")

col1, col2 = st.columns(2)

with col1:
    try:
        st.image("itinerary_new.jpg", caption="📅 The Official Updated Program", use_container_width=True)
    except:
        st.warning("itinerary_new.jpg missing.")

    try:
        st.image("packing.jpg", caption="🧳 What to Pack", use_container_width=True)
    except:
        st.warning("packing.jpg missing")

with col2:
    try:
        st.image("jubilee.jpg", caption="💠 The Golden Anniversary Bash", use_container_width=True)
    except:
        st.warning("jubilee.jpg missing")
    
    st.success(f"""
    **Location:** Kendwa Rocks Hotel  
    **Theme:** Tropical Paradise  
    **Vibe:** Elegant, Exotic, & Unforgettable  
    **RSVP:** [Confirm via WhatsApp]({whatsapp_link})
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
    st.write("### Share some past and present moments with Akwen")
    st.file_uploader("Upload Photos or Videos", type=['png', 'jpg', 'jpeg', 'mp4', 'mov'], accept_multiple_files=True)

# --- FOOTER SECTION ---
st.markdown(f"""
    <div class="footer">
        <p>Built with ❤️ by <b>Frank Fru</b></p>
        <p>
            <a href="https://frankfru.com" target="_blank">frankfru.com</a> | 
            <a href="https://github.com/chifru19" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/in/frankfru" target="_blank">LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)