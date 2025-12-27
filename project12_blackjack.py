import streamlit as st
import random

st.set_page_config(page_title="Blackjack ♠️", layout="centered")

# ---------------- DATA ----------------
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    while 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)

# ---------------- SESSION STATE ----------------
if "user_cards" not in st.session_state:
    st.session_state.user_cards = []
    st.session_state.computer_cards = []
    st.session_state.started = False
    st.session_state.game_over = False
    st.session_state.stand = False

# ---------------- CALLBACKS ----------------
def start_game():
    st.session_state.user_cards = [deal_card(), deal_card()]
    st.session_state.computer_cards = [deal_card(), deal_card()]
    st.session_state.started = True
    st.session_state.game_over = False
    st.session_state.stand = False
    st.rerun()

def hit():
    st.session_state.user_cards.append(deal_card())
    if calculate_score(st.session_state.user_cards) > 21:
        st.session_state.game_over = True
    st.rerun()

def stand():
    st.session_state.stand = True
    st.rerun()

def reset_game():
    st.session_state.user_cards = []
    st.session_state.computer_cards = []
    st.session_state.started = False
    st.session_state.game_over = False
    st.session_state.stand = False
    st.rerun()

# ---------------- UI ----------------
st.title("♠️ Blackjack")
st.caption("Beat the dealer without going over 21")
st.divider()

# ---------------- START ----------------
if not st.session_state.started:
    st.button("🎮 Start Game", on_click=start_game)

# ---------------- GAME PLAY ----------------
if st.session_state.started:
    user_score = calculate_score(st.session_state.user_cards)

    st.subheader(f"Your Cards: {st.session_state.user_cards}")
    st.write(f"Your Score: **{user_score}**")

    st.subheader(f"Dealer's First Card: [{st.session_state.computer_cards[0]}]")

    # Bust check
    if user_score > 21:
        st.error("💥 You went over 21! You lose.")
        st.session_state.game_over = True

    # Action buttons
    if not st.session_state.game_over and not st.session_state.stand:
        col1, col2 = st.columns(2)
        with col1:
            st.button("➕ Hit", on_click=hit)
        with col2:
            st.button("✋ Stand", on_click=stand)

    # Dealer logic
    if st.session_state.stand and not st.session_state.game_over:
        while calculate_score(st.session_state.computer_cards) < 17:
            st.session_state.computer_cards.append(deal_card())
        st.session_state.game_over = True

    # ---------------- FINAL RESULT ----------------
    if st.session_state.game_over:
        dealer_score = calculate_score(st.session_state.computer_cards)

        st.divider()
        st.subheader("📊 Final Results")

        st.write(f"Your Hand: {st.session_state.user_cards} → {user_score}")
        st.write(f"Dealer Hand: {st.session_state.computer_cards} → {dealer_score}")

        if user_score > 21:
            st.error("You lose 😞")
        elif dealer_score > 21:
            st.success("You win 🎉")
        elif user_score > dealer_score:
            st.success("You win 🎉")
        elif user_score < dealer_score:
            st.error("You lose 😞")
        else:
            st.warning("It's a draw 🤝")

        st.button("🔁 Play Again", on_click=reset_game)

st.caption("Built with Python & Streamlit | Day 12 of #100DaysOfCode")
