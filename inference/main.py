from fastapi import FastAPI, UploadFile, File
from inference import run_prediction
from utils import get_models
from starlette.responses import StreamingResponse
from PIL import Image

import numpy as np
import io
import cv2
import os

from constants import  BASE_PATH

from starlette.middleware.cors import CORSMiddleware

MODEL_PATH = os.getenv('MODEL_PATH', 'models')
models = get_models(MODEL_PATH)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
	return {"Served From": str(os.getpid())}

@app.post('/styles/{style}/')
async def transfer_style(style: str, file:UploadFile = File(...)):
	contents = await file.read()
	nparr = np.fromstring(contents, np.uint8)
	input_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

	model = cv2.dnn.readNetFromTorch(f'{BASE_PATH}/{style}.t7')
	cv2img, new_shape = run_prediction(model, input_img)
	res, im_png = cv2.imencode(".png", cv2img)

	return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")