import streamlit as st
import random

st.set_page_config(page_title="Password Generator 🔐")

st.title("🔐 PyPassword Generator")
st.write("Generate a strong and secure password easily 💪")

st.divider()

# Character sets (same as your code)
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User inputs (instead of input())
nr_letters = st.slider("🔤 How many letters?", min_value=1, max_value=20, value=8)
nr_symbols = st.slider("🔣 How many symbols?", min_value=0, max_value=10, value=2)
nr_numbers = st.slider("🔢 How many numbers?", min_value=0, max_value=10, value=2)

if st.button("🚀 Generate Password"):
    password = []

    for _ in range(nr_letters):
        password.append(random.choice(letters))

    for _ in range(nr_symbols):
        password.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)

    final_password = "".join(password)

    st.success("✅ Password Generated Successfully!")
    st.code(final_password)

    # Password strength indicator
    total_length = nr_letters + nr_symbols + nr_numbers

    if total_length >= 14 and nr_symbols > 0 and nr_numbers > 0:
        st.info("💪 Strength: VERY STRONG")
    elif total_length >= 10:
        st.info("👍 Strength: STRONG")
    else:
        st.warning("⚠️ Strength: WEAK")

st.divider()
st.caption("🔐 Built with Python & Streamlit | Day 6 of #100DaysOfCode")
