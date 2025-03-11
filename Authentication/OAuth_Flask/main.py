from flask import Flask, request, jsonify
import authModel
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "WELCOME TO OUR AUTHENTICATION API"

# Register route
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        try:

            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400
            # Receive data as JSON
            data = request.get_json()
            logger.debug(f"Received data: {data}")
            firstname = data.get("firstname")
            lastname = data.get("lastname")
            email = data.get("email")
            password = data.get("password")

            # Validate required fields
            if not all([firstname, lastname, email, password]):
                logger.error("Missing required fields")
                return jsonify({"error": "Missing required fields"}), 400

            # Register data into PostgreSQL Database
            if authModel.create(firstname, lastname, email, password):
                logger.debug("User created successfully")
                return jsonify({"message": "User created successfully"}), 201
            else:
                logger.error("Failed to create user")
                return jsonify({"error": "Failed to create user"}), 500

        except Exception as e:
            logger.error(f"Error in /register: {e}")
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid request method"}), 405

# Login route
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        try:

            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400
            # Receive data as JSON
            data = request.get_json()
            logger.debug(f"Received data: {data}")
            email = data.get("email")
            password = data.get("password")

            # Validate required fields
            if not all([email, password]):
                logger.error("Missing email or password")
                return jsonify({"error": "Missing email or password"}), 400

            # Check and login user from PostgreSQL
            user = authModel.lognin(email, password)
            if user:
                logger.debug("Login successful")
                return jsonify({"message": "Login successful", "user": user}), 200
            else:
                logger.error("Invalid credentials")
                return jsonify({"error": "Invalid credentials"}), 401

        except Exception as e:
            logger.error(f"Error in /login: {e}")
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid request method"}), 405

# Run the Flask app
if __name__ == "__main__":
    # Use environment variables for host and port
    host = os.getenv("HOST", "0.0.0.0")  # Default to 0.0.0.0 for production
    port = int(os.getenv("PORT", 5000))  # Default to port 5000
    app.run(host=host, port=port, debug=False)  # Disable debug mode in production