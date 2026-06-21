from fastapi import FastAPI
from backend.api.v1.routes import router

app = FastAPI(title="KnowledgeMind RAG API")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "System is healthy"}

app.include_router(router, prefix="/api/v1")