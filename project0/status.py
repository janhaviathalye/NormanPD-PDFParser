def status(db):
    curr = db.cursor()
    records = db.execute('''
                    SELECT nature, COUNT(*)
                    FROM incidents
                    GROUP BY nature
                    ORDER BY nature ASC;
                         ''')
    for (nature, count) in records:
        print(f"{nature}|{count}")