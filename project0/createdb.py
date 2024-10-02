import sqlite3
import os

def createdb():
    if os.path.exists("./resources/normanpd.db"):
        os.remove("./resources/normanpd.db")
    connection = sqlite3.connect("./resources/normanpd.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
                    );''')
    connection.commit()
    return connection