import pypdf
from pypdf import PdfReader
from io import BytesIO
import re

def extractincidents(incident_data):

    incident_file = BytesIO(incident_data)
    incident_file_pdf = PdfReader(incident_file)
    records = []
    
    # Regex to match the Date/Time pattern
    date_time_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}')
   
    
    for page in incident_file_pdf.pages:
        text = page.extract_text(extraction_mode="layout")
        for line in text.split('\n'):
            line=line.strip()
           
            # Check if the current line starts with a date
            if re.match(r'^\d{1,2}/\d{1,2}/\d{4}', line):
                parts = re.split(r'\s{2,}', line)
                if len(parts) >= 5:
                    incident = {
                        'Date Time': parts[0],
                        'Incident Number': parts[1],
                        'Location': parts[2],
                        'Nature': parts[3],
                        'ORI': parts[4]
                    }
                    records.append(incident)

    return records