# Meme Generator Project

## Overview
This project is a Meme Generator application that allows users to create memes by overlaying quotes onto images. The application supports both a command-line interface and a web interface built with Flask.

## Setup and Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Download and install the `pdftotext` command line tool from: https://www.xpdfreader.com/download.html

### Run the application
1. Web app:
  ```bash
  python app.py
  ```

2. CLI
   ```bash
   python meme.py
   ```

## Sub-Modules and Dependencies
### 1. `meme_engine`
- **Description**: This module is responsible for generating memes by adding quotes to images.
- **Dependencies**: Requires the `Pillow` library for image processing.
- **Usage Example**:
  ```python
  from meme_engine import MemeEngine
  meme = MemeEngine('./tmp')
  meme.make_meme('path/to/image.jpg', 'Quote body', 'Author')

### 2. `quote_engine`
- **Description**: This module handles the ingestion of quotes from various file formats (TXT, DOCX, PDF, CSV).
- **Dependencies**: Requires `python-docx`, `pandas`, and `pdftotext`.
- **Usage Example**:
  ```python
  from quote_engine import Ingestor
  quotes = Ingestor.parse('path/to/quotes.pdf')
