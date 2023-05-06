import pandas as pd
import streamlit as st
import base64

def process_csv(file):
    df = pd.read_csv(file, header=None)
    df.iloc[:, -1] = 1

    
    return df.to_csv(sep=',', index=False, header=False,lineterminator=",\n")

def download_link(content, filename, text):
    content = content.encode('utf-8')
    b64 = base64.b64encode(content).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'
    return href

st.title('CSV File Converter')

uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        converted_txt = process_csv(uploaded_file)
        st.write("File successfully converted.")
        st.markdown(download_link(converted_txt, 'converted_file.txt', 'Download Converted File'), unsafe_allow_html=True)
    except Exception as e:
        st.write("Error processing the file. Please make sure it is a valid CSV file.")
        st.write(str(e))
