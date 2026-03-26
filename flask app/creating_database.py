from easy import SQL

db = SQL('my_database.db')

query =  """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
""" 
#db.run(query)

query1 =  """CREATE TABLE IF NOT EXISTS booking_exhibits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    exhibit_name TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""
#db.run(query1)


query2 =  """CREATE TABLE IF NOT EXISTS booking_tours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    tour_name TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""
#db.run(query2)

query3 = """CREATE TABLE IF NOT EXISTS booking_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_name TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""
#db.run(query3)

query4 = """CREATE TABLE IF NOT EXISTS booking_workshops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    workshop_name TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""
#db.run(query4)

data = [query, query1, query2, query3, query4]

for i in data:
    db.run(i)