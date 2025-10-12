# Backend Labs

A simple Flask REST API with healthcheck endpoint.

## Features

- Welcome endpoint at `/`
- Healthcheck endpoint at `/healthcheck` with status and current date
- Docker containerization
- Docker Compose support

## Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional, for containerized setup)

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/meluni9/backend-labs.git
cd backend-labs
```

### 2. Create virtual environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
flask --app app run --host 0.0.0.0 -p 8080
```

The API will be available at `http://localhost:8080`

## Docker Setup

### Build and run with Docker

```bash
docker build -t app:latest .
docker run -it --rm -p 8080:8080 -e PORT=8080 app:latest
```

### Run with Docker Compose

```bash
docker-compose up
```

To rebuild after changes:

```bash
docker-compose up --build
```

## API Endpoints

### Welcome
- **URL:** `/`
- **Method:** `GET`
- **Response:**
```json
{
  "message": "Welcome!"
}
```

### Healthcheck
- **URL:** `/healthcheck`
- **Method:** `GET`
- **Response:**
```json
{
  "status": "ok",
  "date": "2025-10-12T14:30:45.123456"
}
```

## Deployment

The application is deployed on Render.com and accessible at:
```
https://backend-labs-s0hz.onrender.com
```

## Project Structure

```
backend-labs/
├── app/
│   ├── __init__.py
│   └── views.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

## Technologies

- Flask - Web framework
- Docker - Containerization
- Render.com - Deployment platform
