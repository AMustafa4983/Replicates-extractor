# Replicates Extractor

## Overview
The Replicates Extractor is a Flask-based web application designed to extract and suggest materials, tools, items, equipment, and suppliers from text documents. It leverages GPT-based natural language processing to analyze and process text data.

## Features
- **Text Extraction**: Processes text files to extract relevant information about materials and suppliers.
- **GPT Integration**: Uses GPT models for intelligent text analysis and extraction.
- **Data Cleaning**: Includes a pipeline for cleaning and normalizing text data.
- **User-Friendly Interface**: Provides a simple and intuitive web interface for uploading text files and viewing extracted data.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/AMustafa4983/Replicates-extractor.git
   cd Replicates-extractor
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Flask App**
   ```
   flask run
   ```

## Usage

After starting the Flask app, navigate to `http://localhost:5000` in your web browser. Upload a text file, and the application will process it to extract and suggest materials, tools, items, equipment, and suppliers.

## Contributing

Contributions to improve the application's functionality or to extend its capabilities are welcome. Please follow the standard fork-and-pull request workflow for contributions.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for more details.
