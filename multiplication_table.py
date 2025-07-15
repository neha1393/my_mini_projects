import streamlit as st 

st.title("Multiplication Table")

Number=st.number_input("Enter a number :",step=1.0)
if st.button("Generate Table"):
    for i in range(1,11):
        result=Number*i
        st.success(f'{int(Number)} x {i} = {int(result)}')
