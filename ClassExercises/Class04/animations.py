import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://assets4.lottiefiles.com/packages/lf20_a2chheio.json"

lottie_animation = load_lottieurl(lottie_url)

st_lottie(lottie_animation, key="animation", height=100)
