from typing import Optional

import magic
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


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
