from typing import Optional

import magic
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/recognize/")
async def upload_photo_to_recognize(picture: UploadFile = File(...)):
    """Attempts recognition of the uploaded picture.

    Returns a list of possible recognition results,
    along with confidence level.

    The picture can be in `jpg` or `png` format.
    """

    header = await picture.read(2048)
    await picture.seek(0)  # Rewind the picture back to the start
    recognised_file_type = magic.from_buffer(header)

    return {"filename": picture.filename, "type": recognised_file_type}
