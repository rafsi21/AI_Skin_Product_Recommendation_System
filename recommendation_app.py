import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("AI_Skin_Product..csv")
st.write("Available Skin Types:")
st.write(df["Skin_Type"].unique())

st.write("Available Concerns:")
st.write(df["Concern"].unique())

st.write("Available Product Combinations:")
st.write(df.groupby(["Skin_Type", "Concern"]).size())

# App title
st.title("AI Skin Product Recommendation System")

st.write("Find skincare products suitable for your skin.")

# Skin type selection
skin_type = st.selectbox(
    "Select your Skin Type",
    df["Skin_Type"].dropna().unique()
)

# Skin concern selection
concern = st.selectbox(
    "Select your Skin Concern",
    df["Concern"].dropna().unique()
)

# Recommendation button
if st.button("Recommend Products"):
    result = df[
        (df["Skin_Type"] == skin_type) &
        (df["Concern"] == concern)
    ]

    st.subheader("Recommended Products")

    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("No matching products found.")

