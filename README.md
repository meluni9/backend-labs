# Expense Tracker API (Lab 3)

A RESTful API for tracking expenses built with Flask, SQLAlchemy (ORM), PostgreSQL, and Marshmallow for validation.

## Lab 3 Variant Info
**Group:** IM-32  
**Variant:** 2 (User-defined expense categories)  
**Task Description:**  
Implemented a category system where:
- **Global Categories:** Created by admins (or without `user_id`), visible to ALL users.
- **Private Categories:** Created by specific users, visible ONLY to the creator.
- When retrieving categories, a user sees the union of Global + Their Private categories.

## Features

- **Database:** Full persistence using PostgreSQL.
- **ORM:** Database interaction via SQLAlchemy.
- **Validation:** Strong input validation using Marshmallow schemas.
- **Migrations:** Database schema management with Flask-Migrate.
- **User Management:** Create, read, delete users.
- **Category Management:** Support for global and private categories.
- **Records:** Track expenses linked to users and categories.
- **Dockerized:** Full setup with App and DB containers.

## Prerequisites

- Docker & Docker Compose
- Postman (for testing)

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/meluni9/backend-labs.git
cd backend-labs
```

### 2. Run with Docker Compose (Recommended)

This command will start both the Flask App and the PostgreSQL database.

```bash
docker-compose up -d --build
```

The API will be available at `http://localhost:8080`.

### 3. Database Migrations (First Run Only)

If you are running the project for the first time, you need to apply database migrations to create tables.

1. Enter the app container:
   ```bash
   docker-compose exec app sh
   ```
2. Apply migrations:
   ```bash
   flask db upgrade
   ```
3. Exit the container:
   ```bash
   exit
   ```

## 🔌 API Endpoints

### Healthcheck
- `GET /healthcheck` - Check DB connection status

### Users
- `GET /users` - List all users
- `POST /user` - Create a user
  - Body: `{"username": "Alice"}`
- `GET /user/<id>` - Get user details
- `DELETE /user/<id>` - Delete a user (cascades to records)

### Categories
- `GET /category?user_id=<id>` 
  - Returns **Global Categories** + **Private Categories** for this user.
- `POST /category` - Create a category
  - Body (Global): `{"name": "Food"}`
  - Body (Private): `{"name": "My Hobby", "user_id": 1}`
- `DELETE /category/<id>` - Delete a category

### Records
- `POST /record` - Add a new expense
  - Body: `{"user_id": 1, "category_id": 2, "amount": 150.50}`
- `GET /record?user_id=<id>&category_id=<id>` - Filter records
- `GET /record/<id>` - Get record details
- `DELETE /record/<id>` - Delete a record

## Testing

The project includes validation. Examples of error handling:
- Trying to create a User with a short name -> **400 Bad Request**
- Trying to create a Record with non-existent User ID -> **400 Bad Request**
- Trying to get a non-existent Record -> **404 Not Found**

## Deployment

The application is deployed on Render.com:
https://backend-labs-s0hz.onrender.com
