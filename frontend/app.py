import os
import streamlit as st
from generator import generate_module, save_module

st.title("ModuLearn - Curriculum Builder")

st.sidebar.header("Module Options")
topic = st.sidebar.text_input("Topic", "Intro to Coding")
length = st.sidebar.slider("Length (days)", min_value=1, max_value=10, value=5)

if st.sidebar.button("Generate Module"):
    with st.spinner("Generating..."):
        module = generate_module(topic, length)
        os.makedirs("../data", exist_ok=True)
        save_module(module, f"../data/{topic.replace(' ', '_')}.json")
        st.success("Module generated!")
        st.json(module)
else:
    st.write("Enter a topic and click Generate Module to create a curriculum.")
