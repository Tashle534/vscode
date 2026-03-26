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
insertBLOB(1, "Sample Image", "/Users/ashleigh/PycharmProjects/PythonProject2/web-applications/sample.jpg")
