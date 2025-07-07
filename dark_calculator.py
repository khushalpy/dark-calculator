import streamlit as st

# Set page config for dark theme feeling
st.set_page_config(page_title="Dark Calculator 💀",
                   page_icon="🖤", layout="centered")

# Custom CSS for full dark styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #C0C0C0;
    }
    .stButton>button {
        background-color: #1F1F1F;
        color: #C0C0C0;
        border: 1px solid #2C2C2C;
        height: 60px;
        width: 80px;
        margin: 2px;
        font-size: 20px;
    }
    .stTextInput>div>div>input {
        background-color: #1F1F1F;
        color: #C0C0C0;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🖤 Dark Calculator 💀")

# Display
if 'expression' not in st.session_state:
    st.session_state.expression = ""

st.text_input("Screen", st.session_state.expression,
              key="display", disabled=True)

# Buttons
cols = st.columns(4)
buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", ".", "=", "+"]

for i, b in enumerate(buttons):
    if cols[i % 4].button(b):
        if b == "=":
            try:
                st.session_state.expression = str(
                    eval(st.session_state.expression))
            except:
                st.session_state.expression = "Error"
        else:
            st.session_state.expression += b

# Clear and Backspace buttons
col_clear, col_back = st.columns(2)
if col_clear.button("Clear"):
    st.session_state.expression = ""
if col_back.button("⌫"):
    st.session_state.expression = st.session_state.expression[:-1]
