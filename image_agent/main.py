from fastapi import FastAPI, UploadFile, File
import easyocr
import shutil
import os

app = FastAPI()

reader = easyocr.Reader(['en'])  # Arabic optional

@app.post("/extract-text")
async def extract_text_from_image(file: UploadFile = File(...)):
    try:
        # 1. Save uploaded image temporarily
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. Run OCR
        result = reader.readtext(temp_path, detail=0)
        extracted_text = "\n".join(result)

        # 3. Clean up temp file
        os.remove(temp_path)

        # 4. Return the extracted text
        return {"extracted_text": extracted_text}

    except Exception as e:
        return {"error": str(e)}
