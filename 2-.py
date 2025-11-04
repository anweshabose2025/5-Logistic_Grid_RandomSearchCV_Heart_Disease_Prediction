# (D:\Udemy\Complete_DSMLDLNLP_Bootcamp\UPractice1\venv) D:\Udemy\Complete_DSMLDLNLP_Bootcamp\UPractice2\5-Logistic_Grid_RandomSearchCV>streamlit run 2-.py 
import streamlit as st
import pandas as pd
import pickle

st.title("Heart Disease Prediction")
st.text('Heyy!! If you want to predict if you are suffering from any Heart Disease or not, then here you go. You are exactly at the right place.')

with open('log_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

age = st.slider("Enter age", 0, 100)   #0
sex = st.selectbox("Select sex", ['Male', 'Female'])   #63
cp = st.slider("Enter cp", 0.0, 100.0)   #1
trestbps = st.slider("Enter trestbps", 0.0, 100.0)   #3
chol = st.slider("Enter chol", 0.0, 100.0)   #145
fbs = st.slider("Enter fbs", 0.0, 100.0)   #233
restecg = st.slider("Enter restecg", 0.0, 100.0)   #1
thalach = st.slider("Enter thalach", 0.0, 100.0)   #0
exang = st.slider("Enter exang", 0.0, 100.0)   #150
oldpeak = st.slider("Enter oldpeak", 0.0, 100.0)   #0
slope = st.slider("Enter slop", 0.0, 100.0)   #2.3
ca = st.slider("Enter ca", 0.0, 100.0)   #0
thal = st.slider("Enter thal", 0.0, 100.0)   #0

if st.button('Submit'):
    if sex=='Male':
        sex=1
    elif sex=='Female':
        sex=0

    new_df = pd.DataFrame({'age':[age], 'sex':[sex], 'cp':[cp], 'trestbps':[trestbps], 'chol':[chol], 'fbs':[fbs], 'restecg':[restecg], 
                'thalach':[thalach],'exang':[exang], 'oldpeak':[oldpeak], 'slope':[slope], 'ca':[ca], 'thal':[thal]})

    new_df = scaler.transform(new_df)
    predicted_result = model.predict(new_df)

    if predicted_result[0]==0:
        st.success("There is no Heart Problem")
    elif predicted_result[0]==1:
        st.warning("There is Heart Problem. You must do an immediate checkup.")
    else:
        st.error("There must be somthing wrong.")