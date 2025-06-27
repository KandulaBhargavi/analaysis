# app.py or streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis App", layout="wide")

st.title("📊 Simple Data Analysis App")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🗃️ Dataset Preview")
    st.dataframe(df.head())

    # Dataset shape
    st.markdown(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    # Select analysis options
    st.subheader("📈 Data Description")
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())

    if st.checkbox("Show Column Info"):
        buffer = []
        df.info(buf=buffer)
        s = '\n'.join(buffer)
        st.text(s)

    # Null values
    st.subheader("🚨 Missing Values")
    if df.isnull().sum().sum() == 0:
        st.success("No missing values found.")
    else:
        st.write(df.isnull().sum())

    # Correlation heatmap
    st.subheader("📌 Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns to plot.")

    # Boxplot
    st.subheader("📦 Boxplot Analysis")
    col = st.selectbox("Select a column", numeric_df.columns)
    fig2, ax2 = plt.subplots()
    sns.boxplot(x=df[col], ax=ax2)
    st.pyplot(fig2)

    # Histogram
    st.subheader("📊 Histogram")
    col2 = st.selectbox("Select column for histogram", numeric_df.columns, key='hist')
    bins = st.slider("Number of bins", 5, 100, 20)
    fig3, ax3 = plt.subplots()
    ax3.hist(df[col2], bins=bins, color='skyblue', edgecolor='black')
    st.pyplot(fig3)

else:
    st.info("Upload a CSV file to begin analysis.")

