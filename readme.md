# InvoiceGen

## Description

This is a simple invoice generator for a small business. It is written in Python and uses the pdfkit library to generate
pdfs.

## Usage

Install `wkhtmltopdf`. On Ubuntu, this can be done with `sudo apt install wkhtmltopdf`.
Download the dist folder, run the executable.

## Windows build

Clone the repo, setup a virtual environment, and install:

1. poetry: `pip install poetry`
2. dependencies: `poetry install`
3. pyinstaller: `pip install pyinstaller`

Build the executable:

1. `pyinstaller --onefile invoice_gen.py`
2. `python ./post_build.py` (to copy necessary files to the dist folder)