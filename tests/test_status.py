import pytest
from unittest.mock import MagicMock, patch
from project0.status import status  # Replace 'your_module' with the actual name of the module where 'status' is defined


@patch('builtins.print')  # Mock the print function
def test_status(mock_print):
    # Sample data returned by the SELECT query
    mock_data = [
        ('Traffic Stop', 10),
        ('Suspicious', 5)
    ]
    
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    
    # Mock the execute method to return mock data
    mock_db.execute.return_value = mock_data
    mock_db.cursor.return_value = mock_cursor
    
    # Call the status function with the mock database
    status(mock_db)
    
    # Ensure that the execute method was called with the correct query
    mock_db.execute.assert_called_once_with('''
                    SELECT nature, COUNT(*)
                    FROM incidents
                    GROUP BY nature
                    ORDER BY nature ASC;
                         ''')
    
    # Check that print was called with the correct arguments
    mock_print.assert_any_call("Traffic Stop|10")
    mock_print.assert_any_call("Suspicious|5")
    
    # Ensure that print was called exactly twice (once for each record)
    assert mock_print.call_count == 2

# test_status()