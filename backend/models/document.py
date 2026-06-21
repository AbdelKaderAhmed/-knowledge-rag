from pydantic import BaseModel
from datetime import datetime

class DocumentMetadata(BaseModel):
    filename: str
    upload_date: datetime = datetime.now()
    file_size: int
    content_type: str