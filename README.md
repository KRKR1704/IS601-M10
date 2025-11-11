# FastAPI Secure User Model with CI/CD Pipeline (Docker Hub + GitHub Actions)
**Author:** Roopesh Kumar Reddy Kaipa  
**Date:** 11/10/2025  

---

## **Project Description**

This project extends the **FastAPI + PostgreSQL + Docker Compose** setup by adding a **secure user model**, **password hashing**, **Pydantic validation**, and a complete **CI/CD pipeline** using **GitHub Actions** and **Docker Hub**.

You will:
- Create a **secure User model** using **SQLAlchemy ORM**.
- Define **Pydantic schemas** for user creation and reading.
- Hash passwords before storage using a reliable cryptographic function.
- Implement **unit and integration tests** for database and schema validation.
- Configure a **CI/CD pipeline** to test, scan, and deploy automatically to Docker Hub.

The goal is to demonstrate modern DevOps integration for Python backends using **FastAPI**, **PostgreSQL**, **Docker**, and **GitHub Actions**.

---

## **How to Run the Project**

### Step 1 — Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### Step 2 — Build and Run Docker Containers

Ensure Docker Desktop is running, then build and start containers:

```bash
docker-compose up --build
```

This launches:
- **FastAPI** at `http://localhost:8000`
- **pgAdmin** at `http://localhost:5050`
- **PostgreSQL** at port `5432`

### Step 3 — Access the Application

- **FastAPI Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)  
- **pgAdmin:** [http://localhost:5050](http://localhost:5050)

Default Credentials for pgAdmin:
```
Email: admin@admin.com
Password: admin
Host: db
Port: 5432
Username: postgres
Password: postgres
```

---

## **User Model Structure**

### SQLAlchemy Model

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
```

### Pydantic Schemas

```python
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
```

### Password Hashing Functions

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

---

## **Testing Locally**

### Run Tests with Pytest

```bash
pytest
```

To view coverage:

```bash
pytest --cov=app
```

### Types of Tests
- **Unit Tests:** Hashing, schema validation, and password verification.
- **Integration Tests:** PostgreSQL container tests verifying uniqueness and invalid email handling.

---

## **CI/CD Pipeline (GitHub Actions)**

The workflow automatically:
1. Runs tests using `pytest`.
2. Performs a **Trivy vulnerability scan**.
3. Builds and pushes a Docker image to Docker Hub.

Example workflow file (`.github/workflows/main.yml`):

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: pytest -v

      - name: Run Trivy Security Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          ignore-unfixed: true
          severity: 'CRITICAL,HIGH'

      - name: Build and Push Docker Image
        uses: docker/build-push-action@v3
        with:
          context: .
          push: true
          tags: zabuza1704/is601_m8:latest
```

---

## **Project Setup (Detailed)**

### Prerequisites

- **Python 3.11+**
- **Docker & Docker Compose**
- **GitHub Account**
- **Docker Hub Account**

### Steps Recap

| Step | Description |
|------|--------------|
| 1️⃣ | Clone the repo |
| 2️⃣ | Build Docker containers |
| 3️⃣ | Run `pytest` for local testing |
| 4️⃣ | Push to GitHub to trigger CI/CD |
| 5️⃣ | Confirm image on Docker Hub |

---

## 📘 **References**

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Passlib Docs](https://passlib.readthedocs.io/)
- [GitHub Actions Guide](https://docs.github.com/en/actions)
- [Docker Hub](https://hub.docker.com/)

---