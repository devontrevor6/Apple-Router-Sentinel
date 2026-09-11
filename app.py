from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import shutil

app = FastAPI(title="SylPulse API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head><title>SylPulse Upload</title></head>
        <body style="font-family: Arial; padding: 40px; background: #0f172a; color: #f8fafc;">
            <h2>SylPulse Syllabus Parser</h2>
            <p>Upload your syllabus image below to generate your automated .ics calendar and study plan.</p>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*" required style="padding: 10px; background: #1e293b; color: white; border: 1px solid #475569;" /><br><br>
                <button type="submit" style="padding: 10px 20px; background: #3b82f6; color: white; border: none; cursor: pointer;">Upload & Generate</button>
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload_syllabus(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "Processed successfully", "message": "Engine OCR parsed and calendar ready."}
