import streamlit as st
import pandas as pd
import plotly.express as px

st.title("School Data")
schoolData = pd.read_csv('data/schoolData.csv')
frpl = pd.read_csv('data/frpl.csv')

# Data Cleaning
# School Data
## Keep only the totals
mask = schoolData['school_group'].isnull()
schoolData=schoolData[mask]

## Select only the necesary columns
schoolData= schoolData.drop(columns=["school_group", "grade", "pi_pct", "blank_col"])

## Remove Grand Total
mask = schoolData["school_name"] != "Grand Total"
schoolData = schoolData[mask]

## Remove "Total" from Name
schoolData["school_name"]= schoolData["school_name"].str.replace("Total","")

## Trim names
schoolData["school_name"]= schoolData["school_name"].str.strip()

## Convert percentages to numeric
def convertToNumber(column):
    column= column.str.replace("%","")
    column= pd.to_numeric(column)
    return column

schoolData["na_pct"]=convertToNumber(schoolData["na_pct"])
schoolData["aa_pct"]=convertToNumber(schoolData["aa_pct"])
schoolData["as_pct"]=convertToNumber(schoolData["as_pct"])
schoolData["hi_pct"]=convertToNumber(schoolData["hi_pct"])
schoolData["hi_pct"]=convertToNumber(schoolData["wh_pct"])

# FRPL

## We remove the rows in which the name of the school is blank. Use "Filter" in the column and then "Remove NA"
frpl["school_name"]= frpl["school_name"].dropna()

## Remove any row in which the school name is: "ELM K_08", "Mid Schl", "High Schl", "Alt HS", "Spec Ed Total", "Cont Alt Total", "Hospital Sites Total", "Dist Total".
mask = ~ frpl["school_name"].isin(["ELM K_08", "Mid Schl", "High Schl", "Alt HS", "Spec Ed Total", "Cont Alt Total", "Hospital Sites Total", "Dist Total"])
frpl=frpl[mask]


## convert percentages
#frpl["frpl_pct"]=pd.to_numeric(frpl["frpl_pct"].str.replace("%",""))
frpl["frpl_pct"]=convertToNumber(frpl["frpl_pct"])

# Data Wrangling
## Joining datasets
schoolData=schoolData.merge(frpl, on='school_name', how='left')

## Calculating high poverty
schoolData = schoolData.assign(high_poverty = lambda x: x.frpl_pct>75)

## Wide to Long
schoolData_total_population = schoolData.melt(
    id_vars='school_name', # column that uniquely identifies a row (can be multiple)
    value_vars=['na_num','aa_num','as_num','hi_num','wh_num'],
    var_name='race_ethnicity', # name for the new column created by melting
    value_name='population' # name for new column containing values from melted columns
)

# Visualization

## Race/Ethnicity per District

fig = px.pie(schoolData_total_population, values='population', names='race_ethnicity', title='Population per Race/Ethnicity')
st.plotly_chart(fig)

schoolData_total_population
frpl

