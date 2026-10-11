# F1 Lab

## Prerequisites

Before starting, make sure you have installed:

- Git
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Node.js 20+
- npm

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aurrog/f1_Lab.git
cd f1_Lab
```

### 2. Backend setup

Install Python dependencies

```bash
uv sync 
source .venv/bin/activate
```

Start the development server

```bash
uv run uvicorn backend.app.main:app --reload
```

The backend will be avialable at:


- API: http://localhost:8000

- Swagger UI: http://localhost:8000/docs


### 3. Frontend setup

Open a new terminal in the project root.

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at:

- http://localhost:5173


## Running tests

Run backend tests from the project root:

```bash
uv run pytest tests/
```