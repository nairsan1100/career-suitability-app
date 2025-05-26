import streamlit as st
from PIL import Image

st.set_page_config(page_title="Career Suitability Assessment", layout="centered")

st.title("🎯 Career Suitability Assessment")
st.caption("By YourCareerGuide.in")
st.write("Answer the following questions to discover careers that best match your aptitude, interests, personality, and values.")

responses = {}

st.header("🧬 Personality")
responses[f"Q7_{key_prefix}"] = st.radio("7. I prefer to work:", ["A. Alone", "B. With a team"])
responses[f"Q8_{key_prefix}"] = st.radio("8. I’m more:", ["A. Focused on details", "B. Focused on the big picture"])
responses[f"Q9_{key_prefix}"] = st.radio("9. When stressed, I:", ["A. Take time to reflect", "B. Talk to others for support"])

st.header("💡 Values")
responses[f"Q10_{key_prefix}"] = st.radio("10. Which is more important to you?", ["A. Job security", "B. Creative freedom"])
responses[f"Q11_{key_prefix}"] = st.radio("11. Would you rather:", ["A. Help others, even if pay is low", "B. Earn a high income"])
responses[f"Q12_{key_prefix}"] = st.radio("12. You value more:", ["A. Recognition & success", "B. Peace and balance"])

correct_answers = {f"Q1": "B", f"Q2_CO": "B", f"Q3_CO": "A", f"Q4_CO": "D", f"Q1": "B", f"Q2_HS": "A", f"Q3_HS": "D", f"Q4_HS": "C"}
dimension_mapping = {
    "Interest": [f"Q5", f"Q6"],
    "Personality": [f"Q7", f"Q8", f"Q9"],
    "Values": [f"Q10", f"Q11", f"Q12"]
}", f"Q6_{key_prefix}"],
    "Personality": [f"Q7_{key_prefix}", f"Q8_{key_prefix}", f"Q9_{key_prefix}"],
    "Values": [f"Q10_{key_prefix}", f"Q11_{key_prefix}", f"Q12_{key_prefix}"]
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
