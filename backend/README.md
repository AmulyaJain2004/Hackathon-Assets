# Hackathon Hub Backend API

A robust, scalable Django Rest Framework API for the Hackathon Hub project with full authentication, user management, and note management functionality.

## Features

- **User Authentication**:
  - JWT Authentication using djangorestframework-simplejwt
  - User registration with email & password
  - User login
  - Password reset via email
  - Change password endpoint

- **Custom User Model**:
  - Email as the unique identifier (no username)
  - Extended user profile information

- **Note Management**:
  - Full CRUD operations for notes
  - Notes belong to users
  - Filter, search, and ordering capabilities

- **API Documentation**:
  - Swagger/OpenAPI documentation
  - Interactive API testing

## Tech Stack

- Django 5
- Django Rest Framework
- djangorestframework-simplejwt
- drf-yasg for Swagger documentation
- CORS headers support
- Filtering, pagination, and search capabilities

## Setup Instructions

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hackathon-hub/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional):
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/v1/auth/register/` - Register a new user
- `POST /api/v1/auth/token/` - Obtain JWT tokens
- `POST /api/v1/auth/token/refresh/` - Refresh JWT token
- `POST /api/v1/auth/token/verify/` - Verify JWT token
- `GET /api/v1/auth/profile/` - Get user profile
- `PUT /api/v1/auth/profile/` - Update user profile
- `POST /api/v1/auth/change-password/` - Change password
- `POST /api/v1/auth/password-reset/` - Request password reset
- `POST /api/v1/auth/password-reset-confirm/<uid>/<token>/` - Confirm password reset

### Notes

- `GET /api/v1/notes/` - List all notes (paginated)
- `POST /api/v1/notes/` - Create a new note
- `GET /api/v1/notes/{id}/` - Retrieve a note
- `PUT /api/v1/notes/{id}/` - Update a note
- `PATCH /api/v1/notes/{id}/` - Partially update a note
- `DELETE /api/v1/notes/{id}/` - Delete a note

### Documentation

- `GET /docs/` - Swagger UI
- `GET /redoc/` - ReDoc UI

## Development

### Running Tests

```
python manage.py test
```

### Code Style

This project follows PEP 8 style guidelines. Use tools like flake8 or black to ensure code quality.

## License

MIT 