import streamlit as st
st.title("🎉 My First Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    st.success(f"Hello, {name}! 👋 Welcome to Streamlit!")

mood = st.slider("How do you feel today?", 0, 10, 5)
st.write(f"Your mood level: {mood}/10")

if st.checkbox("Show a fun fact"):
    st.info("Did you know? Streamlit lets you build apps super fast!")

st.caption("Made with ❤️ using Streamlit")
