# 🚀 FastAPI Boilerplate

A minimal and scalable FastAPI boilerplate with database support, testing, and Docker.

## 📦 Features
- ✅ **FastAPI** with dependency injection
- ✅ **SQLAlchemy** (Supports SQLite, PostgreSQL, MySQL)
- ✅ **Alembic** for database migrations
- ✅ **Pydantic V2**
- ✅ **Pytest** for testing
- ✅ **Docker-ready**
- ✅ **CORS and Exception Handling**

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-boilerplate.git your-project-name
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
```bash
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Create a .env file in the root directory
```env
DATABASE_URL=sqlite:///./todos.db
```

### 5️⃣ Create Database
```bash
alembic upgrade head
```

## 🏗️ Run the Server
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000

## 🧪 Running Tests
```bash
pytest
```

## 🐳 Running with Docker
Build the Docker image:
```bash
docker build -t fastapi-boilerplate .
docker run -p 8000:8000 --env-file .env fastapi-boilerplate
```

## 📜 API Endpoints
| Method    | Endpoint | Description |
| --------- | -------- | ----------- |
| GET       | /todos   | Get all todos |
| POST      | /todos   | Create a new todo |
| DELETE    | /todos/{id} | Delete a todo |


## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ♥ by [**Eduardo Baptista**](https://github.com/EduardoBaptista01)

