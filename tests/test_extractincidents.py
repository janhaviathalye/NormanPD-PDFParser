import pytest
from unittest.mock import MagicMock, patch
from project0.extractincidents import extractincidents  # Adjust this import according to your project structure
from io import BytesIO

def test_extract_incidents():

    with open('./docs/2024-08-01_daily_incident_summary.pdf', 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()
    
    total_records = extractincidents(pdf_bytes)

    assert len(total_records) == 402

# test_extract_incidents()