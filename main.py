import streamlit as st

# App title
st.title("🧮 Unit Converter App")

# Conversion type selection
conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Conversion functions
def convert_length(value, unit_from, unit_to):
    factors = {"m":1, "cm":0.01, "mm":0.001, "km":1000, "inch":0.0254, "ft":0.3048}
    return value * factors[unit_from] / factors[unit_to]

def convert_weight(value, unit_from, unit_to):
    factors = {"kg":1, "g":0.001, "mg":0.000001, "lb":0.453592, "oz":0.0283495}
    return value * factors[unit_from] / factors[unit_to]

def convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return value
    if unit_from == "C":
        return value*9/5 + 32 if unit_to=="F" else value+273.15
    if unit_from == "F":
        return (value-32)*5/9 if unit_to=="C" else (value-32)*5/9+273.15
    if unit_from == "K":
        return value-273.15 if unit_to=="C" else (value-273.15)*9/5+32

# Units based on conversion type
if conversion_type == "Length":
    units = ["m","cm","mm","km","inch","ft"]
elif conversion_type == "Weight":
    units = ["kg","g","mg","lb","oz"]
else:
    units = ["C","F","K"]

# Input section
col1, col2 = st.columns(2)
with col1:
    value = st.number_input(f"Enter {conversion_type} value", value=0.0)
    unit_from = st.selectbox("From", units)
with col2:
    unit_to = st.selectbox("To", units)

# Conversion button
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, unit_from, unit_to)
    elif conversion_type == "Weight":
        result = convert_weight(value, unit_from, unit_to)
    else:
        result = convert_temperature(value, unit_from, unit_to)
    
    st.success(f"{value} {unit_from} = {result:.4f} {unit_to}")
