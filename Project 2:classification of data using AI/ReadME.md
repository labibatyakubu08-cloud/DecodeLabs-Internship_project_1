CLASSIFICATION OF DATA USING AI
Project 2 artificial intelligence internship

Developed by:
YAKUBU LABIBAT

Student Placement Prediction Model
​This repository contains a machine learning pipeline designed to predict student placement status using historical data. 
The project implements data preprocessing, feature standardization, a Logistic Regression classification model, and comprehensive evaluation metrics.

​🚀 Features
​1.Data Preprocessing: Robust handling of features, including automated missing value checks and target variable isolation (placement_status).
​2.Feature Scaling: Implements StandardScaler to normalize features for stable and optimized linear model convergence.
​3.Classification Pipeline: Utilizes an sklearn Logistic Regression model for efficient binary classification.
​4.Performance Evaluation: Generates a detailed classification report and visualizes model accuracy using a Seaborn-annotated confusion matrix heatmap.

​🛠️ Tech Stack & Dependencies
​The implementation relies on core Python data science and machine learning libraries:
​ ~ Data Manipulation: numpy, pandas
​ ~ Machine Learning: scikit-learn
​ ~ Data Visualization: matplotlib, seaborn

​📊 Model Pipeline Summary:

​-- Exploratory Assessment: Loads the dataset, inspects the initial structure (.head()), checks for missing data (.isnull().sum()), and reviews summary statistics (.describe()).
​-- Data Splitting: Isolates the target variable placement_status from predictor variables and partitions them into training and test matrices.
​-- Feature Standardization: Fits a scaler to the training partition and transforms both the training and testing features uniformly.
​-- Training & Inference: Trains a LogisticRegression classifier on the scaled training partition and generates predictions on the unseen test set.
​-- Evaluation: Outputs a precision/recall classification report and renders an intuitive, labeled confusion matrix plot.
​
📊 Results and Evaluation
​The model's performance is evaluated using a standard classification report (tracking precision, recall, and F1-score) 
alongside a visualized confusion matrix to analyze true vs. false predictions.
​1. Performance Metrics
​Below is the summary of the model's predictive performance on the test dataset:









Confusion Matrix Matrix Visualization
​The confusion matrix heatmap (generated via lines 35–40 using Seaborn) 
provides a visual breakdown of correct and incorrect classifications:






 ~ True Negatives (Top-Left): Students correctly predicted as not placed.
​ ~ False Positives (Top-Right): Students incorrectly predicted as placed.
​ ~ False Negatives (Bottom-Left): Students incorrectly predicted as not placed.
​ ~ True Positives (Bottom-Right): Students correctly predicted as placed.
