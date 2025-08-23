import streamlit as st

st.set_page_config(
    page_title="🧠 Smart Productivity APP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
.center {
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.title-background {
    background-color: #d3d3d3;
    padding: 20px;
    border-radius: 10px;
    display: inline-block;
    margin-bottom: 30px;
}
.section {
    background: linear-gradient(135deg, #89f7fe, #66a6ff);
    border-radius: 15px;
    padding: 25px;
    margin: 20px auto;
    width: 80%;
    color: #000000;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
.section h2 {
    font-size: 28px;
    margin-bottom: 12px;
}
.section p {
    font-size: 18px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="center"><h1>🌟Welcome to Smart Productivity Project!🌟</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center"><p>Organize your tasks, understand your mood, and make life easier — all in one place! 💡</p></div>', unsafe_allow_html=True)

#Section 1
st.markdown("""
<div class="section">
<h2>1️⃣ To-Do List 📝</h2>
<p>Create your personal To-Do List, add tasks, deadlines, and see them neatly organized. ✅</p>
</div>
""", unsafe_allow_html=True)

# Section 2
st.markdown("""
<div class="section">
<h2>2️⃣ Mood Analyzer 💭</h2>
<p>Write down how you feel, and our analyzer will detect your mood and give helpful advice.💭 </p>
</div>
""", unsafe_allow_html=True)

# Section 3
st.markdown("""
<div class="section">
<h2>3️⃣ Task Extraction from Speech 🎤</h2>
<p>Speak or write your plans, and the system will extract tasks and deadlines automatically! ⚡</p>
</div>
""", unsafe_allow_html=True)



st.markdown('<div class="center"><p> Explore each section and see how it can make your life more organized and mindful!</p></div>', unsafe_allow_html=True)





