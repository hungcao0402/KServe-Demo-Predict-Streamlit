import streamlit as st
import time
import base64
import requests
import io
from PIL import Image
import os

st.set_page_config(page_title="Ancestry PCA")

st.markdown("# Ancestry")
st.sidebar.header("Ancestry")
st.write(
    """Kiểm tra nguồn gốc quần thể (%) của một hoặc nhiều mẫu đã có trong dữ liệu
1000 Hệ gen thế giới (1KGP). Ngoài ra có thể chọn trực quan hóa các quần thể người
trên thế giới để đánh giá sự khác biệt giữa các quần thể hoặc siêu quần thể!"""
)

status_text = st.sidebar.empty()


def ancestry(population, superpopulation, user, endpoint, host, token):
    payload = {
        "instances": [
            {
                "population": population,
                "superpopulation": superpopulation,
                "user": user
            }
        ]
    }
    
    headers = {
        "Host": host,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        ancestry_result = response.json()['predictions']['ancestry']

        image_buffer = io.BytesIO(base64.b64decode(response.json()['predictions']['b64']))
        im = Image.open(image_buffer)
        im = im.convert("RGB")

        return im, ancestry_result
    else:
        return f"Error: Failed to convert audio to text ({response.status_code})"


TOKEN = os.environ.get("TOKEN")
SERVICE_HOSTNAME = os.environ.get("SERVICE_HOSTNAME_Ancestry")
ENDPOINT = os.environ.get("ENDPOINT") + '/v1/models/AncestryPCA:predict'

population = st.text_input('Population:', '')
superpopulation = st.text_input('Superpopulation:', 'EUR EAS AFR SAS AMR')
user = st.text_input('User:', 'HG01595 HG01607 HG03702 HG03078')

if st.button('Submit'):
    img, ancestry_result = ancestry(population, superpopulation, user, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
    
    if ancestry_result:
        for item in ancestry_result:
            st.write(item)

    st.image(img, use_column_width=True)


