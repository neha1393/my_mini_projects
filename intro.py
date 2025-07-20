import streamlit as st
st.title("MY FIRST STREAMLIT APP")
st.write("Welcome! the application tracks the square of a number.")
st.header("Select a number")
number=st.slider("pick a number",0,100,25)
st.subheader("Result")
squared_number=number*number
st.write(f"The square of {number} is {squared_number}.")