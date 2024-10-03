import pytest
import os
import sqlite3
from unittest.mock import patch, MagicMock
from project0.createdb import createdb  # Replace 'your_module' with the actual name of your Python file or module

@patch('os.path.exists')
@patch('os.remove')
@patch('sqlite3.connect')
def test_createdb(mock_connect, mock_remove, mock_exists):
    # Mock os.path.exists to return True, simulating that the file exists
    mock_exists.return_value = True
    
    # Mock the sqlite3 connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Call the function
    conn = createdb()
    
    # Check if os.remove was called because the file existed
    mock_remove.assert_called_once_with("./resources/normanpd.db")
    
    # Check if sqlite3.connect was called with the correct path
    mock_connect.assert_called_once_with("./resources/normanpd.db")
    
    # Check if the CREATE TABLE statement was executed
    mock_cursor.execute.assert_called_once_with('''CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
                    );''')
    
    # Check if the connection commit was called
    mock_conn.commit.assert_called_once()
    
    # Ensure that the returned connection is the mock connection
    assert conn == mock_conn

# createdb()