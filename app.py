import streamlit as st
st.title("My first web app")
st.write("Welcome to my AI journey")
name=st.text_input("enter your name:")
if name:
    st.write(f"hello,{name}!")