#################################  C S V  #################################
import csv, io
from emergio.models import Leads
from django.core.files.base import ContentFile

def create_csv(data):
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)

    # Write the header row
    if data and len(data) > 0:
        headers = data[0].keys()
        csv_writer.writerow(headers)

    # Write the data rows
    for row in data:
        csv_writer.writerow(row.values())

    csv_content = csv_buffer.getvalue()

    leads = Leads.objects.create()
    leads.file.save('leads.csv', ContentFile(csv_content), save=True)