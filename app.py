import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Seoul Cafe Geography",
    page_icon="☕",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
    background-color: #050505;
    color: white;
}

.main {
    background-color: #050505;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: white;
}

.hero-title {
    font-size: 72px;
    font-weight: 700;
    line-height: 0.95;
    letter-spacing: -3px;
    margin-bottom: 20px;
}

.hero-subtitle {
    color: #999;
    font-size: 22px;
    line-height: 1.8;
    max-width: 750px;
    margin-bottom: 50px;
}

.metric-card {
    background: #111111;
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #222;
}

.section-title {
    font-size: 14px;
    color: #777;
    letter-spacing: 3px;
    margin-top: 50px;
    margin-bottom: 20px;
}

.quote-box {
    background: linear-gradient(145deg,#101010,#0a0a0a);
    border: 1px solid #222;
    border-radius: 30px;
    padding: 60px;
    margin-top: 40px;
}

.quote-text {
    font-size: 32px;
    line-height: 1.6;
    color: #ddd;
    font-weight: 300;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------

st.markdown("""
<div class="hero-title">
SEOUL<br>
CAFE<br>
GEOGRAPHY
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-subtitle">
Exploring Seoul’s urban cafe culture through
district density, consumer trends, youth lifestyle,
and spatial storytelling.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# DATA
# -----------------------------

data = {
    "District": [
        "Seongsu",
        "Hongdae",
        "Gangnam",
        "Itaewon",
        "Hannam",
        "Jamsil",
        "Yeonnam",
        "Euljiro"
    ],

    "Cafe_Count": [310, 420, 530, 210, 180, 290, 340, 160],

    "Average_Price": [6800, 6500, 7200, 7000, 8500, 6900, 6400, 6200],

    "Youth_Popularity": [95, 98, 90, 85, 88, 80, 92, 83],

    "Instagram_Tag": [89, 96, 91, 80, 87, 78, 93, 76]
}

df = pd.DataFrame(data)

# -----------------------------
# METRICS
# -----------------------------

st.markdown('<div class="section-title">SEOUL OVERVIEW</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h2>8</h2>
    <p>Major Districts</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h2>2440+</h2>
    <p>Total Cafes</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h2>95%</h2>
    <p>Youth Engagement</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h2>2026</h2>
    <p>Final Project</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# BAR CHART
# -----------------------------

st.markdown('<div class="section-title">CAFE DENSITY ANALYSIS</div>', unsafe_allow_html=True)

fig1 = px.bar(
    df,
    x="District",
    y="Cafe_Count",
    color="Cafe_Count",
    text="Cafe_Count"
)

fig1.update_layout(
    paper_bgcolor="#050505",
    plot_bgcolor="#050505",
    font_color="white",
    height=600,
    title="Cafe Density by District",
    title_font_size=28
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# SCATTER PLOT
# -----------------------------

st.markdown('<div class="section-title">PRICE VS POPULARITY</div>', unsafe_allow_html=True)

fig2 = px.scatter(
    df,
    x="Average_Price",
    y="Youth_Popularity",
    size="Instagram_Tag",
    color="District",
    hover_name="District",
    size_max=50
)

fig2.update_layout(
    paper_bgcolor="#050505",
    plot_bgcolor="#050505",
    font_color="white",
    height=650,
    title="Cafe Price and Youth Popularity",
    title_font_size=28
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# RADAR CHART
# -----------------------------

st.markdown('<div class="section-title">DISTRICT ATMOSPHERE INDEX</div>', unsafe_allow_html=True)

categories = [
    'Aesthetic',
    'Nightlife',
    'Cafe Culture',
    'Youth Presence',
    'Social Media'
]

fig3 = go.Figure()

fig3.add_trace(go.Scatterpolar(
    r=[95, 88, 97, 96, 99],
    theta=categories,
    fill='toself',
    name='Hongdae'
))

fig3.add_trace(go.Scatterpolar(
    r=[99, 75, 96, 92, 98],
    theta=categories,
    fill='toself',
    name='Seongsu'
))

fig3.update_layout(
    paper_bgcolor="#050505",
    polar=dict(
        bgcolor="#050505",
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            color="white"
        )
    ),
    font_color="white",
    height=700
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# DATA TABLE
# -----------------------------

st.markdown('<div class="section-title">DISTRICT DATASET</div>', unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# PHILOSOPHY
# -----------------------------

st.markdown("""
<div class="quote-box">

<div class="quote-text">
“Seoul’s cafe culture is more than consumption.
It reflects identity, aesthetics, social behavior,
and the emotional geography of the city.”
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.caption("HAOWEI XU — Arts & Big Data Final Project")