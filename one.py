import os
import re
import matplotlib.pyplot as plt

# aa@example.com
# aa@example.com
# aa@example.com
# 6011044422221811
def classify_files(folder_path):
    """
    Classifies files in a folder based on their extension and scans for specific data types.

    Args:
      folder_path: The path to the folder containing the files.

    Returns:
      A dictionary mapping file types to the number of files of that type,
      and a dictionary mapping data types to the number of occurrences found.
    """

    file_types = {}
    data_types = {"Credit Cards": 0, "Emails": 0}
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
    plt.figure(figsize=(12, 6))  # Adjust figure size for better layout
    plt.subplot(1, 2, 1)  # Create subplot for file type distribution
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('File Type Distribution')

    # Data type distribution
    labels = list(data_types.keys())
    sizes = list(data_types.values())
    plt.subplot(1, 2, 2)  # Create subplot for data type distribution
    plt.bar(labels, sizes)
    plt.title('Data Type Occurrences')
    plt.ylabel('Number of Occurrences')

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    file_types, data_types = classify_files(folder_path)
    generate_report(file_types, data_types)