import streamlit as st
import joblib

# Load model
model = joblib.load("kmeans_model.pkl")

st.title("Mall Customer Segmentation")

income = st.number_input("Annual Income (k$)", 0, 200, 50)
score = st.number_input("Spending Score", 0, 100, 50)

if st.button("Predict"):
    data = [[income, score]]
    cluster = model.predict(data)
    st.success(f"Cluster: {cluster[0]}")