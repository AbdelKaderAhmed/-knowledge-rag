from langchain_community.document_loaders import PyPDFLoader
from backend.models.document import ProcessedDocument

class DocumentProcessor:
    @staticmethod
    def process(file_path: str) -> list[ProcessedDocument]:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        
        processed_docs = []
        for doc in docs:
            cleaned_content = doc.page_content.strip()
            processed_docs.append(ProcessedDocument(
                content=cleaned_content,
                metadata={**doc.metadata, "source": file_path}
            ))
        return processed_docs