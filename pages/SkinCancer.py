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

st.set_page_config(page_title="SkinCancer")

st.markdown("# Mô hình học máy trên dữ liệu hình ảnh bệnh da liễu")
st.sidebar.header("Mô hình học máy trên dữ liệu hình ảnh bệnh da liễu")
st.write(
    """Phân loại bệnh ung thư da cho ảnh chụp các loại ung thư da phổ biến"""
)

status_text = st.sidebar.empty()


def skin(upload_file, endpoint, host, token):
    x=[]
    output_shape = (128, 128)
    image = Image.open(uploaded_file).convert('RGB')


    # image = np.array(image.resize(output_shape))


    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img2 = resize(img, output_shape)  

    x.append(img2) 
    x = np.array(x)

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
        lesion_names = ['Melanocytic nevi','Melanoma','Benign keratosis-like lesions ',
                   'Basal cell carcinoma','Actinic keratoses','Vascular lesions',
                   'Dermatofibroma']

        id = np.argmax(response.json()["predictions"][0])
        result = {'predict_type_cancer': lesion_names[id],
                    'probability': response.json()["predictions"][0][id]}
        return result
    else:
        return f"Error: Failed to convert audio to text ({response.status_code})"




TOKEN = os.environ.get("TOKEN")
SERVICE_HOSTNAME = os.environ.get("SERVICE_HOSTNAME_SkinCancer")
ENDPOINT = os.environ.get("ENDPOINT") + '/v1/models/skin-cancer:predict'


uploaded_file = st.file_uploader("Upload file image", type=['jpg','png'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    if st.button('Submit'):
        # file_content = uploaded_file.read()
        result = skin(uploaded_file, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
        st.write('Result', result)
