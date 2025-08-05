from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from shared.utils import generate_text_gemini
import tempfile

app = FastAPI()


@app.post("/analyze")
async def analyze_text(file: UploadFile = File(...), interests: str = Form(...)):
    contents = await file.read()
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(contents)
    temp.close()

    with open(temp.name, "r", encoding="utf-8", errors="ignore") as f:
        cv_text = f.read()

    prompt = f"""
    You are an AI career assistant. Analyze the following CV and user interests, then extract skills and suggest suitable career paths.

    --- CV CONTENT ---
    {cv_text}

    --- USER INTERESTS ---
    {interests}

    Provide a JSON response with:
    - extracted_skills
    - suggested_fields
    - summary_analysis
    """

    result = generate_text_gemini(prompt)

    return JSONResponse(content={
        "source": "text",
        "analysis": result
    })
