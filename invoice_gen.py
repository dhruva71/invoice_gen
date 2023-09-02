import toml
from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import date
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser(description='Generate PDF invoice from TOML data.')
parser.add_argument('toml_file', type=str, help='Path to the TOML file containing invoice data.')
parser.add_argument('output_filename', type=str, help='Name of the output PDF file.')
args = parser.parse_args()

template_folder = './templates/'
output_folder = './output/'

# Load the data from the TOML file
data = toml.load(args.toml_file)

# Calculate subtotal and total
subtotal = sum(
    item['amount'] if item['amount'] != 0 else item['hourly_cost'] * item['hours'] for
    item in data['items'])
total = subtotal  # Adjust this if you have taxes or other additions/deductions

# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(template_folder + 'template_01.html')

# Read CSS content
with open(template_folder + 'template_01.css', 'r') as f:
    css_content = f.read()

# Get today's date
today = date.today()

# Render the template with the data from the TOML file and CSS content
html = template.render(user=data['user'],
                       company=data['company'],
                       items=data['items'],
                       subtotal=subtotal,
                       total=total,
                       css_content=css_content,
                       invoice_date=today.strftime("%d-%m-%Y"))

# Save the rendered HTML to a file
with open(output_folder + 'invoice.html', 'w') as f:
    f.write(html)

# Convert the HTML to PDF using pdfkit
pdfkit.from_string(html, output_folder + args.output_filename)
