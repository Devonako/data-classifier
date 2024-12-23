# File Classifier and Data Scanner

This Python program scans files in a specified folder, classifies them by file type, and analyzes their contents for specific data types like credit card numbers and email addresses. It then generates a graphical report visualizing the file type distribution and the occurrences of the identified data.

## Features

- **File Classification:** Classifies files based on their extensions (e.g., .txt, .pdf, .docx).
- **Data Scanning:** Scans file contents for:
    - Credit card numbers (using regular expressions)
    - Email addresses (using regular expressions)
- **Graphical Reporting:** Generates two plots:
    - Pie chart showing the distribution of file types
    - Bar chart showing the number of occurrences of each data type

## Requirements

- Python 3.6 or higher
- matplotlib library (`pip install matplotlib`)

## How to Run

1. Save the code as a Python file (e.g., `file_classifier.py`).
2. Install the required library: `pip install matplotlib`
3. Run the script from your terminal: `python file_classifier.py`
4. Enter the path to the folder you want to analyze when prompted.

## Usage Example
Enter the folder path: /path/to/your/folder


The program will then generate two plots: one showing the file type distribution and another showing the occurrences of credit card numbers and email addresses in the scanned files.

## Important Notes

- **Regular Expressions:** The regex patterns used for data scanning are basic examples and might need adjustments depending on the specific formats you expect.
- **False Positives:** Regex can sometimes produce false positives. Further validation might be needed to confirm the accuracy of the identified data.
- **Data Security:** Handle sensitive data like credit card numbers responsibly and comply with relevant data privacy regulations.
- **Error Handling:** The program includes basic error handling for file encoding issues, but it's important to be aware that some data might be skipped in case of errors.

## Future Improvements

- **More Data Types:** Add support for scanning other data types like phone numbers, addresses, etc.
- **Improved Regex:** Refine the regex patterns for more accurate data extraction.
- **User Interface:** Develop a graphical user interface (GUI) for easier interaction.
- **Recursive Scanning:** Add an option to scan subfolders recursively.
- **Output Options:** Allow users to save the report as an image or PDF file.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for bug fixes, enhancements, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
