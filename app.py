import streamlit as st
import math

# Title for the calculator app
st.title("Enhanced Calculator with Streamlit")

# Create a dropdown to choose the type of calculation
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", 
                                              "Square Root", "Logarithm (Base 10)", "Natural Logarithm", 
                                              "Sine", "Cosine", "Tangent"])

# Basic Operations
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
    
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == "Exponentiation":
        result = num1 ** num2

    if st.button("Calculate"):
        st.write(f"The result of {operation} is: {result}")

# Square root
elif operation == "Square Root":
    num = st.number_input("Enter a number", min_value=0.0, format="%f")
    if st.button("Calculate Square Root"):
        st.write(f"The square root of {num} is: {math.sqrt(num)}")

# Logarithmic Operations
elif operation == "Logarithm (Base 10)":
    num = st.number_input("Enter a positive number", min_value=0.0, format="%f")
    if st.button("Calculate Logarithm (Base 10)"):
        st.write(f"The log base 10 of {num} is: {math.log10(num)}")
        
elif operation == "Natural Logarithm":
    num = st.number_input("Enter a positive number", min_value=0.0, format="%f")
    if st.button("Calculate Natural Logarithm"):
        st.write(f"The natural log (ln) of {num} is: {math.log(num)}")

# Trigonometric Functions
elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter angle in degrees")
    radian = math.radians(angle)
    
    if operation == "Sine":
        result = math.sin(radian)
    elif operation == "Cosine":
        result = math.cos(radian)
    elif operation == "Tangent":
        result = math.tan(radian)
        
    if st.button(f"Calculate {operation}"):
        st.write(f"The {operation.lower()} of {angle} degrees is: {result}")

# Footer information
st.write("Developed with ❤️ using Streamlit")

