import streamlit as st
from PIL import Image

st.set_page_config(page_title="Career Suitability Assessment", layout="centered")

st.title("🎯 Career Suitability Assessment")
st.caption("By YourCareerGuide.in")
st.write("Answer the following questions to discover careers that best match your aptitude, interests, personality, and values.")

user_group = st.radio("Who are you?", ["🎒 High School Student", "🎓 College Student"])
responses = {}

if user_group == "🎒 High School Student":
    st.header("🧠 Aptitude")
    responses["Q1"] = st.radio("1. Which number comes next? 2, 4, 6, 8, ___", ["A. 9", "B. 10", "C. 12", "D. 11"])
    responses["Q2"] = st.radio("2. What is the opposite of 'happy'?", ["A. Sad", "B. Angry", "C. Excited", "D. Tired"])
    responses["Q3"] = st.radio("3. Which object does not belong? Pen, Pencil, Eraser, Apple", ["A. Pen", "B. Pencil", "C. Eraser", "D. Apple"])
    responses["Q4"] = st.radio("4. Book is to Reading as Spoon is to __?", ["A. Writing", "B. Stirring", "C. Eating", "D. Drawing"])

    st.header("🎨 Interest")
    responses["Q5"] = st.radio("5. What sounds more fun to you?", ["A. Building a model", "B. Solving a riddle", "C. Drawing a poster", "D. Helping a classmate"])
    responses["Q6"] = st.radio("6. Choose one:", ["A. Organize a shelf", "B. Lead a group", "C. Design a card", "D. Fix a toy"])
else:
    st.header("🧠 Aptitude")
    responses["Q1"] = st.radio("1. What is the next number in the series: 3, 6, 12, 24, ___?", ["A. 36", "B. 48", "C. 40", "D. 30"])
    responses["Q2"] = st.radio("2. Which word is the opposite of 'benevolent'?", ["A. Kind", "B. Cruel", "C. Friendly", "D. Honest"])
    responses["Q3"] = st.radio("3. Which number doesn’t belong: 2, 3, 5, 7, 9, 11?", ["A. 9", "B. 11", "C. 7", "D. 3"])
    responses["Q4"] = st.radio("4. Book is to Reading as Fork is to __?", ["A. Drawing", "B. Writing", "C. Stirring", "D. Eating"])

    st.header("🎨 Interest")
    responses["Q5"] = st.radio("5. Would you rather:", ["A. Fix a broken fan", "B. Solve a math puzzle", "C. Write a poem", "D. Lead a discussion group"])
    responses["Q6"] = st.radio("6. Would you rather:", ["A. Organize an event", "B. Sort files", "C. Design a logo", "D. Build a model airplane"])
responses["Q5"] = st.radio("5. Would you rather:", [
    "A. Fix a broken fan", "B. Solve a math puzzle", "C. Write a poem", "D. Lead a discussion group"])
responses["Q6"] = st.radio("6. Would you rather:", [
    "A. Organize an event", "B. Sort files", "C. Design a logo", "D. Build a model airplane"])

st.header("🧬 Personality")
responses["Q7"] = st.radio("7. I prefer to work:", ["A. Alone", "B. With a team"])
responses["Q8"] = st.radio("8. I’m more:", ["A. Focused on details", "B. Focused on the big picture"])
responses["Q9"] = st.radio("9. When stressed, I:", ["A. Take time to reflect", "B. Talk to others for support"])

st.header("💡 Values")
responses["Q10"] = st.radio("10. Which is more important to you?", ["A. Job security", "B. Creative freedom"])
responses["Q11"] = st.radio("11. Would you rather:", ["A. Help others, even if pay is low", "B. Earn a high income"])
responses["Q12"] = st.radio("12. You value more:", ["A. Recognition & success", "B. Peace and balance"])

correct_answers = {"Q1": "B", "Q2": "B", "Q3": "A", "Q4": "D"}
dimension_mapping = {
    "Interest": ["Q5", "Q6"],
    "Personality": ["Q7", "Q8", "Q9"],
    "Values": ["Q10", "Q11", "Q12"]
}
scores = {"Aptitude": 0, "Interest": 0, "Personality": 0, "Values": 0}

for q in correct_answers:
    if responses.get(q, "").startswith(correct_answers[q]):
        scores["Aptitude"] += 5
for dim, questions in dimension_mapping.items():
    for q in questions:
        if responses.get(q, "").startswith("A"):
            scores[dim] += 5

weights = {"Aptitude": 0.30, "Interest": 0.30, "Personality": 0.25, "Values": 0.15}
weighted_scores = {
    dim: round((score / 20) * 100 * weights[dim], 2)
    for dim, score in scores.items()
}
total_score = sum(weighted_scores.values())

career_profiles = {
    "Software Engineer 💻": {"Aptitude": 18, "Interest": 15, "Personality": 14, "Values": 12},
    "Graphic Designer 🎨": {"Aptitude": 14, "Interest": 18, "Personality": 16, "Values": 15},
    "Civil Services Officer 🏛️": {"Aptitude": 17, "Interest": 14, "Personality": 15, "Values": 18},
    "Entrepreneur 🚀": {"Aptitude": 16, "Interest": 17, "Personality": 15, "Values": 14},
    "Teacher 👩‍🏫": {"Aptitude": 14, "Interest": 12, "Personality": 16, "Values": 18},
    "Digital Marketer 📱": {"Aptitude": 12, "Interest": 16, "Personality": 14, "Values": 13},
    "Chartered Accountant (CA) 💼": {"Aptitude": 18, "Interest": 14, "Personality": 15, "Values": 12},
    "IAS/IPS Officer 🛡️": {"Aptitude": 17, "Interest": 15, "Personality": 16, "Values": 18},
    "Data Scientist 📊": {"Aptitude": 18, "Interest": 17, "Personality": 14, "Values": 13},
    "Doctor (MBBS) 🩺": {"Aptitude": 17, "Interest": 15, "Personality": 15, "Values": 16},
    "Lawyer ⚖️": {"Aptitude": 15, "Interest": 16, "Personality": 17, "Values": 14},
    "Architect 🏗️": {"Aptitude": 14, "Interest": 18, "Personality": 16, "Values": 13},
    "UX/UI Designer 🖌️": {"Aptitude": 13, "Interest": 18, "Personality": 15, "Values": 14},
    "Sports Coach / Athlete 🏅": {"Aptitude": 14, "Interest": 17, "Personality": 17, "Values": 15},
    "YouTuber / Content Creator 📹": {"Aptitude": 12, "Interest": 18, "Personality": 16, "Values": 13},
    "Psychologist / Counselor 🧠": {"Aptitude": 14, "Interest": 13, "Personality": 18, "Values": 17}
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
