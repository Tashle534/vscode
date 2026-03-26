import pathlib
from easy import SQL
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Database setup
db = SQL("MyDatabase.db")

#setting up images/ blob table
import sqlite3

# Function to convert image to binary data
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(img_id, name, photo_path):
    try:
        conn = sqlite3.connect('photos.db')
        cursor = conn.cursor()
        
        sqlite_insert_blob_query = """INSERT INTO images (id, name, photo) VALUES (?, ?, ?)"""
        
        # Convert photo to binary
        photo = convertToBinaryData(photo_path)
        data_tuple = (img_id, name, photo)
        
        # Insert
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image inserted successfully")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data", error)
    finally:
        if conn:
            conn.close()

# Example usage
#insertBLOB(1, "Sample Image", "/Users/ashleigh/PycharmProjects/PythonProject2/web-applications/sample.jpg")


class table_creation:
    def __init__(self):
        self.create_users() 
        self.create_exhibitions()
        self.create_employees()
        self.create_tickets()
        self.images()
        

    def create_users(self):
        query = """
        CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email UNIQUE TEXT NOT NULL)
        """
        db.execute(query)
        
    def create_exhibitions(self):
        query = """
        CREATE TABLE IF NOT EXISTS exhibitions ( 
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL)
        """
        db.execute(query)
        
    def create_employees(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees ( 
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        position TEXT NOT NULL,
        email UNIQUE TEXT NOT NULL)
        """
        db.execute(query)
        
    def create_tickets(self):
        query = """
        CREATE TABLE IF NOT EXISTS tickets ( 
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        exhibition_id INTEGER NOT NULL,
        purchase_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (exhibition_id) REFERENCES exhibitions(id))
        """
        db.execute(query)
        
    def images(self):
        query = """
        CREATE TABLE IF NOT EXISTS images ( 
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        photo BLOB NOT NULL)
        """
        db.execute(query)
        
table_creation()

for image in pathlib.Path("images").glob("*.*"):
    try:
        insertBLOB(image.stem, image.name, str(image))
    except Exception as e:
        print(f"Error inserting image {image.name}: {e}")

# @app.route("/")
# def index():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    