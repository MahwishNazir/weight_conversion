import streamlit as st

# Conversion functions
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kg": 1, "pounds": 2.20462
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def convert_distance(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1, "kilometers": 0.001, "miles": 0.000621371
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Streamlit UI
st.title("🔄 Unit Converter")

category = st.selectbox("Choose a category", ["Weight", "Temperature", "Distance"])

if category == "Weight":
    units = ["kg", "pounds"]
elif category == "Temperature":
    units = ["Celsius", "Fahrenheit"]
elif category == "Distance":
    units = ["meters", "kilometers", "miles"]

from_unit = st.selectbox("Convert from", units)
to_unit = st.selectbox("Convert to", units)
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

if st.button("Convert"):
    if category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Distance":
        result = convert_distance(value, from_unit, to_unit)
    
    st.success(f"Converted Value: {result:.2f} {to_unit}")