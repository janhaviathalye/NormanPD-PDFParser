# cis6930fa24-project0

Project 0 - CIS 6930: Data Engineering Fall 2024

Name: Janhavi Athalye

# Project Description

This project is designed to download and extract incident data from the Norman, Oklahoma Police Department's incident reports, which are available in PDF format. The project processes the PDF data to extract fields such as date, incident number, location, nature of the incident, and ORI. The data is stored in a SQLite database, and the nature of each incident is printed along with the frequency of occurrences, sorted alphabetically.

The project is implemented using Python, SQLite3, regular expressions, and the pypdf library for PDF processing. Command-line arguments are used to pass the URL of the PDF to download.


# How to install
Ensure you have pipenv installed otherwise install it using the following command.

```
pip install pipenv
```
The following command can also be used.

```
pipenv install -e
```

## How to run

To run the project, execute the following command after activating the pipenv environment:

```
pipenv run python project0/main.py --incidents <URL_of_incident_PDF>
```
An example command for running the project:

```
pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-01_daily_incident_summary.pdf

```
This will download the incident PDF, extract the data, store it in a SQLite database, and print a summary of the incident types and their occurrences.


To run the test cases, execute the following command:
```
pipenv run python -m pytest
```

## Project Demo Video


https://github.com/user-attachments/assets/202cee61-e975-4c5b-a9dc-898e9e038cc3


## Functions

#### main.py: 
Makes calls to all the required functions in order. It takes the incident PDF url from the command line and passes it to the first function: fetchincidents(url).

#### fetchincidents(url): 
This function takes the URL of the incident PDF, downloads it, and returns the binary data.

#### extractincidents(incident_data): 
This function processes the downloaded PDF data and extracts the fields:

Date/Time <br />
Incident Number<br />
Location<br />
Nature of the incident<br />
ORI<br /> 

The extracted fields are stored in a list of dictionaries for further processing.


#### createdb(): 
This function creates a SQLite database normanpd.db with the appropriate table schema (incidents). If the database already exists, it is replaced with a new one.

#### populatedb(db, incidents): 
This function takes the extracted data and inserts it into the incidents table in the SQLite database.

#### status(db): 
This function queries the database for the distinct incident types (natures) and the number of times each type occurs. It prints the results to the console, sorted alphabetically by the nature field.


## Database Development
The project utilizes SQLite as a lightweight database to store incident data extracted from the PDFs. The following functions handle the creation, population, and querying of the SQLite database.

#### createdb() Function
The createdb() function is responsible for creating a SQLite database file named normanpd.db. If the database file already exists in the resources/ directory, it is deleted and replaced with a new one. This ensures that each time the program is run, it starts with a fresh database. The function creates a table named incidents with the following schema:

```
CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
);

```

#### populatedb(db, incidents) Function
The populatedb() function is responsible for inserting the incident data extracted from the PDF into the incidents table in the SQLite database.

The SQLite database connection returned by the createdb() function.
incidents: A list of dictionaries, where each dictionary contains the fields extracted from the PDF (incident_time, incident_number, incident_location, nature, and incident_ori).
Process:

The function converts each dictionary (representing an incident) into a tuple of values that correspond to the columns in the incidents table.
It uses the executemany() function to efficiently insert all the incidents into the table in one go. This reduces the overhead of executing individual INSERT statements and speeds up the population process.

Example SQL:

```
INSERT INTO incidents 
(incident_time, 
incident_number, 
incident_location, 
nature, 
incident_ori)

VALUES (?, ?, ?, ?, ?);
```

#### status(db) Function
The status() function provides a summary of the incidents stored in the database. It queries the incidents table to count the occurrences of each unique incident type (the nature field) and prints the results in a sorted format.

The function runs a SQL query that groups the incidents by their nature and counts how many times each type of incident occurred. The results are sorted alphabetically by the nature field:


```
SELECT nature, COUNT(*)
FROM incidents
GROUP BY nature
ORDER BY nature ASC;
```

## Test Cases

This project includes several test cases designed to verify the correctness and functionality of key functions, such as downloading the incident PDF, extracting data, creating and populating the SQLite database, and querying the database for incident summaries. These tests ensure that each component works as expected and can handle edge cases such as missing data, incorrect formatting, and multiple-line fields.

The tests are located in the tests/ directory, and each function is tested individually. You can run all the tests using pytest, and each function has been tested with both normal inputs and edge cases.

#### test_fetchincidents.py <br />

Purpose: Tests the fetchincidents() function to ensure that it can successfully download a PDF file from the provided URL.

Test Case:

The test case mocks the URL and simulates downloading the data. The response is a mock object that mimics a real PDF download.
It verifies that the function correctly handles the HTTP request and retrieves data.

#### test_extractincidents.py <br />

Purpose: Tests the extractincidents() function, which processes the PDF and extracts the necessary fields like date/time, incident number, location, nature, and ORI.

Test Case:

The test case mocks a PDF file with sample incident data. It verifies that the extractincidents() function correctly parses the PDF and extracts the expected fields.
It also checks that the function can handle multi-line fields and extracts the correct data from each row.

#### test_createdb.py <br />

Purpose: Tests the createdb() function to ensure that a fresh SQLite database is created, and the schema is correctly set up.

Test Case:

The test case checks whether the database file is correctly created in the resources/ directory.
It verifies that the incidents table exists with the correct schema, and no old data remains after creating a new database.

#### test_populatedb.py <br />

Purpose: Tests the populatedb() function, which takes the extracted data and inserts it into the SQLite database.

Test Case:

The test case verifies that the extracted data is correctly inserted into the incidents table.
It checks that the number of records in the table matches the number of incidents passed to the function.


#### test_status.py <br />

Purpose: Tests the status() function, which queries the database and prints a summary of the incident types and their counts.

Test Case:

The test case populates the database with mock data and verifies that the status() function correctly queries the data, sorts the results alphabetically, and prints the correct counts.
It also ensures that the output is formatted correctly, with fields separated by pipes (|) and each row followed by a newline.



## Bugs and Assumptions
Multiple Line Cells: In some cases, cells (like location or nature) may span multiple lines. The code handles this by merging lines that do not start with a new record's date.

PDF Formatting: The Norman Police Department might change the PDF format at any time. The code currently assumes that the format remains consistent (fields are always in the same order).

Network Issues: The project does not currently handle network-related errors, such as the URL being unreachable or the file being moved/removed from the Norman PD website.
