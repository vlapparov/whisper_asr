import whisper
from fastapi import FastAPI, UploadFile, File

from app.src.conf import UPLOAD_DIRECTORY
from app.src.utils.general import create_folder, remove_file
from app.src.utils.structure import OutputSchema

description = """
The API for automatic speech recognition (ASR). 
"""

tags_metadata = [
    {
        "name": "Health check",
        "description": "A simple health check",
    },
    {
        "name": "Automatic speech recognition",
        "description": "Perform automatic speech recognition",
    },
]

app = FastAPI(
    title="ASR API",
    version="v2",
    description=description,
    openapi_tags=tags_metadata,
)


@app.on_event("startup")
def load_pipe():
    global asr_model
    print("Loading ASR model...")
    asr_model = whisper.load_model("base")
    print("Successfully loaded!")

    # Directory to save uploaded audio files
    create_folder(UPLOAD_DIRECTORY)


@app.get("/", status_code=200, response_model=dict, tags=["Health check"])
async def home():
    return {"message": "Hello World"}


@app.post(
    "/recognize",
    status_code=200,
    response_model=OutputSchema,
    tags=["ASR"],
)
async def recognize_text(file: UploadFile = File(...)) -> OutputSchema:
    # Save the uploaded audio file
    file_location = f"{UPLOAD_DIRECTORY}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    # Perform ASR
    response = asr_model.transcribe(file_location)
    # Remove processed file
    remove_file(file_location)
    output = {"text": response["text"]}
    return OutputSchema(**output)
