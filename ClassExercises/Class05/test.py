import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Chart")
df = px.data.gapminder().query("country=='Canada'")

st.write(df)

fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
st.plotly_chart(fig)
