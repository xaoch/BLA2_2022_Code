import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
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
schoolData["wh_pct"]=convertToNumber(schoolData["wh_pct"])


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


# Controls
st.sidebar.title("Visualizations")
visualization = st.sidebar.radio(
    "What visualization do you want to see?",
    options=['Race/Ethnicity in the District', 'Percentage Poverty', "Race/Ethnicity in High Poverty Schools","Histogram of Populations"])


size= st.sidebar.slider(
    'Only considers schools with this size:',
    min_value=int(schoolData["tot"].min()),
    max_value=int(schoolData["tot"].max()),
    value=(int(schoolData["tot"].min()), int(schoolData["tot"].max())))

mask=schoolData["tot"].between(size[0],size[1])
schoolData=schoolData[mask]

schools= st.sidebar.multiselect(
    'What schools do you want to include',
    options=schoolData["school_name"].unique(),
    default=schoolData["school_name"].unique())

mask=schoolData["school_name"].isin(schools)
schoolData=schoolData[mask]

schoolData_population = schoolData.melt(
    id_vars=['school_name', 'high_poverty'], # column that uniquely identifies a row (can be multiple)
    value_vars=['na_num','aa_num','as_num','hi_num','wh_num'],
    var_name='race_ethnicity', # name for the new column created by melting
    value_name='population' # name for new column containing values from melted columns
)

schoolData_population["race_ethnicity"]= schoolData_population["race_ethnicity"].replace("na_num","Native American")
schoolData_population["race_ethnicity"]= schoolData_population["race_ethnicity"].replace("aa_num","African American")
schoolData_population["race_ethnicity"]= schoolData_population["race_ethnicity"].replace("as_num","Asian American")
schoolData_population["race_ethnicity"]= schoolData_population["race_ethnicity"].replace("hi_num","Hispanic")
schoolData_population["race_ethnicity"]= schoolData_population["race_ethnicity"].replace("wh_num","White")

schoolData_population_totals = schoolData_population.groupby("race_ethnicity").sum()

schoolData_percentages = schoolData.melt(
    id_vars=['school_name', 'high_poverty'], # column that uniquely identifies a row (can be multiple)
    value_vars=['na_pct','aa_pct','as_pct','hi_pct','wh_pct'],
    var_name='race_ethnicity', # name for the new column created by melting
    value_name='percentage' # name for new column containing values from melted columns
)

## Race/Ethnicity per District
if (visualization=="Race/Ethnicity in the District"):
    col1, col2= st.columns(2)

    with col1:
        fig = px.pie(schoolData_population, values='population', names='race_ethnicity',
                     title='Percentages of Population per Race/Ethnicity')
        st.plotly_chart(fig)

    with col2:
        fig2 = px.bar(schoolData_population_totals, x=schoolData_population_totals.index, y='population',
                      title="Population per Race/Ethnicity")
        st.plotly_chart(fig2)

## Percentage Poverty
if (visualization=="Percentage Poverty"):
    fig = px.pie(schoolData, names='high_poverty', title='Percentage of Schools in Poverty', hole=0.5)
    st.plotly_chart(fig)

## Population Division per Poverty Level
if (visualization=="Race/Ethnicity in High Poverty Schools"):
    fig = px.pie(schoolData_population, values='population', names='race_ethnicity', facet_col="high_poverty",
                 title='Percentages of Population per Race/Ethnicity', width=1200)
    st.plotly_chart(fig)

## Histogram of Populations
if (visualization=="Histogram of Populations"):
    mask=schoolData_percentages["race_ethnicity"]=="aa_pct"
    fig = px.histogram(schoolData_percentages[mask], x="percentage", color="high_poverty",  marginal="rug",width=800, title="African American")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)

    mask = schoolData_percentages["race_ethnicity"] == "as_pct"
    fig = px.histogram(schoolData_percentages[mask], x="percentage", color="high_poverty", marginal="rug", width=800,
                       title="Asian American")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)

    mask = schoolData_percentages["race_ethnicity"] == "na_pct"
    fig = px.histogram(schoolData_percentages[mask], x="percentage", color="high_poverty", marginal="rug", width=800,
                       title="Native American")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)

    mask = schoolData_percentages["race_ethnicity"] == "hi_pct"
    fig = px.histogram(schoolData_percentages[mask], x="percentage", color="high_poverty", marginal="rug", width=800,
                       title="Hispanics")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)

    mask = schoolData_percentages["race_ethnicity"] == "wh_pct"
    fig = px.histogram(schoolData_percentages[mask], x="percentage", color="high_poverty", marginal="rug", width=800,
                       title="White")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)


