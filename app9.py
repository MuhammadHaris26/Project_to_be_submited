import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Simple data Dashboard")
uploaded_file = st.file_uploader("Choose a CSV file." , type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Flter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_vlaues = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_vlaues)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x-axis column," , columns)
    y_column = st.selectbox("select y-axis column," , columns)
