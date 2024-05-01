import streamlit as st
import time
import base64
import requests
import io
import pandas as pd 
import os

st.set_page_config(page_title="EEG")

st.markdown("# Mô hình học máy trên dữ liệu điện não đồ EEG")
st.sidebar.header("Mô hình học máy trên dữ liệu điện não đồ EEG")
st.write(
    """Khi con người suy nghĩ, chúng ta tạo ra sóng não, sóng não có thể được ánh
xạ tới ý định thực tế. Dự án này, chúng tôi sử dụng dữ liệu sóng não của mọi người với
mục tiêu đánh vần một từ bằng cách chỉ chú ý đến kích thích thị giác. Mục tiêu của dự
án này là phát hiện các lỗi trong quá trình làm bài chính tả dựa trên sóng não của đối
tượng."""
)

status_text = st.sidebar.empty()


def eeg(file_content, filename, endpoint, host, token):
    base64_data = base64.b64encode(file_content).decode('utf-8')

    payload = {
        'instances': [{'content': base64_data,
                        'filename': filename}]
    }
    
    headers = {
        "Host": host,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Failed to convert audio to text ({response.status_code})"

TOKEN = os.environ.get("TOKEN")
SERVICE_HOSTNAME = os.environ.get("SERVICE_HOSTNAME_EEG")
ENDPOINT = os.environ.get("ENDPOINT") + '/v1/models/eeg_model:predict'

uploaded_file = st.file_uploader("Upload file csv", type=['csv'])

if uploaded_file is not None:
    if st.button('Submit'):
        file_content = uploaded_file.read()
        result = eeg(file_content, uploaded_file.name, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
        df = pd.DataFrame(result['predictions'])
        st.write('Result', df)
