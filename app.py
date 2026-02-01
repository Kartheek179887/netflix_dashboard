import streamlit as st
import pandas as pd

st.title("Netflix Data Analysis Dashboard")

# Load data
df = pd.read_csv("netflix_titles.csv")

# Convert date
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

st.subheader("Dataset Preview")
st.dataframe(df.head())
st.sidebar.header("Filters")

content_type = st.sidebar.selectbox(
    "Select Content Type",
    options=["All", "Movie", "TV Show"]
)

if content_type != "All":
    df = df[df["type"] == content_type]
st.subheader("Movies vs TV Shows")

type_counts = df["type"].value_counts()
st.bar_chart(type_counts)
st.subheader("Titles Added Per Year")

year_counts = df["year_added"].value_counts().sort_index()
st.line_chart(year_counts)
st.subheader("Top 10 Countries by Content")

countries = df["country"].dropna().str.split(", ").explode()
top_countries = countries.value_counts().head(10)

st.bar_chart(top_countries)





