[restaurant-api-README.md](https://github.com/user-attachments/files/29281852/restaurant-api-README.md)
# 🍽️ Restaurant REST API

A backend REST API built with **Python and FastAPI** for managing restaurants with user authentication. Features JWT-based login, SQLite database, and a static frontend — all deployed on Render.

---

## ✨ Features

- 🔐 User registration and login with **JWT Authentication**
- 🔒 Password hashing (never stored as plain text)
- 🍴 Add, view, and delete restaurants
- ⭐ Store restaurant name and rating
- 🗄️ Persistent data storage with **SQLite**
- 🌐 Static HTML frontend served directly from the API
- 📦 Modular project structure with separate routes

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | FastAPI |
| Server | Uvicorn |
| Database | SQLite |
| ORM | SQLAlchemy |
| Auth | JWT (JSON Web Tokens) |
| Frontend | HTML / Static Files |
| Deployment | Render |

---

## 📁 Project Structure

```
restaurant--api/
├── main.py           # App entry point, router registration
├── models.py         # Database models (Restaurant, User)
├── schemas.py        # Pydantic schemas for request/response
├── database.py       # SQLite database connection setup
├── auth_helper.py    # JWT token creation and verification
├── routes/
│   ├── restaurants.py  # Restaurant CRUD endpoints
│   └── auth.py         # Register and login endpoints
├── static/
│   └── index.html    # Frontend UI
└── requirements.txt
```

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/PAVANVSAI/restaurant--api.git
cd restaurant--api
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the server**
```bash
uvicorn main:app --reload
```

**4. Open in browser**
```
http://localhost:8000        → Frontend UI
http://localhost:8000/docs   → Swagger API docs (interactive)
```

---

## 📡 API Endpoints

### 🔐 Auth Routes

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |

### 🍴 Restaurant Routes (Protected)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurants` | Get all restaurants |
| POST | `/restaurants` | Add a new restaurant |
| DELETE | `/restaurants/{id}` | Delete a restaurant by ID |

> **Note:** Restaurant routes require a valid JWT token in the `Authorization: Bearer <token>` header.

---

## 🔒 Authentication Flow

1. Register a new user via `POST /auth/register`
2. Login via `POST /auth/login` → receive JWT token
3. Use token in all restaurant requests as `Authorization: Bearer <your_token>`

---

## 🌐 Live Demo

- **Frontend:** [https://restaurant-api.onrender.com](https://restaurant-api.onrender.com)
- **API Docs:** [https://restaurant-api.onrender.com/docs](https://restaurant-api.onrender.com/docs)

> ⚠️ Render free tier may take 30–60 seconds to wake up on first request.

---

## 👨‍💻 Author

**Pavan Venkata Sai Makkala**
B.Tech CSE (AI & Robotics) — VIT Chennai (2025–2029)
🔗 [LinkedIn](https://linkedin.com/in/pavanvsaimakkala) | 🐙 [GitHub](https://github.com/PAVANVSAI)
