import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
