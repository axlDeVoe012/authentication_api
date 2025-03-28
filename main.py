from flask import Flask, request, jsonify
from authModel import *
from logging import Logger
import bcrypt
import os
from dotenv import load_dotenv
from supabase import create_client, Client


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

            data = request.get_json()
            firstname = data.get("firstname")
            lastname = data.get("lastname")
            email = data.get("email")
            password = data.get("password")

            if not all([firstname, lastname, email, password]):
                return jsonify({"error": "Missing required fields"}), 400

            if create_user(firstname, lastname, email, password):
                return jsonify({"message": "User created successfully"}), 201
            else:
                return jsonify({"error": "Failed to create user"}), 500

        except Exception as e:
            logger.error(f"Error in /register: {e}")
            return jsonify({"error": str(e)}), 500

# Login route
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        try:
            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400

            data = request.get_json()
            email = data.get("email")
            password = data.get("password")

            if not all([email, password]):
                return jsonify({"error": "Missing email or password"}), 400

            user = login_user(email, password)
            if user:
                return jsonify({"message": "Login successful", "user": user}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except Exception as e:
            logger.error(f"Error in /login: {e}")
            return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    
    app.run(debug=False)