# 🍳 Cookbook REST API — FastAPI & CI

🌐 **Limbi disponibile pentru documentație**

🇬🇧 [English](README.md) | 🇷🇺 [Русский](README.ru.md) | 🇷🇴 **Română**

## 📖 Prezentare generală

Cookbook REST API este o aplicație backend asincronă dezvoltată utilizând Python, FastAPI și SQLAlchemy.

Aplicația oferă un API REST pentru crearea și vizualizarea rețetelor culinare, monitorizarea numărului de vizualizări și sortarea rețetelor după popularitate.

Acest proiect educațional demonstrează competențe practice în dezvoltarea API-urilor asincrone, gestionarea bazelor de date relaționale, validarea datelor, testarea automată și integrarea continuă (CI).

## ✨ Funcționalități

- 🍽️ Crearea rețetelor culinare
- 📋 Obținerea listei de rețete disponibile
- 🔎 Vizualizarea informațiilor detaliate despre o rețetă
- 📈 Contorizarea automată a vizualizărilor
- ⭐ Sortarea rețetelor după popularitate
- ⏱️ Sortarea suplimentară după timpul de preparare
- 🗄️ Operații asincrone cu baza de date
- 📝 Documentație API interactivă generată automat
- 🧪 Teste automate cu Pytest
- ⚙️ Configurație CI utilizând GitHub Actions

## 🛠 Tehnologii utilizate

**Backend**
- Python
- FastAPI
- Pydantic
- Uvicorn

**Bază de date**
- SQLite
- SQLAlchemy Async ORM
- aiosqlite

**Instrumente de dezvoltare**
- Git
- GitHub
- GitHub Actions
- Pytest
- Flake8

## 🚀 Instalare și pornire

### 1. Clonarea repository-ului

```bash
git clone https://github.com/PhilipTataroii/fastapi-recipes-ci.git
cd fastapi-recipes-ci
```

### 2. Crearea unui mediu virtual

```bash
python -m venv .venv
```

Activarea în Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

În Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalarea dependențelor

```bash
pip install -r requirements.txt
```

### 4. Pornirea aplicației

```bash
uvicorn main:app --reload
```

După pornire, API-ul va fi disponibil la adresa:

http://127.0.0.1:8000/

Tabelele bazei de date sunt create automat la pornirea aplicației.

## 🔗 Endpoint-uri REST API

| Metodă | Endpoint | Descriere |
|---|---|---|
| POST | `/recipes` | Crearea unei rețete noi |
| GET | `/recipes` | Obținerea rețetelor sortate după popularitate |
| GET | `/recipes/{recipe_id}` | Obținerea detaliilor unei rețete și incrementarea numărului de vizualizări |

### Exemplu de creare a unei rețete

**POST `/recipes`**

```json
{
  "name": "Margherita Pizza",
  "cooking_time": 30,
  "ingredients": "Flour, tomatoes, mozzarella, basil",
  "description": "Prepare the dough, add the toppings, and bake."
}
```

La crearea cu succes, API-ul returnează HTTP `201 Created`.

### Sortarea rețetelor

Rețetele sunt sortate după următoarele criterii:

1. Numărul de vizualizări — descrescător
2. Timpul de preparare — crescător, atunci când numărul de vizualizări este egal

La fiecare accesare reușită a unei rețete individuale, contorul vizualizărilor crește cu o unitate.

Dacă rețeta nu există, API-ul returnează HTTP `404 Not Found`.

## 📚 Documentație API

FastAPI generează automat documentația interactivă.

**Swagger UI**

http://127.0.0.1:8000/docs

**ReDoc**

http://127.0.0.1:8000/redoc

**Schema OpenAPI**

http://127.0.0.1:8000/openapi.json

## 🧪 Testare

Repository-ul include teste API automate în fișierul `test_main.py`.

Instalați dependențele necesare pentru testare, dacă este cazul, apoi executați:

```bash
python -m pytest -v
```

## ⚙️ Integrare continuă (CI)

Repository-ul conține directorul `.github/workflows/` pentru GitHub Actions.

Configurația CI este destinată automatizării verificărilor proiectului.

Rezultatele executării workflow-urilor pot fi consultate în secțiunea **Actions** de pe GitHub.

## 📂 Structura proiectului

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

## 🗄️ Baza de date

Aplicația utilizează SQLite împreună cu sesiuni asincrone SQLAlchemy.

Conexiunea la baza de date este configurată în fișierul `database.py`.

Tabelele sunt create automat la pornirea aplicației.

## 📝 Note privind dezvoltarea

Acesta este un proiect backend educațional, realizat pentru exersarea dezvoltării software și prezentarea competențelor într-un portofoliu profesional.

Configurația implicită SQLite este potrivită pentru dezvoltare și testare locală.

## 👨‍💻 Autor

**Filip Tataroi**

Python Backend Developer

GitHub: https://github.com/PhilipTataroii

LinkedIn: https://www.linkedin.com/in/filip-tataroi/

**Tipul proiectului:** Proiect educațional backend dezvoltat cu FastAPI
