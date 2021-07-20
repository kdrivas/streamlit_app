import streamlit as st
import requests 
from io import BytesIO
import os
from PIL import Image

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la muse": "la_muse",
    "mosaic": "mosaic",
    "the scream": "the_scream",
    "udnie": "udnie",
}

SERVER = os.getenv('SERVER_PORT', 'inference:8080')

st.write("Test App")

file = st.file_uploader("Upload an image", type=['png', 'jpg'])
style = st.selectbox("Select style", [i for i in STYLES.keys()])

if st.button("submit") and file is not None and style is not None:
	res = requests.post(f'https://{SERVER}/styles/{STYLES[style]}', files={'file': file}, )
	print(f'https://{SERVER}/styles/{STYLES[style]}')
	print(res.content)
	img = BytesIO(res.content)
	new_image = Image.open(img)
	st.image(new_image, width=500)