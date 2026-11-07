# 🍳 Cookbook REST API — FastAPI & CI

🌐 **Documentation Languages**

🇬🇧 **English** | 🇷🇺 [Русский](README.ru.md) | 🇷🇴 [Română](README.ro.md)

## 📖 Overview

Cookbook REST API is an asynchronous backend application developed with Python, FastAPI, and SQLAlchemy.

The application provides a REST API for creating and browsing cooking recipes, tracking recipe views, and sorting recipes by popularity.

This educational project demonstrates practical experience with asynchronous API development, relational databases, data validation, automated testing, and continuous integration.

## ✨ Features

- 🍽️ Create cooking recipes
- 📋 Retrieve a list of available recipes
- 🔎 View detailed information about individual recipes
- 📈 Automatically track recipe views
- ⭐ Sort recipes by popularity
- ⏱️ Use cooking time as a secondary sorting criterion
- 🗄️ Asynchronous database operations
- 📝 Automatic interactive API documentation
- 🧪 Automated testing with Pytest
- ⚙️ CI workflow configuration with GitHub Actions

## 🛠 Technology Stack

**Backend**
- Python
- FastAPI
- Pydantic
- Uvicorn

**Database**
- SQLite
- SQLAlchemy Async ORM
- aiosqlite

**Development & Quality**
- Git
- GitHub
- GitHub Actions
- Pytest
- Flake8

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PhilipTataroii/fastapi-recipes-ci.git
cd fastapi-recipes-ci
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000/

Database tables are created automatically when the application starts.

## 🔗 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/recipes` | Create a new recipe |
| GET | `/recipes` | Retrieve all recipes sorted by popularity |
| GET | `/recipes/{recipe_id}` | Retrieve recipe details and increment the view counter |

### Example: Create a Recipe

**POST `/recipes`**

```json
{
  "name": "Margherita Pizza",
  "cooking_time": 30,
  "ingredients": "Flour, tomatoes, mozzarella, basil",
  "description": "Prepare the dough, add the toppings, and bake."
}
```

A successful creation returns HTTP `201 Created`.

### Recipe Sorting

Recipes are sorted by:

1. Number of views, descending
2. Cooking time, ascending when view counts are equal

Each successful request for an individual recipe increases its view counter by one.

If a recipe does not exist, the API returns HTTP `404 Not Found`.

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

**Swagger UI**

http://127.0.0.1:8000/docs

**ReDoc**

http://127.0.0.1:8000/redoc

**OpenAPI Schema**

http://127.0.0.1:8000/openapi.json

## 🧪 Testing

The repository includes automated API tests in `test_main.py`.

Install the required test dependencies if necessary, then run:

```bash
python -m pytest -v
```

## ⚙️ Continuous Integration

The repository includes a `.github/workflows/` directory for GitHub Actions.

The CI configuration is intended to support automated project checks.

Check the repository's **Actions** tab for workflow execution results.

## 📂 Project Structure

```text
fastapi-recipes-ci/
├── .github/
│   └── workflows/
├── .flake8
├── .gitignore
├── database.py
├── main.py
├── models.py
├── schemas.py
├── test_main.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── README.ru.md
└── README.ro.md
```

## 🗄️ Database

The application uses SQLite with asynchronous SQLAlchemy sessions.

The database connection is configured in `database.py`.

Database tables are automatically initialized during application startup.

## 📝 Development Notes

This is an educational backend project intended for practical learning and professional portfolio demonstration.

The default SQLite configuration is suitable for local development and testing.

## 👨‍💻 Author

**Filip Tataroi**

Python Backend Developer

GitHub: https://github.com/PhilipTataroii

LinkedIn: https://www.linkedin.com/in/filip-tataroi/

**Project Type:** Educational FastAPI Backend Project
