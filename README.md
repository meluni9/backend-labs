# Expense Tracker API (Lab 2)

A Flask-based REST API for tracking expenses, managing users, and categories.

## Features

- **User Management**: Create, view, and delete users.
- **Category Management**: Create, view, and delete expense categories.
- **Record Management**: Create and delete expense records.
- **Filtering**: View records filtered by User ID and Category ID.
- **Healthcheck**: Endpoint to verify service status.
- **Dockerized**: Easy setup with Docker and Docker Compose.

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

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

### Run with Docker Compose

```bash
docker-compose up --build
```

The service will be available at `http://localhost:8080`.

## API Endpoints

### General
- `GET /` - Welcome message
- `GET /healthcheck` - API status and time

### Users
- `GET /users` - List all users
- `POST /user` - Create a user
- `GET /user/<user_id>` - Get user details
- `DELETE /user/<user_id>` - Delete a user

### Categories
- `GET /category` - List all categories
- `POST /category` - Create a category
- `DELETE /category/<category_id>` - Delete a category

### Records (Expenses)
- `POST /record` - Create an expense record
- `GET /record/<record_id>` - Get record details
- `DELETE /record/<record_id>` - Delete a record
- `GET /record?user_id=<id>&category_id=<id>` - Get filtered records

## Testing with Postman

This repository includes a Postman collection for testing all endpoints.

1. Import the collection and environment files from the submitted archive (or `postman/` folder if you added it).
2. Ensure the `domain` variable is set to your local or deployed URL.

### Postman Flow
The project logic has been verified using Postman Flows:
![Postman Flow](lab2_flow.png) 

## Deployment

The application is deployed on Render.com:
https://backend-labs-s0hz.onrender.com
