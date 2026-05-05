import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))


st.title("🎓 Student Placement Prediction")

# Inputs
cgpa = st.number_input("CGPA", 0.0, 10.0)
internships = st.number_input("Internships", 0, 5)
projects = st.number_input("Projects", 0, 10)
coding = st.slider("Coding Skills", 1, 10)
communication = st.slider("Communication Skills", 1, 10)
aptitude = st.number_input("Aptitude Score", 0, 100)
soft = st.slider("Soft Skills", 1, 10)
certifications = st.number_input("Certifications", 0, 5)
backlogs = st.number_input("Backlogs", 0, 10)

if st.button("Predict"):
    input_data = np.array([[cgpa, internships, projects, coding, communication,
                            aptitude, soft, certifications, backlogs]])

    

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student will be Placed")
    else:
        st.error("❌ Student will NOT be Placed")
