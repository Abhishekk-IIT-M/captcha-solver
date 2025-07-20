from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
import re

app = FastAPI()

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(image)

    match = re.search(r"(\d{8})\s*[*x×]\s*(\d{8})", text)
    if not match:
        return JSONResponse(status_code=400, content={"error": "Expression not found"})

    a, b = match.groups()
    result = int(a) * int(b)

    return {"answer": result, "email": "23ds3000150@ds.study.iitm.ac.in"}
