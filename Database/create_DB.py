import sqlite3

with sqlite3.connect('Database.db') as connection:
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS metro ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "station_name      TEXT NOT NULL UNIQUE,"
        "location_station        TEXT NOT NULL"
        ");"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS  object ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name_object      TEXT NOT NULL UNIQUE,"
        "location_object        TEXT NOT NULL,"
        "flore     INTEGER NOT NULL,"
        "square     INTEGER NOT NULL,"
        "type_object        TEXT NOT NULL,"
        "station_metro        TEXT NOT NULL REFERENCES metro(station_name)"
        ");"
    )
