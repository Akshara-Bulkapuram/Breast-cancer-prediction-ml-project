import streamlit as st
import joblib
import pandas as pd
import sqlite3
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

data_list = []

model_filename = os.path.join(script_directory, "mlp_model.joblib")
mlp_classifier = joblib.load(model_filename)
st.title("Breast Cancer Prediction using Machine learning")

# Create input fields for 11 features
radius_mean = st.number_input("radius_mean")
perimeter_mean= st.number_input("perimeter_mean")
area_mean = st.number_input("area_mean")
concavity_mean = st.number_input("concavity_mean")
concave_points_mean = st.number_input("concave points_mean")
area_se = st.number_input("area_se")
radius_worst = st.number_input("radius_worst")
perimeter_worst = st.number_input("perimeter_worst")
area_worst = st.number_input("area_worst")
concavity_worst = st.number_input("concavity_worst")
concave_points_worst = st.number_input("concave points_worst")

def add_user_data(features, predicted_class):
    data_list.append({
        "Feature1 (radius_mean)": features[0],
        "Feature2 (perimeter_mean)": features[1],
        "Feature3 (area_mean)": features[2],
        "Feature4 (concavity_mean)": features[3],
        "Feature5 (concave_points_mean)": features[4],
        "Feature6 (area_se)": features[5],
        "Feature7 (radius_worst)": features[6],
        "Feature8 (perimeter_worst)": features[7],
        "Feature9 (area_worst)": features[8],
        "Feature10 (concavity_worst)": features[9],
        "Feature11 (concave_points_worst)": features[10],
        "Predicted_Class": predicted_class
    })


\

if st.button("Predict"):

    features = [radius_mean, perimeter_mean, area_mean, concavity_mean,
       concave_points_mean,area_se,radius_worst, perimeter_worst,
       area_worst, concavity_worst, concave_points_worst]  # Include all 11 features

 
    prediction = mlp_classifier.predict([features])

  

    st.write(f"Predicted class: {prediction[0]}")
    if(prediction[0]==0):
        st.write(f"The patient is having Malignant cancer type")
    else:
        st.write(f"The patient is having Benign cancer type")
    st.write("Thank You")

 # Store the user data in the SQLite database
    db_filename=os.path.join(script_directory, 'user_data.db')
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    c.execute('''
        INSERT INTO user_data (
            radius_mean, perimeter_mean, area_mean, concavity_mean,
            concave_points_mean, area_se, radius_worst, perimeter_worst,
            area_worst, concavity_worst, concave_points_worst, predicted_class
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
         area_se, radius_worst, perimeter_worst, area_worst, concavity_worst,
         concave_points_worst, prediction[0]))
    conn.commit()
    conn.close()