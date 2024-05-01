import streamlit as st
import os

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Demo Apps! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Nhập các endpoint và token để inference.
"""
)


if "SERVICE_HOSTNAME_HeartDisease" in os.environ:
    ENDPOINT = st.text_input('ENDPOINT Kubeflow:', os.environ["ENDPOINT"])
    SERVICE_HOSTNAME_Speech2Text = st.text_input('SERVICE_HOSTNAME_Speech2Text:', os.environ["SERVICE_HOSTNAME_Speech2Text"])
    SERVICE_HOSTNAME_EEG = st.text_input('SERVICE_HOSTNAME_EEG::',  os.environ["SERVICE_HOSTNAME_EEG"])
    SERVICE_HOSTNAME_Ancestry = st.text_input('SERVICE_HOSTNAME_Ancestry:', os.environ["SERVICE_HOSTNAME_Ancestry"])
    SERVICE_HOSTNAME_SkinCancer = st.text_input('SERVICE_HOSTNAME_SkinCancer:', os.environ["SERVICE_HOSTNAME_SkinCancer"])
    SERVICE_HOSTNAME_HeartDisease = st.text_input('SERVICE_HOSTNAME_HeartDisease:', os.environ["SERVICE_HOSTNAME_HeartDisease"])
    TOKEN = st.text_input('TOKEN:', os.environ["TOKEN"])
else:
    ENDPOINT = st.text_input('ENDPOINT Kubeflow:', 'http://103.22.218.60:33535')
    SERVICE_HOSTNAME_Speech2Text = st.text_input('SERVICE_HOSTNAME_Speech2Text:','speech2text-2024-05-01--07-11-28.kubeflow-user-example-com.example.com')
    SERVICE_HOSTNAME_EEG = st.text_input('SERVICE_HOSTNAME_EEG:','kserve-eeg.kubeflow-user-example-com.example.com')
    SERVICE_HOSTNAME_Ancestry = st.text_input('SERVICE_HOSTNAME_Ancestry:', 'ancestry-2024-05-01--07-13-27.kubeflow-user-example-com.example.com')
    SERVICE_HOSTNAME_SkinCancer = st.text_input('SERVICE_HOSTNAME_SkinCancer:', 'skin-cancer.kubeflow-user-example-com.example.com')
    SERVICE_HOSTNAME_HeartDisease = st.text_input('SERVICE_HOSTNAME_HeartDisease:', 'heart-disease.kubeflow-user-example-com.example.com')
    TOKEN = st.text_input('TOKEN:', 'eyJhbGciOiJSUzI1NiIsImtpZCI6InQxR2JxYk56SGJNVklqT1ctSV91b3Jxdy1iSFRidGFYSzNxcklKS0NyeEEifQ.eyJhdWQiOlsiaXN0aW8taW5ncmVzc2dhdGV3YXkuaXN0aW8tc3lzdGVtLnN2Yy5jbHVzdGVyLmxvY2FsIl0sImV4cCI6MTcxNTg0NTQ3NywiaWF0IjoxNzE0MTE3NDc3LCJpc3MiOiJodHRwczovL2t1YmVybmV0ZXMuZGVmYXVsdC5zdmMuY2x1c3Rlci5sb2NhbCIsImt1YmVybmV0ZXMuaW8iOnsibmFtZXNwYWNlIjoia3ViZWZsb3ctdXNlci1leGFtcGxlLWNvbSIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJkZWZhdWx0LWVkaXRvciIsInVpZCI6ImI2Yjc1MTI3LWMxY2UtNGJkYi1hMWU0LTZmZTgyYzFjNDdmZCJ9fSwibmJmIjoxNzE0MTE3NDc3LCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZWZsb3ctdXNlci1leGFtcGxlLWNvbTpkZWZhdWx0LWVkaXRvciJ9.inpWWzk6Y1HEBoMMAMBzXX660miGYjK1JE_R-1tO3svu41jXfiXP5ZunBdj_whxT8bHD02FDv5rdelIUF-v9muVDI1SFR3cMaWA8udrN5jmxI8RnU2elqZVRj9OlJB0eHxg_riHKg9C0ix70BtZojxd_N85a_-3mhA4zdkOd6Uc0Z1Px_bdVFLQsSNThtk02zsgjhD0yhejXPh0g2wKPCJkFDuw8Cl_Djf1ljAdSqj6cOE-dFw3tUJbHTMUsGIHnm41PKMAjBUltMa9wvnfOfB7-S88ftsc_9BinYW1Q0ut7B34a088XshjMR1ua7mN1POBq6prerdoeth6UrqB0EA')


if st.button('Run'):
    os.environ["TOKEN"] = TOKEN
    os.environ["ENDPOINT"] = ENDPOINT
    os.environ["SERVICE_HOSTNAME_Speech2Text"] = SERVICE_HOSTNAME_Speech2Text
    os.environ["SERVICE_HOSTNAME_EEG"] = SERVICE_HOSTNAME_EEG
    os.environ["SERVICE_HOSTNAME_Ancestry"] = SERVICE_HOSTNAME_Ancestry
    os.environ["SERVICE_HOSTNAME_HeartDisease"] = SERVICE_HOSTNAME_HeartDisease
    os.environ["SERVICE_HOSTNAME_SkinCancer"] = SERVICE_HOSTNAME_SkinCancer
