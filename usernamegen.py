import streamlit as st 

st.title("USERNAME GENERATOR")

Nickname = st.text_input("Enter your nickname")
First_name = st.text_input("Enter your first name")
yearofbirth = st.text_input("Enter your year of birth (YYYY)")

# Check if all fields are filled first
if st.button("Generate Username Now"):
    # do something

    if Nickname and First_name and yearofbirth:
        if len(yearofbirth) == 4 and yearofbirth.isdigit():
            username = Nickname.lower().strip() + '_' + First_name.lower().strip() + yearofbirth
            st.success(f"Your username is: {username}")
        else:
            st.error("Enter a valid 4-digit year")
