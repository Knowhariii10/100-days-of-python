import streamlit as st
import random

st.set_page_config(page_title="Higher Lower 🔼🔽", layout="centered")

# ---------------- DATA ----------------
data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 149, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Neymar', 'follower_count': 138, 'description': 'Footballer', 'country': 'Brasil'},
    {'name': 'National Geographic', 'follower_count': 135, 'description': 'Magazine', 'country': 'United States'},
    {'name': 'Taylor Swift', 'follower_count': 131, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 55, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Ronaldinho', 'follower_count': 51, 'description': 'Footballer', 'country': 'Brasil'}
]

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.a = random.choice(data)
    st.session_state.b = random.choice(data)
    st.session_state.game_over = False

def pick_new_b():
    st.session_state.b = random.choice(data)
    while st.session_state.b == st.session_state.a:
        st.session_state.b = random.choice(data)

# ---------------- UI ----------------
st.title("🔼 Higher Lower Game")
st.caption("Who has more followers?")
st.divider()

# ---------------- GAME OVER ----------------
if st.session_state.game_over:
    st.error(f"❌ Game Over! Final Score: {st.session_state.score}")
    if st.button("🔁 Play Again"):
        st.session_state.score = 0
        st.session_state.a = random.choice(data)
        pick_new_b()
        st.session_state.game_over = False

# ---------------- GAME PLAY ----------------
if not st.session_state.game_over:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🅰️ Compare A")
        st.write(f"**{st.session_state.a['name']}**")
        st.write(st.session_state.a['description'])
        st.write(st.session_state.a['country'])

    with col2:
        st.subheader("🅱️ Compare B")
        st.write(f"**{st.session_state.b['name']}**")
        st.write(st.session_state.b['description'])
        st.write(st.session_state.b['country'])

    st.divider()
    st.write(f"🔥 Current Score: **{st.session_state.score}**")

    colA, colB = st.columns(2)

    with colA:
        if st.button("⬅️ A has more followers"):
            if st.session_state.a['follower_count'] > st.session_state.b['follower_count']:
                st.session_state.score += 1
                st.session_state.a = st.session_state.b
                pick_new_b()
            else:
                st.session_state.game_over = True

    with colB:
        if st.button("➡️ B has more followers"):
            if st.session_state.b['follower_count'] > st.session_state.a['follower_count']:
                st.session_state.score += 1
                st.session_state.a = st.session_state.b
                pick_new_b()
            else:
                st.session_state.game_over = True

st.caption("Built with Python & Streamlit | Day 14 of #100DaysOfCode")
