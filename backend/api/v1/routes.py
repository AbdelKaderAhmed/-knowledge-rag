from fastapi import APIRouter, UploadFile, HTTPException
from backend.services.storage import StorageService
from backend.models.document import DocumentMetadata

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    file_path = StorageService.save_file(file)
    return {"message": "Success", "path": file_path}