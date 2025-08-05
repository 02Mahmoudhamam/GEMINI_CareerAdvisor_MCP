from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from shared.utils import generate_text_gemini

app = FastAPI()

@app.post("/advice")
async def generate_advice(request: Request):
    body = await request.json()
    agent_source = body.get("source", "unknown")
    content = body.get("analysis", "")

    prompt = f"""
    Based on the following {agent_source} analysis, provide a final career recommendation report. 
    Be concise and categorize the output into:
    - Top Suggested Fields
    - Recommended Skills to Learn
    - Optional Certifications
    - Final Notes

    --- ANALYSIS CONTENT ---
    {content}
    """

    final_report = generate_text_gemini(prompt)

    return JSONResponse(content={
        "final_report": final_report
    })
