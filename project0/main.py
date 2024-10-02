import argparse
import fetchincidents
import extractincidents
import createdb
import populatedb
import status



def main(url):
    # Download data
    incident_data = fetchincidents.fetchincidents(url)

    # Extract data
    incidents = extractincidents.extractincidents(incident_data)
	
    # Create new database
    db = createdb.createdb()
	
    # Insert data
    populatedb.populatedb(db, incidents)
	
    # Print incident counts
    status.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

