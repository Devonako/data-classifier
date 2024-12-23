import os
import re
import matplotlib.pyplot as plt

def classify_files(folder_path):
    """
    Classifies files in a folder and scans for various sensitive data types.

    Args:
      folder_path: The path to the folder containing the files.

    Returns:
      A dictionary mapping file types to the number of files of that type,
      and a dictionary mapping data types to the number of occurrences found.
    """

    file_types = {}
    data_types = {
        "Credit Cards": 0,
        "Emails": 0,
        "Phone Numbers": 0,
        "Social Security Numbers": 0,
        "IP Addresses": 0,
        "Driver's Licenses": 0,
        "Passport Numbers": 0,
        "Bank Account Numbers": 0,
        "Dates of Birth": 0,
        "Health Records": 0  # This will need more specific regex/keyword matching
    }

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in file_types:
                file_types[file_extension] += 1
            else:
                file_types[file_extension] = 1

            # Scan file contents for data types
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8', errors='ignore') as f:
                file_content = f.read()
                data_types["Credit Cards"] += len(re.findall(r"\b(?:\d[ -]*?){13,16}\b", file_content))
                data_types["Emails"] += len(re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", file_content))
                data_types["Phone Numbers"] += len(re.findall(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b", file_content))
                data_types["Social Security Numbers"] += len(re.findall(r"\b\d{3}-\d{2}-\d{4}\b", file_content))
                data_types["IP Addresses"] += len(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", file_content))
                # Add more regex patterns for other data types below (examples provided)
                data_types["Driver's Licenses"] += len(re.findall(r"\b[A-Z]{2}\d{6,8}\b", file_content))  # Example pattern, adjust as needed
                data_types["Passport Numbers"] += len(re.findall(r"\b[A-Z]\d{7}\b", file_content))  # Example pattern, adjust as needed
                data_types["Bank Account Numbers"] += len(re.findall(r"\b\d{9,18}\b", file_content))  # Example pattern, adjust as needed
                data_types["Dates of Birth"] += len(re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", file_content))  # Example pattern, adjust as needed
                # For "Health Records", you'll likely need more sophisticated techniques than basic regex

    return file_types, data_types

def generate_report(file_types, data_types):
    """
    Generates graphical reports of the file types and data types found.

    Args:
      file_types: A dictionary mapping file types to the number of files of that type.
      data_types: A dictionary mapping data types to the number of occurrences found.
    """

    # File type distribution
    labels = list(file_types.keys())
    sizes = list(file_types.values())
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('File Type Distribution')

    # Data type distribution
    labels = list(data_types.keys())
    sizes = list(data_types.values())
    plt.subplot(1, 2, 2)
    plt.bar(labels, sizes)
    plt.title('Data Type Occurrences')
    plt.ylabel('Number of Occurrences')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    file_types, data_types = classify_files(folder_path)
    generate_report(file_types, data_types)