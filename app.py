import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Career Fit Tool", layout="centered")

# Auth0 login script
st.markdown("""
    <script src="https://cdn.auth0.com/js/auth0-spa-js/1.13/auth0-spa-js.production.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", async () => {
        const auth0 = await createAuth0Client({
          domain: 'dev-hfz67rcatqi8c8u5.us.auth0.com',
          client_id: 'JTUA5YbIkq3NUtiLjVFF390nMAsxd2e6',
          cacheLocation: 'localstorage',
          useRefreshTokens: true,
          redirect_uri: window.location.origin
        });

        const isAuthenticated = await auth0.isAuthenticated();
        if (!isAuthenticated) {
          await auth0.loginWithRedirect();
        } else {
          const user = await auth0.getUser();
          window.parent.postMessage(JSON.stringify({type: 'auth', email: user.email, name: user.name}), '*');
        }
      });
    </script>
""", unsafe_allow_html=True)

email = st.experimental_get_query_params().get("email", [None])[0]
if not email:
    st.warning("Please wait for authentication...")
    st.stop()

st.sidebar.success(f"Welcome {email} 👋")

st.title("🎯 Career Fit Tool")
st.write("You're now securely logged in via Auth0.")

# Career assessment introduction
st.subheader("Let's find your best-fit career")
st.markdown("Please answer the following 12 questions to get a personalized career match based on your aptitude, interests, personality, and values.")

responses = {}

# Questions
questions = [
    ("Q1", "What is the next number in the series: 3, 6, 12, 24, ___?", ["A. 36", "B. 48", "C. 40", "D. 30"]),
    ("Q2", "Which word is the opposite of 'benevolent'?", ["A. Kind", "B. Cruel", "C. Friendly", "D. Honest"]),
    ("Q3", "Which number doesn’t belong: 2, 3, 5, 7, 9, 11?", ["A. 9", "B. 11", "C. 7", "D. 3"]),
    ("Q4", "Book is to Reading as Fork is to __?", ["A. Drawing", "B. Writing", "C. Stirring", "D. Eating"]),
    ("Q5", "Would you rather fix a broken fan or lead a discussion group?", ["A. Fix a broken fan", "B. Solve a math puzzle", "C. Write a poem", "D. Lead a discussion group"]),
    ("Q6", "Would you rather design a logo or build a model airplane?", ["A. Organize an event", "B. Sort files", "C. Design a logo", "D. Build a model airplane"]),
    ("Q7", "I prefer to work:", ["A. Alone", "B. With a team"]),
    ("Q8", "I’m more:", ["A. Focused on details", "B. Focused on the big picture"]),
    ("Q9", "When stressed, I:", ["A. Take time to reflect", "B. Talk to others for support"]),
    ("Q10", "Which is more important to you?", ["A. Job security", "B. Creative freedom"]),
    ("Q11", "Would you rather:", ["A. Help others, even if pay is low", "B. Earn a high income"]),
    ("Q12", "You value more:", ["A. Recognition & success", "B. Peace and balance"]),
]

for qid, question, options in questions:
    responses[qid] = st.radio(question, options, key=qid)

# Scoring and recommendation logic
import datetime
import csv

if st.button("🔍 Get My Career Match"):
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
        "Digital Marketer 📱": {"Aptitude": 12, "Interest": 16, "Personality": 14, "Values": 13}
    }

    st.subheader("Your Weighted Scores")
    for dim, score in weighted_scores.items():
        st.write(f"{dim}: {score}%")
    st.write(f"
Total Suitability Score: {total_score}%")

    st.subheader("Top Career Matches")
    career_scores = {}
    for career, ideal in career_profiles.items():
        match_score = 0
        for dim in scores:
            match_score += (min(scores[dim], ideal[dim]) / ideal[dim]) * weights[dim] * 100
        career_scores[career] = round(match_score, 2)

    sorted_matches = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
        timestamp = datetime.datetime.now().isoformat()
    top_match = sorted_matches[0][0]
    with open("responses_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, email, total_score, top_match])

    for career, score in sorted_matches:
        st.write(f"{career}: {score}% match")    responses[qid] = st.radio(question, options, key=qid)
