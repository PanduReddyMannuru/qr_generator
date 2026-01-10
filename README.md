# QR Code Generator

A simple web-based QR code generator built with Flask. This application allows you to generate QR codes from text or URLs with an easy-to-use web interface.

## Features

- **Web Interface**: User-friendly web application to generate QR codes
- **Quick Generation**: Generate QR codes in real-time
- **Multiple Input Support**: Generate QR codes from text, URLs, or any data
- **CLI Tool**: Command-line utility for batch QR code generation

## Project Structure

```
qrgen/
├── app.py                 # Flask web application
├── qr_generator.py        # Command-line QR code generator
├── requirements.txt       # Python dependencies
├── static/               # Generated QR code images
├── templates/
│   └── index.html       # Web interface template
├── README.md            # This file
└── stash.sh            # Shell script utility
```

## Requirements

- Python 3.x
- Flask 3.1.2
- qrcode 8.2
- Pillow 12.1.0

## Installation

1. Clone or download this repository:
```bash
cd qrgen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install Flask qrcode pillow
```

## Usage

### Web Application

Run the Flask app:
```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

Enter the text or URL you want to encode, click the button, and your QR code will be generated and displayed.

### Command-Line Tool

For generating QR codes via command line:
```bash
python qr_generator.py
```

Follow the prompts to enter your text or URL. The QR code will be saved as `my_qr.png`.

## Dependencies

- **Flask** (3.1.2) - Web framework
- **qrcode** (8.2) - QR code generation library
- **Pillow** (12.1.0) - Image processing
- **Werkzeug** (3.1.5) - WSGI utilities
- **Jinja2** (3.1.6) - Template engine

## File Descriptions

- **app.py**: Main Flask application that serves the web interface and handles QR code generation requests
- **qr_generator.py**: Standalone script for generating QR codes from the command line
- **index.html**: HTML template for the web interface
- **stash.sh**: Shell script utility
- **static/**: Directory where generated QR code images are stored

## License

This project is open source and available for personal and educational use.
