import streamlit as st
import requests 
from io import BytesIO

from PIL import Image

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la muse": "la_muse",
    "mosaic": "mosaic",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}

st.write("Test App")

file = st.file_uploader("Upload an image", type=['png', 'jpg'])
style = st.selectbox("Select style", [i for i in STYLES.keys()])

