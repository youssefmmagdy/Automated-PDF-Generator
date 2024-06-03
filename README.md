# Automated Room Key Holder PDF Generator with Date Integration

## Project Description

This project aims to develop a software tool for hotel staff that automates the creation of customized PDFs for printing on pre-printed A6-sized room key holders. The tool will be user-friendly, catering to non-technical staff, and capable of importing guest data, including arrival and departure dates, while ensuring proper formatting and validation of long names.

## Illustration

### Pre-Printed A6 Room Key Holder (outside)

[PDF of Pre-Printed A6 Room Key Holder](./documentation/assets/RoomKeyCard-clear.pdf)

### Generated PDF by this library

[PDF of content to Print](./documentation/assets/RoomKeyCard-filling.pdf "Title")

### Actual Document after Printing (physically)

[PDF of final A6 Room Key Holder](./documentation/assets/RoomKeyCard-filled.pdf)

## Key Features

- **Data Import and Processing:**
  - Ability to import guest data from an API or a CSV file.
  - Automatic extraction of guest details: First Name, Last Name, Room Number (if available), Breakfast option (Yes/No), Arrival Date, and Departure Date.

- **PDF Generation:**
  - Quick generation of a PDF with guest details correctly formatted for the A6 key holder.
  - Inclusion of checkboxes for the breakfast option and fields for arrival and departure dates.

- **Name Validation and Formatting:**
  - Special handling for long names to ensure they fit within the designated space on the key holder without compromising the layout.
  - Options to automatically adjust font size or abbreviate names if they exceed a certain length.

- **User-Friendly Interface:**
  - Simple, intuitive interface for uploading data and generating the PDF.
  - Preview functionality for verifying the layout before printing.

- **Error Handling and Data Validation:**
  - Robust error handling for data inconsistencies, especially in date formats.
  - Validation checks for data accuracy and print readiness.

- **Printer Compatibility:**
  - Ensures the generated PDFs are compatible with standard office printers used in hotels.

## End-User Benefits

- **Rapid Customization:** Enables quick and efficient customization of room key holders.
- **Professional Presentation:** Ensures a high-quality, professional look for the key holders.
- **User Accessibility:** Designed for easy use by all staff members, regardless of technical skill level.

## Project Scope

The project will include:
- Developing a streamlined software interface for data import and PDF generation.
- Implementing a template that aligns with pre-printed key holders, including handling long names and date fields.
- Ensuring the tool has robust error handling and data validation capabilities.
- Initial testing for accuracy and ease of use.

## Timeline

The project aims for a rapid development cycle, scheduled to complete the first prototype within 1 month:
- [ ] **Week 1:** Requirements gathering and software design.
- [ ] **Week 2:** Development of core functionalities (data import, PDF generation, name validation).
- [ ] **Week 3:** Integration of the template design and initial testing.
- [ ] **Week 4:** Interface development, final testing, and prototype completion.

# Getting Started

This project uses venv to have its own virtual environment.

## Work in Environment

### Activate VENV
```
source .venv/bin/activate
```

### Play in Playground

You can install the package locally in an editable mode using the following command.

```sh
pip install --editable .
```

If that is not working an alternative could be:

```sh
export PYTHONPATH=/path/to/root:$PYTHONPATH
python playground/get_data.py
```

## Create Environment in Project

```
python3 -m venv .venv
```

## Setup Dev dependencies

### 1. install dependencies

Make sure you are in the virtual environment

```
pip install -r requirements.txt
```

### Copy the `.env`

copy the file `_env` to `.env` and insert the right keys

- [ ] TODO: use githubs secret to get rid of that step
