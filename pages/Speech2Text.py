import streamlit as st
import time
import base64
import requests
from st_audiorec import st_audiorec
import os

st.set_page_config(page_title="Speech to Text")

st.markdown("# Speech to Text")
st.sidebar.header("Speech to Text")
st.write(
    """Tự động nhận dạng tiếng nói từ Audio sang văn bản!"""
)

status_text = st.sidebar.empty()

def speech_to_text(wav_audio_data, endpoint, host, token):
    audio_content = wav_audio_data

    base64_data = base64.b64encode(audio_content).decode('utf-8')

    inference_input = {
    'instances': [{'audio_content': base64_data}]
    }

    headers = {
        "Host": host,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(endpoint, headers=headers, json=inference_input)

    if response.status_code == 200:
        return response.json()['predictions']
    else:
        return f"Error: Failed to convert audio to text ({response.status_code})"


TOKEN = os.environ.get("TOKEN")
SERVICE_HOSTNAME = os.environ.get("SERVICE_HOSTNAME_Speech2Text")
ENDPOINT = os.environ.get("ENDPOINT") + '/v1/models/speech2text:predict'

option = st.sidebar.selectbox(
    'Chọn dịch vụ:',
    ('Chuyển file âm thanh thành văn bản', 'Ghi âm và chuyển thành văn bản')
)

if option == 'Ghi âm và chuyển thành văn bản':
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        if st.button('Run'):
            result = speech_to_text(wav_audio_data, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
            st.write('Result:', result)
else:
    uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        if st.button('Submit'):
            wav_audio_data = uploaded_file.read()
            result = speech_to_text(wav_audio_data, ENDPOINT, SERVICE_HOSTNAME, TOKEN)
            st.write('Result:', result)


