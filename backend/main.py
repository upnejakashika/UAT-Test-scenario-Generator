
Kashika Upneja <upnejakashika@gmail.com>
5:24 PM (23 minutes ago)
to me

from fastapi import FastAPI, UploadFile, File
from backend.parser import extract_text_from_pdf
from backend.llm import generate_test_scenarios
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "backend/data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload-srs/")
async def upload_srs(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Generate scenarios
    scenarios = generate_test_scenarios(extracted_text)

    return {
        "message": "File processed successfully",
        "scenarios": scenarios
    }
