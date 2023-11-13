# Breast-cancer-prediction-ml-project

# Breast Cancer Feature Selection and Classification

This project aims to perform feature selection and classification on breast cancer data. Breast cancer is a significant health concern, and machine learning techniques can help in early detection and diagnosis.

# Table of Contents

Introduction
Data Set
Exploratory Data Analysis 
Feature Selection
Classification
Dependencies
Results

# Introduction
Breast cancer is one of the most common types of cancer among women worldwide. Early detection and accurate diagnosis are crucial for effective treatment. In this project, we use machine learning techniques to:

1.Select relevant features from breast cancer data.
2.Train a classification model to predict whether a breast tumor is malignant or benign.

# Dataset 

The dataset from Wisconsin Breast cancer 
Dataset (WBCD)with 32 attributes The dataset contains 569 samples of malignant and benign tumor cells.

The features include various measurements such as radius, texture, smoothness, and more.

# EDA
We have performed different data visualizations like scatter plot, blox plot , histograms and correlation heatmap for better data understanding.

# Feature Selection
We have performed
1.ANOVA feature selection
2.Kendall's tau Feature selection
3.Correlation based
4.Recursive elimation based feature selection method
5.PCA+CFS feature selection methods

# Classification

We use different classification algorithms to build predictive models for breast cancer diagnosis.
The ML models we used are

Multi Layer Perceptron(MLP)
Support Vector Machine (SVM)
Linear Regression
Random Forest

# Dependencies
Python 3.x
Scikit-learn
Pandas
NumPy
Matplotlib
Seaborn
Streamlit

# Results
We have found out that Multi layer perceptron model gives best accuracy in terms of accuracy and prediction, followed by SVM classifier model. linear regression was comparitively worse among the four models. Random Forest gave an average performance.




