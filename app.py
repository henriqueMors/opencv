import cv2
import streamlit as st

def principal():
    st.title("Open Data App")
    st.subheader("Esse aplicativo permite integrar processamento de imagens com OpenCV")
    st.text("Streamlit com OpenCV para processamento de imagens em tempo real.")

    img = cv2.imread("images/vicecity.jpg")