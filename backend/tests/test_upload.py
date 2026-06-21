from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_upload_pdf():
    
    with open("test.pdf", "wb") as f:
        f.write(b"%PDF-1.4 test content")
    
    with open("test.pdf", "rb") as f:
        response = client.post("/api/v1/upload", files={"file": ("test.pdf", f, "application/pdf")})
    
    assert response.status_code == 200
    assert "path" in response.json()