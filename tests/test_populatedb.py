import pytest
from unittest.mock import MagicMock
from project0.populatedb import populatedb  # Replace 'your_module' with the actual module where 'populatedb' is located


def test_populatedb():
    # Sample data (list of dictionaries)
    incidents = [
        {
            'Date Time': '8/1/2024 0:04',
            'Incident Number': '2024-00055419',
            'Location': '1345 W LINDSEY ST',
            'Nature': 'Traffic Stop',
            'ORI': 'OK0140200'
        },
        {
            'Date Time': '8/1/2024 0:18',
            'Incident Number': '2024-00055420',
            'Location': '1820 BEVERLY HILLS ST',
            'Nature': 'Suspicious',
            'ORI': 'OK0140200'
        }
    ]
    
    # Expected records to be inserted into the database
    expected_records = [
        ('8/1/2024 0:04', '2024-00055419', '1345 W LINDSEY ST', 'Traffic Stop', 'OK0140200'),
        ('8/1/2024 0:18', '2024-00055420', '1820 BEVERLY HILLS ST', 'Suspicious', 'OK0140200')
    ]
    
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    
    # Call the function with the mock db and incidents data
    populatedb(mock_db, incidents)
    
    # Ensure that the cursor was created
    mock_db.cursor.assert_called_once()
    
    # Ensure that executemany was called with the correct SQL and records
    mock_cursor.executemany.assert_called_once_with('''
                    INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
                    VALUES (?, ?, ?, ?, ?);
                     ''', expected_records)

# test_populatedb()