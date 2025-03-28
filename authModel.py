from flask import Flask, request, jsonify
from authModel import *
import bcrypt
import os
from dotenv import load_dotenv
import logging
from supabase import create_client, Client

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Flask app
app = Flask(__name__)

# Function to create a user
def create_user(firstname, lastname, email, passwd):
    try:
        # Hash the password
        hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Insert user into Supabase
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email.lower(),
            "password": hashed_password
        }
        response = supabase.table("users").insert(data).execute()

        return True
        
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return False

# Function to log in user
def login_user(email, passwd):
    try:
        # Fetch user by email
        response = supabase.table("users").select("*").eq("email", email.lower()).single().execute()
        user = response.data
        
        if user:
            stored_hashed_password = user.get("password").encode('utf-8')
            if bcrypt.checkpw(passwd.encode('utf-8'), stored_hashed_password):
                return user
            else:
                logger.debug("Invalid password")
                return None
        else:
            logger.debug("User not found")
            return None
    except Exception as e:
        logger.error(f"Error logging in: {e}")
        return None


