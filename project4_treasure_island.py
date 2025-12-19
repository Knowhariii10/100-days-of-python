import streamlit as st

st.set_page_config(page_title="Treasure Island Adventure 🏝️")

st.title("🏴‍☠️ Treasure Island Adventure")
st.write("🎯 **Goal:** Make smart choices and find the hidden treasure!")
st.divider()


if "stage" not in st.session_state:
    st.session_state.stage = "start"


if st.session_state.stage == "start":
    st.subheader("🚪 You arrive at a mysterious island")
    st.write("Two paths lie ahead. Each path is dangerous.")

    choice = st.radio(
        "Which direction will you choose?",
        ["⬅️ Left Path", "➡️ Right Path"]
    )

    if st.button("Continue"):
        if choice == "⬅️ Left Path":
            st.session_state.stage = "left_forest"
        else:
            st.session_state.stage = "right_cave"


elif st.session_state.stage == "left_forest":
    st.subheader("🌲 Left Path: Dark Forest")
    st.write("You enter a forest filled with strange sounds.")

    choice = st.radio(
        "What will you do?",
        ["🔥 Light a torch", "👣 Walk quietly"]
    )

    if st.button("Next"):
        if choice == "🔥 Light a torch":
            st.session_state.stage = "forest_river"
        else:
            st.session_state.stage = "forest_trap"

elif st.session_state.stage == "forest_trap":
    st.error("🕸️ You stepped into a hidden trap!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"

elif st.session_state.stage == "forest_river":
    st.subheader("🌊 Forest River")
    st.write("A river blocks your path.")

    choice = st.radio(
        "How will you cross?",
        ["⛵ Use a small boat", "🏊 Swim across"]
    )

    if st.button("Cross"):
        if choice == "⛵ Use a small boat":
            st.session_state.stage = "left_temple"
        else:
            st.session_state.stage = "river_crocodile"

elif st.session_state.stage == "river_crocodile":
    st.error("🐊 Crocodiles attacked you while swimming!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"

elif st.session_state.stage == "left_temple":
    st.subheader("🏛️ Ancient Temple")
    st.write("You see two doors inside the temple.")

    choice = st.radio(
        "Which door do you open?",
        ["🚪 Golden Door", "🚪 Stone Door"]
    )

    if st.button("Open Door"):
        if choice == "🚪 Golden Door":
            st.session_state.stage = "win"
        else:
            st.session_state.stage = "snake_room"

elif st.session_state.stage == "snake_room":
    st.error("🐍 Poisonous snakes attack you!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"

elif st.session_state.stage == "right_cave":
    st.subheader("🕳️ Right Path: Dark Cave")
    st.write("The cave is cold and silent.")

    choice = st.radio(
        "What will you do?",
        ["🔦 Turn on flashlight", "🚶 Walk in darkness"]
    )

    if st.button("Next"):
        if choice == "🔦 Turn on flashlight":
            st.session_state.stage = "cave_bridge"
        else:
            st.session_state.stage = "fall_pit"

elif st.session_state.stage == "fall_pit":
    st.error("🕳️ You fell into a deep pit!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"

elif st.session_state.stage == "cave_bridge":
    st.subheader("🌉 Broken Bridge")
    st.write("A broken bridge stands in front of you.")

    choice = st.radio(
        "How will you cross?",
        ["🪢 Use a rope", "🤞 Jump carefully"]
    )

    if st.button("Cross"):
        if choice == "🪢 Use a rope":
            st.session_state.stage = "right_chamber"
        else:
            st.session_state.stage = "bridge_fall"

elif st.session_state.stage == "bridge_fall":
    st.error("💥 You slipped and fell!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"

elif st.session_state.stage == "right_chamber":
    st.subheader("💎 Hidden Chamber")
    st.write("You see two chests.")

    choice = st.radio(
        "Which chest will you open?",
        ["📦 Old Wooden Chest", "📦 Shiny Chest"]
    )

    if st.button("Open Chest"):
        if choice == "📦 Old Wooden Chest":
            st.session_state.stage = "win"
        else:
            st.session_state.stage = "explosion"

elif st.session_state.stage == "explosion":
    st.error("💣 The chest exploded!")
    st.write("❌ GAME OVER")

    if st.button("🔁 Restart"):
        st.session_state.stage = "start"


elif st.session_state.stage == "win":
    st.balloons()
    st.success("🎉 CONGRATULATIONS!")
    st.write("💰 You found the hidden treasure and escaped safely!")

    if st.button("🔁 Play Again"):
        st.session_state.stage = "start"

st.divider()
st.caption("🎮 Built with Python & Streamlit | Interactive Adventure Game")
