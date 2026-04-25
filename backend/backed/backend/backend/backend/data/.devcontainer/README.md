AI Test Scenario Generator

🚀 Overview

This project is an AI-based system that:

- Accepts SRS/BRD documents
- Extracts requirements
- Generates test scenarios:
  - UI/UX
  - Functional Testing
  - Role-Based Testing

---

🧠 Architecture

SRS Upload → Parser → AI Model → Rule Engine → Test Scenarios

---

🌐 Run in Browser (No Installation)

This project runs using GitHub Codespaces.

---

▶️ Steps to Run

1. Open in Codespaces

Click:
Code → Codespaces → Create Codespace

---

2. Install Dependencies

Run:
pip install -r backend/requirements.txt

---

3. Start Backend

Run:
uvicorn backend.main:app --host 0.0.0.0 --port 8000

---

4. Start AI Model

Run:
docker-compose up -d

Then:
docker ps

Copy container ID and run:
docker exec -it <container_id> ollama run mistral

---

5. Open API

Go to:
http://localhost:8000/docs

---

6. Upload SRS

Use endpoint:
/upload-srs/

---

📤 Output

- Extracted requirements
- Generated test scenarios

---

🔐 Note

This setup is for development.
For production, use a secure local deployment.

---

🚀 Future Enhancements

- Excel export
- React frontend
- RTM mapping
