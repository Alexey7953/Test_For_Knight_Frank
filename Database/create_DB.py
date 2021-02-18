import sqlite3

with sqlite3.connect('Database.db') as connection:
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE  users ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "first_name      TEXT NOT NULL,"
        "last_name        TEXT NOT NULL,"
        "email      TEXT NOT NULL,"
        "password   TEXT NOT NULL,"
        "position    TEXT NOT NULL"
        ");"
    )
