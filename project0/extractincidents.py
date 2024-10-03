import pypdf
from pypdf import PdfReader
from io import BytesIO
import re

def extractincidents(incident_data):

    incident_file = BytesIO(incident_data)
    incident_file_pdf = PdfReader(incident_file)
    records = []
    exclude_line = ["Date / Time", "Incident Number", "Location", "Nature", "Incident ORI"]
    
    
    # Regex to match the Date/Time pattern
    date_time_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}')
   
    
    for page in incident_file_pdf.pages:
        text = page.extract_text(extraction_mode="layout")
        for line in text.split('\n'):
            line=line.strip()

            for str in exclude_line:
                if line.startswith(str):
                    continue
           
            # Check if the current line starts with a date
            if re.match(r'^\d{1,2}/\d{1,2}/\d{4}', line):
                chunks = re.split(r'\s{2,}', line)
                if len(chunks) >= 5:
                    incident = {
                        'Date Time': chunks[0],
                        'Incident Number': chunks[1],
                        'Location': chunks[2],
                        'Nature': chunks[3],
                        'ORI': chunks[4]
                    }
                    records.append(incident)
                

    return records