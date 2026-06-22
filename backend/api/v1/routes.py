from fastapi import APIRouter, UploadFile, HTTPException
from backend.services.storage import StorageService
from backend.services.processor import DocumentProcessor
from backend.services.chunker import ChunkingService
from backend.services.embedding import EmbeddingService
from backend.services.vector_store import VectorStoreService

router = APIRouter()

# Initialize services as singletons for efficiency
embedder = EmbeddingService()
vector_store = VectorStoreService()

@router.post("/upload")
async def upload_document(file: UploadFile):
    """Uploads a PDF file to the local storage."""
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    file_path = StorageService.save_file(file)
    return {"message": "Success", "filename": file.filename}

@router.post("/ingest/{filename}")
def ingest_document(filename: str):
    """Full pipeline: Process, Chunk, Embed, and Index into ChromaDB."""
    file_path = f"data/uploads/{filename}"
    
    try:
        # 1. Extract text from PDF
        raw_docs = DocumentProcessor.process(file_path)
        
        # 2. Split text into manageable chunks
        chunker = ChunkingService()
        all_chunks = []
        for doc in raw_docs:
            all_chunks.extend(chunker.chunk_document(doc))
            
        # 3. Generate vector embeddings
        vectors = embedder.generate_embeddings(all_chunks)
        
        # 4. Store vectors in ChromaDB
        vector_store.add_documents(all_chunks, vectors)
        
        return {
            "status": "success",
            "total_chunks": len(all_chunks),
            "total_vectors": len(vectors),
            "preview": [c.content[:50] for c in all_chunks[:3]]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))