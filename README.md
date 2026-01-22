# 📘 Najot Talim Backend (FastAPI)

This project is a **backend system for Najot Talim** built with **FastAPI**. It provides CRUD operations, asynchronous database handling, and automatically generated API documentation.

---

## ✨ Key Features

* **CRUD Operations:** Create, read, update, and delete resources such as courses, lessons, or users.
* **Asynchronous Database Queries:** Uses async DB handling for better performance.
* **API Documentation:** FastAPI provides automatic OpenAPI/Swagger docs for easy testing and exploration.

---

## 🔹 Project Structure

```
Najot-Talim-Backend-FastAPI/
├── api/
│   ├── endpoints.py
│   ├── services.py
│   └── models.py
├── database/
│   ├── connection.py
│   └── models.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **SQLite**
* **SQLAlchemy / Tortoise ORM** (for async DB handling)
* **Pydantic** (data validation)
* **Git / GitHub**

---

## 🔑 Environment Variables (.env)

```
DEBUG=True
DATABASE_URL=sqlite:///najot_talim.db
```

---

## 👤 User Flow

1. Access API endpoints for CRUD operations
2. Perform asynchronous create, read, update, and delete operations
3. Explore and test all endpoints via `/docs` or `/redoc`

---

## 📄 License

Private project, intended for learning and personal portfolio.

---

## 👨‍💻 Author

Developed by **Muhammadumar Umarov**
Telegram: @Muhammadumar_umarov
Python Developer
