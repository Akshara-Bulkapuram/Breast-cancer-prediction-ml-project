import streamlit as st
import joblib
import pandas as pd
import sqlite3
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

data_list = []

model_filename = os.path.join(script_directory, "mlp_model.joblib")
mlp_classifier = joblib.load(model_filename)

logo_path = os.path.join(script_directory, "NITKlogo.png")

from PIL import Image
image=Image.open(logo_path)
if os.path.exists(logo_path):
    col1,col2,col3=st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image(image,width=100)
    with col3:
        st.write(' ')   
else:
    st.warning("Image file not found. Please check the file path.")
st.header("Department of Information Technology")
st.header("National Institute of Karnataka, Surathkal")
st.markdown("-------------------------------------------------------------------------------------------------------------")
st.markdown("")

st.title("Breast Cancer Prediction using Machine Learning")
st.markdown("**By Akshara(211AI012) and Sowjanya(211AI037)**\n", unsafe_allow_html=True)
st.markdown("")

st.subheader("Please provide your details:")
# Input fields for patient information
name = st.text_input("Name")
age = st.number_input("Age")

st.subheader("Enter Tumor Features")
# Input fields for 11 features with updated names
texture_mean = st.number_input("Texture Mean")
concavity_mean = st.number_input("Concavity Mean")
concave_points_mean = st.number_input("Concave Points Mean")
area_se = st.number_input("Area SE")
symmetry_se = st.number_input("Symmetry SE")
radius_worst = st.number_input("Radius Worst")
perimeter_worst = st.number_input("Perimeter Worst")
area_worst = st.number_input("Area Worst")
smoothness_worst = st.number_input("Smoothness Worst")
concavity_worst = st.number_input("Concavity Worst")
concave_points_worst = st.number_input("Concave Points Worst")

def add_user_data(name, age, features, predicted_class):
    data_list.append({
        "Name": name,
        "Age": age,
        "Texture Mean": features[0],
        "Concavity Mean": features[1],
        "Concave Points Mean": features[2],
        "Area SE": features[3],
        "Symmetry SE": features[4],
        "Radius Worst": features[5],
        "Perimeter Worst": features[6],
        "Area Worst": features[7],
        "Smoothness Worst": features[8],
        "Concavity Worst": features[9],
        "Concave Points Worst": features[10],
        "Predicted_Class": predicted_class
    })

if st.button("Predict"):
    features = [texture_mean, concavity_mean, concave_points_mean, area_se,
                symmetry_se, radius_worst, perimeter_worst, area_worst,
                smoothness_worst, concavity_worst, concave_points_worst]

    prediction = mlp_classifier.predict([features])

    st.write(f"Predicted class: {prediction[0]}")
    if prediction[0] == 0:
        st.write("The patient is predicted to have Malignant cancer.")
    else:
        st.write("The patient is predicted to have Benign cancer.")
    st.write("Thank You")

    # Store the user data in the SQLite database
    db_filename = os.path.join(script_directory, 'user_data.db')
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    c.execute('''
        INSERT INTO user_data (name, age, texture_mean, concavity_mean, concave_points_mean,
            area_se, symmetry_se, radius_worst, perimeter_worst,
            area_worst, smoothness_worst, concavity_worst, concave_points_worst, predicted_class
        ) VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, texture_mean, concavity_mean, concave_points_mean, area_se,
          symmetry_se, radius_worst, perimeter_worst, area_worst,
          smoothness_worst, concavity_worst, concave_points_worst, prediction[0]))

    conn.commit()
    conn.close()
