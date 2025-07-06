# 📝 Smart Task Tracker API

A lightweight task management system built with **FastAPI**, **SQLite**, and a simple **HTML frontend**. It allows users to create, view, update, and delete tasks through a browser interface.

---

## 🚀 Features

- RESTful API with FastAPI  
- SQLite database (auto-created)  
- Full CRUD operations for tasks  
- HTML + JavaScript frontend  
- Interactive UI (Add, Complete, Delete)  
- CORS enabled for smooth frontend-backend communication

---

## 📁 Project Structure

```
smart-task-tracker-api/
├── main.py           # FastAPI app (routes + CORS)
├── models.py         # SQLAlchemy Task model
├── schemas.py        # Pydantic schemas
├── database.py       # SQLite DB setup
├── index.html        # Frontend UI
├── requirements.txt  # Python dependencies
├── tasks.db          # Auto-created DB file
└── README.md         # Project guide
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bhola-dev58/smart-task-tracker-api.git
cd smart-task-tracker-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv myenv
# Activate (Windows)
myenv\Scripts\activate
# Activate (Linux/macOS)
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Or manually install:
```bash
pip install fastapi uvicorn sqlalchemy
```

---

## ▶️ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

- Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Use the HTML Frontend

1. Open `index.html` (double-click or right-click → Open in browser)  
2. Use the form to add tasks  
3. Click “Complete” or “Delete” to manage them  
4. All actions send requests to your FastAPI API

---

## 🧪 API Testing (Optional)

Use the Swagger UI:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Or via curl:

```bash
curl -X POST "http://127.0.0.1:8000/tasks" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\": \"Read Book\", \"description\": \"Chapter 4\", \"is_completed\": false}"
```

---

## 🗂 View the SQLite Database

1. Install [DB Browser for SQLite](https://sqlitebrowser.org)  
2. Open `tasks.db` file  
3. Go to “Browse Data” tab → View `tasks` table

---

## 💡 Notes

- Database auto-creates on first request  
- Backend must be running before using the frontend  
- If you get CORS issues, ensure CORS middleware is added in `main.py`

---
## Output DEMO
  <h2>Screenshots</h2>
   <img src="https://github.com/user-attachments/assets/298d6938-b0aa-43b2-85fe-80008b1956a8" alt="output-test" width="500" height="300" />



## 🙋 Author

**Bhola Yadav**  
📱 WhatsApp: +91-9198709984  
🔗 GitHub: [bhola-dev58](https://github.com/bhola-dev58)

---

## 📃 License

This project is licensed under the MIT License

---

> 🚀 Happy Task Tracking!
