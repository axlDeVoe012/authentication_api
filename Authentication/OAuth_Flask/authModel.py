from flask import Flask, request, jsonify
import psycopg2
import bcrypt
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()


#Function to create a user
def create(fistname, lastname, email, passwd):
    conn = None
    cur = None
    try:
        #Hashing the users password using bcrypt for security
        hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        query = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
        #Connection to the database
        conn = psycopg2.connect(
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")            
        )

        #Instance the object allows to interact with database (queries)
        cur = conn.cursor()
        cur.execute(query,(fistname, lastname, email, hashed_password.decode('utf-8')))
        conn.commit()

        return True
    except(Exception, psycopg2.DatabaseError) as error:
        print("ERROR: ", error)
        return False
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

#User login function
def lognin(email, passwd):
    conn = None

    try:
        query = "SELECT * FROM users WHERE LOWER(email) = LOWER(%s)"
        #Connection to the database
        conn = psycopg2.connect(
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")               
        )
    
        #Instance the object allows to interact with database (queries)
        cur = conn.cursor()
        cur.execute(query,(email,))
        user = cur.fetchone()

        if user:

            logger.debug(f"User tuple: {user}")
            #Pass verification
            stored_hashed_password = user[4].encode('utf-8')

            if bcrypt.checkpw(passwd.encode('utf-8'), stored_hashed_password):
                logger.debug("Login successful")
                return user
            else:
                logger.debug("Invalid password")
                #return nothing if password is incorrect
                return None
        else:
            logger.debug("User not found")
            #return nothing if user not found or does not exist
            return None
            
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(f"ERROR: {error}")
        return None  # Return None on error
    finally:
        # Ensure the cursor and connection are closed properly
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()