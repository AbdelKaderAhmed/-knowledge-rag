from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class DocumentMetadata(BaseModel):
    filename: str
    upload_date: datetime = datetime.now()
    file_size: int
    content_type: str

class ProcessedDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]

