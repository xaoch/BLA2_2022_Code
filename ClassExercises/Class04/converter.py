import streamlit as st

st.title("Temparature Converter")

temperature = st.slider('What is the temperature?', -200, 200, 0)

converTo = st.radio(
    "To what unit you want to convert",
    ('Farenheit', 'Celcius'))

newTemp=0
unit=None

if (converTo =="Farenheit"):
    newTemp=(temperature*9/5)+32
    unit="Farenheit"
elif (converTo =="Celcius"):
    newTemp=(temperature-32)*5/9
    unit="Celcius"

st.markdown("The converted temperature is **{:.2f}** degrees {}".format(newTemp, unit))
