# RESTful API with Flask

A simple RESTful API built with Flask for managing users. This project demonstrates the fundamentals of creating web APIs with Python.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Testing](#testing)

## ✨ Features

- **User Management**: Add, retrieve, and list users
- **JSON Responses**: All data exchanged in JSON format
- **Error Handling**: Proper HTTP status codes and error messages
- **RESTful Design**: Follows REST API conventions
- **Lightweight**: Built with Flask's minimalist approach

## 🔧 Requirements

- Python 3.x
- Flask

## 📦 Installation

1. **Install Flask**:
   ```bash
   pip install Flask
   ```

2. **Clone or download the project files**

## 🚀 Usage

### Starting the Server

**Method 1: Direct execution**
```bash
python3 task_04_flask.py
```

**Method 2: Flask CLI (recommended)**
```bash
flask --app task_04_flask.py run
```

The server will start on `http://127.0.0.1:5000`

## 🛠 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Welcome message | Plain text |
| `GET` | `/status` | API status | Plain text |
| `GET` | `/data` | List all usernames | JSON array |
| `GET` | `/users/<username>` | Get user by username | JSON object |
| `POST` | `/add_user` | Add new user | JSON object |

## 📝 Examples

### 1. Welcome Message
```bash
curl http://localhost:5000/
```
**Response:**
```
Welcome to the Flask API!
```

### 2. Check API Status
```bash
curl http://localhost:5000/status
```
**Response:**
```
OK
```

### 3. List All Users
```bash
curl http://localhost:5000/data
```
**Response:**
```json
["alice", "john"]
```

### 4. Get Specific User
```bash
curl http://localhost:5000/users/alice
```
**Response:**
```json
{
  "username": "alice",
  "name": "Alice",
  "age": 25,
  "city": "San Francisco"
}
```

**User not found:**
```json
{
  "error": "User not found"
}
```

### 5. Add New User
```bash
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
  }'
```
**Response (201 Created):**
```json
{
  "message": "User added",
  "user": {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
  }
}
```

**Missing username (400 Bad Request):**
```bash
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
  }'
```
**Response:**
```json
{
  "error": "Username is required"
}
```

## 📁 Project Structure

```
restful-api/
├── task_04_flask.py    # Main Flask application
├── README.md           # Project documentation
└── ...                 # Other project files
```

## 🧪 Testing

### Manual Testing with curl

Test all endpoints:

```bash
# Test welcome message
curl http://localhost:5000/

# Test status
curl http://localhost:5000/status

# Test empty user list
curl http://localhost:5000/data

# Test adding a user
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"test","name":"Test User","age":30}'

# Test getting user list
curl http://localhost:5000/data

# Test getting specific user
curl http://localhost:5000/users/test

# Test non-existent user
curl http://localhost:5000/users/nonexistent

# Test missing username error
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","age":30}'
```

### Automated Testing

The application includes proper error handling and follows REST conventions for automated testing compatibility.

## 🔍 HTTP Status Codes

- `200 OK`: Successful GET requests
- `201 Created`: Successful user creation
- `400 Bad Request`: Missing required fields
- `404 Not Found`: User not found (handled as 200 with error message)

## 💡 Notes

- Users are stored in memory and will be lost when the server restarts
- The API is designed for development/testing purposes
- No authentication or authorization is implemented
- All JSON responses are properly formatted with appropriate Content-Type headers

## 🤝 Contributing

This is an educational project. Feel free to fork and modify for learning purposes.

## 📄 License

This project is created for educational purposes as part of the Holberton School curriculum.