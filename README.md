# Expense Tracker API (Lab 4: Authentication)

A RESTful API for tracking expenses built with Flask, SQLAlchemy, and Marshmallow, now featuring **JWT-based Authentication** and **Password Hashing**.

## Lab 4 Variant Info
**Group:** IM-32  
**Task Description:**  
Implemented a full authentication flow using **JSON Web Tokens (JWT)**:
- **JWT Authentication:** Implemented using `flask-jwt-extended`.
- **Password Security:** Passwords are never stored in plain text; they are hashed using `passlib` (pbkdf2_sha256).
- **Access Control:** All resource-related endpoints (Users, Categories, Records) are protected with the `@jwt_required()` decorator.
- **Custom Error Handlers:** Specific responses for expired, invalid, or missing tokens.

## Features

- **Authentication:** Dedicated `/register` and `/login` endpoints.
- **Security:** Secure password hashing and JWT identity verification.
- **Database:** PostgreSQL persistence via SQLAlchemy ORM.
- **Validation:** Strong input validation using Marshmallow schemas.
- **Migrations:** Managed database schema updates with Flask-Migrate.
- **Access Control:** Differentiated access to Global vs Private categories based on the authenticated user's identity.

## Prerequisites

- Docker & Docker Compose
- Postman (to test the authentication flow)

## Setup & Run

### 1. Configure Secret Key
Before running the application, generate a secret key for JWT:
```bash
python -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'
```
Set this value as an environment variable: `JWT_SECRET_KEY`.

### 2. Run with Docker Compose
```bash
docker-compose up -d --build
```
The API will be available at `http://localhost:8080`.

### 3. Database Migrations
Apply migrations to create the new `users` table with password support:
```bash
docker-compose exec app flask db upgrade
```

## API Endpoints

### Authentication (Public)
- `POST /register` - Create a new account
  - Body: `{"username": "Alice", "password": "securepassword"}`
- `POST /login` - Authenticate and receive a token
  - Body: `{"username": "Alice", "password": "securepassword"}`
  - Response: `{"access_token": "your_jwt_token_here"}`
- `GET /healthcheck` - Check DB connection

### Protected Endpoints (Requires `Authorization: Bearer <token>`)

#### Users
- `GET /users` - List all users
- `GET /user/<id>` - Get user details
- `DELETE /user/<id>` - Delete a user

#### Categories
- `GET /category` - Returns **Global Categories** + **Private Categories** for the authenticated user.
- `POST /category` - Create a category (Global if `user_id` is null, else Private)
- `DELETE /category/<id>` - Delete a category

#### Records
- `POST /record` - Add a new expense record
- `GET /record?user_id=<id>&category_id=<id>` - Filter records
- `GET /record/<id>` - Get record details
- `DELETE /record/<id>` - Delete a record

## Testing with Postman Flow

1. **Register:** Create a user via `/register`.
2. **Login:** Send a request to `/login` to receive your **Access Token**.
3. **Authorize:** Copy the token. In Postman, go to the **Authorization** tab, select **Bearer Token**, and paste the token.
4. **Access:** Now you can access protected resources like `/users` or `/category`. Without the token, the API will return a **401 Unauthorized** error.

## Deployment

The application is deployed on Render.com:
[https://backend-labs-s0hz.onrender.com](https://backend-labs-s0hz.onrender.com)