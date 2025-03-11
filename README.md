# authentication_api
Here’s a comprehensive **README.md** file for your Flask Authentication API project. You can copy and paste this into your repository and customize it as needed.

---

# Flask Authentication API

A secure and scalable **Flask-based REST API** for user authentication, featuring password hashing, user registration, and login functionality. Built with **PostgreSQL** for database management and **bcrypt** for password security.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Environment Variables](#environment-variables)
4. [API Endpoints](#api-endpoints)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features
- **User Registration**: Securely register new users with hashed passwords.
- **User Login**: Authenticate users with email and password.
- **Password Hashing**: Uses **bcrypt** for secure password storage.
- **PostgreSQL Integration**: Stores user data in a PostgreSQL database.
- **Environment Variables**: Sensitive data is managed using `.env` files.
- **Production-Ready**: Ready for deployment on platforms like Render or Heroku.

---

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for building the API.
- **PostgreSQL**: Relational database for storing user data.
- **bcrypt**: Password hashing library for secure authentication.
- **Render/Heroku**: Deployment platforms.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- Pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-authentication-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-authentication-api
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
Create a `.env` file in the root directory and add the following variables:

```plaintext
# Flask settings
HOST=0.0.0.0
PORT=5000

# Database settings
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_PORT=5432
```

---

## API Endpoints

### **POST /register**
Register a new user.

**Request Body**:
```json
{
  "firstname": "John",
  "lastname": "Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response**:
- Success:
  ```json
  {
    "message": "User created successfully"
  }
  ```
- Error:
  ```json
  {
    "error": "Missing required fields"
  }
  ```

---

### **POST /login**
Authenticate a user.

**Request Body**:
```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response**:
- Success:
  ```json
  {
    "message": "Login successful",
    "user": {
      "id": 1,
      "firstname": "John",
      "lastname": "Doe",
      "email": "john@example.com"
    }
  }
  ```
- Error:
  ```json
  {
    "error": "Invalid credentials"
  }
  ```

---

## Deployment

### Deploy to Render
1. Go to the [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub repository.
4. Configure the web service:
   - **Name**: Choose a name for your app.
   - **Environment**: Select **Python 3**.
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
5. Add environment variables:
   - Go to the **Environment** section.
   - Add the variables from your `.env` file.
6. Click **Create Web Service**.

### Deploy to Heroku
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Set environment variables:
   ```bash
   heroku config:set DB_USER=your_db_user DB_PASSWORD=your_db_password DB_HOST=your_db_host DB_NAME=your_db_name DB_PORT=5432
   ```
5. Push your code to Heroku:
   ```bash
   git push heroku main
   ```

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
