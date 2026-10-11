
import streamlit as st

st.set_page_config(
    page_title="How Many?",
    page_icon="🎮",
    layout="wide"
)

# Game categories
OBJECTS = [
    "Chickens",
    "Million Dollars",
    "Cats",
    "Whales",
    "Dogs",
    "Random People",
    "Giraffes",
    "Puppets",
    "AI's",
    "Spidermans",
    "Pregnant Women",
    "Grandmas",
    "Bugs",
    "McDonalds"
]

# Game state: each visitor gets their own game
if "hm_index" not in st.session_state:
    st.session_state.hm_index = 0

if "hm_value" not in st.session_state:
    st.session_state.hm_value = 0

if "hm_ended" not in st.session_state:
    st.session_state.hm_ended = False


def change_value(amount):
    st.session_state.hm_value += amount


def submit_value():
    if st.session_state.hm_index < len(OBJECTS) - 1:
        st.session_state.hm_index += 1
        st.session_state.hm_value = 0
    else:
        st.session_state.hm_ended = True


# Dark dashboard styling
st.markdown("""
<style>
.stApp {
    background-color: #0F111A;
    color: #FFFFFF;
}
[data-testid="stSidebar"] {
    background-color: #161925;
}
h1, h2, h3, p, label {
    color: #FFFFFF;
}
.game-card {
    background: #161925;
    border: 1px solid #24283B;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    margin: 20px 0;
}
.game-value {
    color: #00ADB5;
    font-size: 48px;
    font-weight: bold;
}
div.stButton > button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown("## 🎮 DASHBOARD")
    st.markdown("---")

    if not st.session_state.hm_ended:
        st.caption("CURRENT ROUND")
        st.markdown(
            f"### STAGE {st.session_state.hm_index + 1:02d}"
        )
        st.markdown("🟢 ACTIVE")
        st.progress(
            (st.session_state.hm_index + 1) / len(OBJECTS)
        )
    else:
        st.markdown("### GAME ENDED")
        st.caption("Thanks for playing!")

    st.markdown("---")
    st.caption("HOW MANY?")
    st.caption("Count your worth in different things.")


# Main game
st.markdown("# HOW MANY?")
st.markdown(
    "### Find out how many of each thing you think you are worth."
)

if st.session_state.hm_ended:
    st.success("🏁 The game actually ended!")
    st.markdown("## You completed all the stages!")

    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.hm_index = 0
        st.session_state.hm_value = 0
        st.session_state.hm_ended = False
        st.rerun()

else:
    current_object = OBJECTS[st.session_state.hm_index]

    st.markdown(
        f"## How Many {current_object} Are You Worth?"
    )

    st.markdown(
        f"""
        <div class="game-card">
            <div class="game-value">
                {st.session_state.hm_value:,}
            </div>
            <p>You Are {st.session_state.hm_value:,}
            {current_object} Worth</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Increase buttons
    st.markdown("### ➕ Increase")
    plus1, plus10, plus100 = st.columns(3)

    with plus1:
        st.button(
            "+1",
            on_click=change_value,
            args=(1,),
            use_container_width=True,
            key="hm_plus1"
        )

    with plus10:
        st.button(
            "+10",
            on_click=change_value,
            args=(10,),
            use_container_width=True,
            key="hm_plus10"
        )

    with plus100:
        st.button(
            "+100",
            on_click=change_value,
            args=(100,),
            use_container_width=True,
            key="hm_plus100"
        )

    # Decrease buttons
    st.markdown("### ➖ Decrease")
    minus1, minus10, minus100 = st.columns(3)

    with minus1:
        st.button(
            "-1",
            on_click=change_value,
            args=(-1,),
            use_container_width=True,
            key="hm_minus1"
        )

    with minus10:
        st.button(
            "-10",
            on_click=change_value,
            args=(-10,),
            use_container_width=True,
            key="hm_minus10"
        )

    with minus100:
        st.button(
            "-100",
            on_click=change_value,
            args=(-100,),
            use_container_width=True,
            key="hm_minus100"
        )

    st.markdown("---")

    st.button(
        "SUBMIT VALUE →",
        on_click=submit_value,
        use_container_width=True,
        type="primary",
        key="hm_submit"
    )

    st.caption(
        f"Stage {st.session_state.hm_index + 1} "
        f"of {len(OBJECTS)}"
    )
