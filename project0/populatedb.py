#Inserts the data in records in the corresponding columns within the db
def populatedb(db, incidents):
    curr = db.cursor()
    records = [(data['Date Time'], data['Incident Number'], data['Location'], data['Nature'], data['ORI'])
               for data in incidents]
    
    curr.executemany('''
                    INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
                    VALUES (?, ?, ?, ?, ?);
                     ''', records)