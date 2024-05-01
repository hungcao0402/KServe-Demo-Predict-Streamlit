import streamlit as st
import time
import base64
import requests
import io
import os
from PIL import Image
import numpy as np
from cv2 import imread, resize
import cv2

st.set_page_config(page_title="HeartDisease")

st.markdown("# Mô hình học máy trên dữ liệu bệnh tim")
st.sidebar.header("Mô hình học máy trên dữ liệu bệnh tim")
st.write(
    """Dự đoán một người có bị bệnh tim hay không dựa vào các thông tin liên quan
đến bệnh tim của bệnh nhân"""
)

status_text = st.sidebar.empty()


def heartpredict(x: np.array, endpoint: str, host: str, token: str):
    inference_input = {
      'instances': x.tolist()
    }

    headers = {
        "Host": host,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, headers=headers, json=inference_input)

    if response.status_code == 200:        
        return response.json()['predictions'][0]
    else:
        return f"Error: Failed to convert audio to text ({response.status_code})"


TOKEN = os.environ.get("TOKEN")
SERVICE_HOSTNAME = os.environ.get("SERVICE_HOSTNAME_HeartDisease")
ENDPOINT = os.environ.get("ENDPOINT") + '/v1/models/heart-disease:predict'

age = st.number_input("Age", min_value=18, max_value=100, step=1, value=50)
sex = st.radio("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Probable or definite left ventricular hypertrophy"])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, step=1, value=120)
exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=6.2, step=0.1, value=0.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.number_input("Number of Major Vessels Colored by Flouroscopy", min_value=0, max_value=4, step=1, value=0)
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# Preprocess inputs
sex = 1 if sex == "Male" else 0
exang = 1 if exang == "Yes" else 0
cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
restecg = ["Normal", "ST-T wave abnormality", "Probable or definite left ventricular hypertrophy"].index(restecg)
slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal) + 1

if st.button('Submit'):
    input = np.array([[age, sex, cp, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    result = heartpredict(input, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
    result = "Bị bệnh tim" if result == 1 else "Không bị bệnh tim"
    st.write('**Kết quả:**', result)
