# F1 Lab

## Prerequisites

Before starting, make sure you have installed:

- Python 3.12+
- uv
- Node.js 20+
- npm

## Getting Started

### Clone repository

```bash
git clone https://github.com/aurrog/f1_Lab.git
cd f1_Lab
```

### Backend

```bash
uv sync 
source .venv/bin/activate

uvicorn backend.app.main:app --reload
```

Backend: 
```http://localhost:8000```

Swagger UI: 
```http://localhost:8000/docs```


## Frontend

```bash
cd frontend

npm install
npm run dev
```

Frontend:
```http://localhost:5173```