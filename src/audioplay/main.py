# TODO: - Basic Intro Page
import streamlit as st


def greet_intro():
    greet = st.text_input("Please Input your name", type="default")
    if greet:
        st.write("Welcome 😊", greet)


greet_intro()
