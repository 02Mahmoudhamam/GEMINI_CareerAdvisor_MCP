from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import httpx
import traceback

app = FastAPI()

TEXT_AGENT_URL = "http://127.0.0.1:8002/analyze"
IMAGE_AGENT_URL = "http://127.0.0.1:8003/extract-text"


@app.post("/route")
async def route_file(file: UploadFile = File(...), interests: str = Form(...)):
    content_type = file.content_type
    try:
        if "text" in content_type or file.filename.endswith((".txt", ".pdf", ".docx")):
            files = {"file": (file.filename, await file.read(), content_type)}
            data = {"interests": interests}
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(TEXT_AGENT_URL, files=files, data=data)
            return JSONResponse(content={"agent": "text_agent", "response": response.json()})

        elif "image" in content_type:
            files = {"file": (file.filename, await file.read(), content_type)}
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(IMAGE_AGENT_URL, files=files)
            return JSONResponse(content={"agent": "image_agent", "response": response.json()})

        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type"})

    except Exception as e:
        tb = traceback.format_exc()
        print("Router Exception:", tb)  # طباعة الخطأ الكامل في اللوج
        return JSONResponse(status_code=500, content={"error": "Routing error", "details": str(e)})
