# make necessary copies to dist folder
import os
import shutil

# Copy invoice_data.toml to dist/invoice_data.toml
shutil.copy2('invoice_data.toml', 'dist/invoice_data.toml')

# create dist/templates folder
os.mkdir('dist//templates')

# Copy templates/template_01.css to dist/template_01.css
shutil.copy2('templates/template_01.css', 'dist/templates/template_01.css')

# Copy templates/template_01.html to dist/template_01.html
shutil.copy2('templates/template_01.html', 'dist/templates/template_01.html')

# Create output folder in dist
os.mkdir('dist//output')
