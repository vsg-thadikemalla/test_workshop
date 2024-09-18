import streamlit as st

# Streamlit app title
st.title("Area Calculator")

# Input for length and width
length = st.number_input("Enter Length:", min_value=0.0, step=0.1)
width = st.number_input("Enter Width:", min_value=0.0, step=0.1)

# Calculate the area
if st.button("Calculate Area"):
    area = length * width
    st.write(f"The area is: {area} square units")
