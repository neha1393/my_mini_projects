import streamlit as st

st.title("BMI Calculator")

Weight = st.number_input("Enter your weight (in kg): ")
Height = st.number_input("Enter your height (in cm): ")

if st.button("Generate BMI"):
    if Weight > 0 and Height > 0:
        BMI = Weight / ((Height / 100) ** 2)
        st.write("The BMI is:", round(BMI, 2))

        if BMI < 18.5:
            st.info("You are underweight.")
        elif BMI < 24.9:
            st.success("You have a normal weight.")
        elif BMI < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Enter valid weight and height.")
