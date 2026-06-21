from fastapi import APIRouter, UploadFile, HTTPException
from backend.services.storage import StorageService
from backend.models.document import DocumentMetadata
from backend.services.processor import DocumentProcessor

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    file_path = StorageService.save_file(file)
    return {"message": "Success", "path": file_path}

@router.post("/process/{filename}")
def process_file(filename: str):
    file_path = f"data/uploads/{filename}"
    docs = DocumentProcessor.process(file_path)
    return {"status": "processed", "chunks": len(docs)}