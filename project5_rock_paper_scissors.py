import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors 🎮", layout="centered")

# ASCII Art
rock = """
✊ ROCK
"""

paper = """
✋ PAPER
"""

scissors = """
✌️ SCISSORS
"""

choices = {
    "Rock": rock,
    "Paper": paper,
    "Scissors": scissors
}

st.title("🎮 Rock Paper Scissors")
st.write("Play against the computer and test your luck 😄")
st.divider()

# User choice
user_choice = st.radio(
    "Choose your move:",
    ["Rock", "Paper", "Scissors"],
    horizontal=True
)

if st.button("🔥 Play"):
    computer_choice = random.choice(list(choices.keys()))

    st.subheader("🧑 Your Choice")
    st.code(choices[user_choice])

    st.subheader("🤖 Computer Choice")
    st.code(choices[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        st.info("🤝 It's a DRAW!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.balloons()
        st.success("🎉 YOU WON!")
    else:
        st.error("😢 YOU LOST!")

st.divider()
st.caption("🎮 Built with Python & Streamlit | Day 6 of #100DaysOfCode")
