
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Career Suitability Assessment", layout="centered")

# Optional logo (replace with your own image path or URL)
# logo = Image.open("logo.png")
# st.image(logo, width=120)

st.title("🎯 Career Suitability Assessment")
st.caption("By YourCareerGuide.in")
st.write("Answer the following questions to discover careers that best match your aptitude, interests, personality, and values.")

# Store responses
responses = {}

st.header("🧠 Aptitude")
responses["Q1"] = st.radio("1. What is the next number in the series: 3, 6, 12, 24, ___?", ["A", "B", "C", "D"])
responses["Q2"] = st.radio("2. Opposite of 'benevolent'?", ["A", "B", "C", "D"])
responses["Q3"] = st.radio("3. Which number doesn’t belong: 2, 3, 5, 7, 9, 11?", ["A", "B", "C", "D"])
responses["Q4"] = st.radio("4. Book is to Reading as Fork is to __?", ["A", "B", "C", "D"])

st.header("🎨 Interest")
responses["Q5"] = st.radio("5. Would you rather fix a broken fan or lead a discussion group?", ["A", "B", "C", "D"])
responses["Q6"] = st.radio("6. Would you rather design a logo or build a model airplane?", ["A", "B", "C", "D"])

st.header("🧬 Personality")
responses["Q7"] = st.radio("7. I prefer to work:", ["A", "B"])
responses["Q8"] = st.radio("8. I’m more:", ["A", "B"])
responses["Q9"] = st.radio("9. When stressed, I:", ["A", "B"])

st.header("💡 Values")
responses["Q10"] = st.radio("10. Which is more important to you?", ["A", "B"])
responses["Q11"] = st.radio("11. Would you rather help others or earn more?", ["A", "B"])
responses["Q12"] = st.radio("12. You value more:", ["A", "B"])

# Define scoring logic
correct_answers = {"Q1": "B", "Q2": "B", "Q3": "A", "Q4": "D"}
dimension_mapping = {
    "Interest": ["Q5", "Q6"],
    "Personality": ["Q7", "Q8", "Q9"],
    "Values": ["Q10", "Q11", "Q12"]
}
scores = {"Aptitude": 0, "Interest": 0, "Personality": 0, "Values": 0}

# Calculate scores
for q in correct_answers:
    if responses.get(q) == correct_answers[q]:
        scores["Aptitude"] += 5
for dim, questions in dimension_mapping.items():
    for q in questions:
        if responses.get(q) == "A":
            scores[dim] += 5

# Weighted scoring
weights = {"Aptitude": 0.30, "Interest": 0.30, "Personality": 0.25, "Values": 0.15}
weighted_scores = {
    dim: round((score / 20) * 100 * weights[dim], 2)
    for dim, score in scores.items()
}
total_score = sum(weighted_scores.values())

# Match careers
career_profiles = {
    "Software Engineer 💻": {"Aptitude": 18, "Interest": 15, "Personality": 14, "Values": 12},
    "Graphic Designer 🎨": {"Aptitude": 14, "Interest": 18, "Personality": 16, "Values": 15},
    "Civil Services Officer 🏛️": {"Aptitude": 17, "Interest": 14, "Personality": 15, "Values": 18},
    "Entrepreneur 🚀": {"Aptitude": 16, "Interest": 17, "Personality": 15, "Values": 14},
    "Teacher 👩‍🏫": {"Aptitude": 14, "Interest": 12, "Personality": 16, "Values": 18},
    "Digital Marketer 📱": {"Aptitude": 12, "Interest": 16, "Personality": 14, "Values": 13}
}

if st.button("🔍 Get My Career Match"):
    st.subheader("Your Weighted Scores")
    for dim, score in weighted_scores.items():
        st.write(f"{dim}: {score}%")
    st.write(f"\nTotal Suitability Score: {total_score}%")

    st.subheader("Top Career Matches")
    career_scores = {}
    for career, ideal in career_profiles.items():
        match_score = 0
        for dim in scores:
            match_score += (min(scores[dim], ideal[dim]) / ideal[dim]) * weights[dim] * 100
        career_scores[career] = round(match_score, 2)

    sorted_matches = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    for career, score in sorted_matches:
        st.write(f"{career}: {score}% match")
