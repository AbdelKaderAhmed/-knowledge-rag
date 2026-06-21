from fastapi import APIRouter, UploadFile, HTTPException
from backend.services.storage import StorageService
from backend.models.document import DocumentMetadata
from backend.services.processor import DocumentProcessor
from backend.services.chunker import ChunkingService
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


@router.post("/process-and-chunk/{filename}")
def process_and_chunk(filename: str):
    
    raw_docs = DocumentProcessor.process(f"data/uploads/{filename}")
    chunker = ChunkingService()
    
    all_chunks = []
    for doc in raw_docs:
        all_chunks.extend(chunker.chunk_document(doc))
        
    return {
        "status": "success",
        "total_chunks": len(all_chunks),
        "preview": [c.content[:50] for c in all_chunks[:3]]
    }