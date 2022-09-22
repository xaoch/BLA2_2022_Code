import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img_file_buffer = st.camera_input("Take a picture")

face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    image = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    image.flags.writeable = False
    results = face_detection.process(image)
    image.flags.writeable = True
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    st.write(results.detections)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
    # Flip the image horizontally for a selfie-view display.

st.image(image)