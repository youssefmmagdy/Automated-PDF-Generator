# Simple Script to use the provided PDF4RoomKey module to create a PDF Room Key Card
# the script takes the demo data, and the default template and creates a joined PDF

# Import the PDF4RoomKey module
from pprint import pprint
from PDF4RoomKey import PDFGenerator, PDFTemplate
import json

# load the demo arrivals from /demo_data/arrivals.json
with open('./demo_data/arrivals.json') as f:
    arrivals = json.load(f)

# load the demo template from /demo_data/template.json
with open('./demo_data/hab_template.json') as f:
    template = json.load(f)

pdf_generator = PDFGenerator(None, None, template)

# tmpl = PDFTemplate(template)
# arrivals = tmpl.format_arrivals(arrivals)

# generate the PDF
pdf = pdf_generator._generate_pdf(arrivals)

pdf.output('test.pdf')