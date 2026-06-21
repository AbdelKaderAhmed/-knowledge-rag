from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from backend.models.document import ProcessedDocument

class ChunkingService:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def chunk_document(self, doc: ProcessedDocument) -> List[ProcessedDocument]:
        texts = self.splitter.split_text(doc.content)
        chunks = []
        for i, text in enumerate(texts):
            
            metadata = {**doc.metadata, "chunk_index": i, "total_chunks": len(texts)}
            chunks.append(ProcessedDocument(content=text, metadata=metadata))
        return chunks