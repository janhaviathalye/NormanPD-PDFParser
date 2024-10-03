#Sorts the list of the nature of incidents and the number of times they have occurred. 
#It also sorts it alphabetically and case sensitively by the nature.

def status(db):
    curr = db.cursor()
    records = db.execute('''
                    SELECT nature, COUNT(*)
                    FROM incidents
                    GROUP BY nature
                    ORDER BY nature ASC;
                         ''')
    for (nature, count) in records:
        print(f"{nature}|{count}")  #Each field of the row is separated by the pipe character (|) and printed.