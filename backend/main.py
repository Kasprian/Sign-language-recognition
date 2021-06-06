from typing import Optional

import numpy as np
import tensorflow as tf
import magic
import io
import sys

import uvicorn
from PIL import Image
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow import keras

app = FastAPI()

filepath = '/home/pjoter/ziwg-projekt/ml/save_at_50.h5'
model = keras.models.load_model(filepath, compile=True)
image_size = (180, 180)

SIGNS = ["1", "2", "3", "4", "5", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S",
         "T", "U", "W", "Y", "Z"]


def predict(image: Image.Image):
    image = np.asarray(image.resize((180, 180)))[..., :3]
    image = np.expand_dims(image, 0)
    predictions = model.predict(image)

    return predictions


@app.post("/recognize/")
async def upload_photo_to_recognize(file: UploadFile = File(...)):
    if file.content_type.startswith('image/') is False:
        raise HTTPException(status_code=400, detail=f'File \'{file.filename}\' is not an image.')

    try:
        # Read image contents
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        predictions = predict(image)
        # Generate prediction
        print(predictions)
        best = np.argmax(predictions)
        print(best)
        p = predictions[0][best]
        return {"First sign": SIGNS[best]}

    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
