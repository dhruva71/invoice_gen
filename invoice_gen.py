import toml
from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import date

template_folder = './templates/'
output_folder = './output/'

# Load the data from the TOML file
data = toml.load('invoice_data.toml')

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

# save the rendered HTML to a file
with open(output_folder + 'invoice.html', 'w') as f:
    f.write(html)

# Convert the HTML to PDF using pdfkit
pdfkit.from_string(html, output_folder + 'invoice.pdf')
