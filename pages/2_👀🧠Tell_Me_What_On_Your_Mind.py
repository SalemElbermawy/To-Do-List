import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

st.title("🧠 Mood AnalyzeeR")


st.markdown("""
Hey there! 👋  
This tool helps you **analyze your mood** from what you write and gives you **personalized advice** to feel better or maintain your good vibes.  
📝 Just type or paste anything on your mind below and see what your mood is!
""")

text = st.text_area("💬 Open up to me and tell me what's on your mind:", height=150)

advice_dict = {
    "good": [
        "Great! Keep doing what you love! 😄",
        "Awesome! Stay positive and enjoy your day! 🌟",
        "Keep up the good vibes! 🎉"
    ],
    "bad": [
        "Take a short break, breathe deeply, and relax. 😔",
        "It's okay to feel down. Try a calm activity. 🌿",
        "Rest a bit and do something that makes you happy. 💙"
    ],
    "neutral": [
        "Maintain your balance and stay calm. 😐",
        "Take things slowly and enjoy small moments. 🌸",
        "A calm mind helps you think clearly. 🕊️"
    ]
}

if st.button("Click here 🚀"):
    if text.strip():
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            mood = "GOOD 😊"
            advice = random.choice(advice_dict["good"])
        elif compound <= -0.05:
            mood = "BAD 😔"
            advice = random.choice(advice_dict["bad"])
        else:
            mood = "NEUTRAL 😐"
            advice = random.choice(advice_dict["neutral"])

        st.success(f"🌟 Mood: {mood}")
        st.info(f"💡 Advice: {advice}")
