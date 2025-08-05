from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import httpx
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

ROUTER_URL = "http://127.0.0.1:8001/route"


@app.post("/process")
async def process_file(file: UploadFile = File(...), interests: str = Form(...)):
    try:
        file_bytes = await file.read()
        files = {"file": (file.filename, file_bytes, file.content_type)}
        data = {"interests": interests}

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(ROUTER_URL, files=files, data=data)

            logging.info(f"Router Response Status: {response.status_code}")
            logging.info(f"Router Response Content: {response.text}")

            try:
                return JSONResponse(content=response.json())
            except Exception:
                return JSONResponse(
                    content={
                        "agent": "router_agent",
                        "raw_response": response.text
                    }
                )


    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": "Orchestrator error", "details": str(e)}
        )



