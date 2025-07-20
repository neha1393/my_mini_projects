import streamlit as st
import numpy as np
import pandas as pd 
#title of the project
st.title("My Second streamlit app")
st.write("This is a simple app to demonstrate the basic functionaities of streamlit")
#Interactive widget in sidebar
st.sidebar.header("User input features")
#text input 
username=st.sidebar.text_input("What is your name ?","Streamlit User")
#slider
age=st.sidebar.slider("select your age",0,100,25)
#select box
favorite_color=st.sidebar.selectbox("What is your favourite color?",["Blue","Yellow","Green","Red"])

#main page content
st.header(f'Welcome!,{username}')
st.write(f'You are {age} years old and your favourite color is {favorite_color}.')

#dislaying data 
st.subheader("Here is some random data: ")

#create sample dataframe
data=pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

#checkbox  to show or hide content
if st.checkbox("show raw data:"):
    st.subheader("Raw data")
    st.write(data)

#button to trigger an action
if st.button("Say Hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")