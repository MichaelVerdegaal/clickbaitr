import csv
import os
import re

from langid import classify


def remove_first_column():
    """
    Removes the keyword column from the dataset
    :return: csv with only the titles contained
    """
    source = open("data.csv", "r", encoding="utf-8")
    reader = csv.reader(source)
    result = open("data_columns_removed.csv", "w", newline='\n', encoding=" utf-8")
    writer = csv.writer(result)

    row_count = 0
    for row in reader:
        del row[0]
        writer.writerow(row)
        row_count += 1
        print(f"Columns removed: {row_count}\n")


def remove_non_en():
    """
    Removes the non-English titles from the dataset
    :return: csv with only English titles
    """
    # Set up files
    source = open("data_columns_removed.csv", "r", encoding="utf-8")
    reader = csv.reader(source)
    output = open("data_language_cleaned.csv", "w", newline='', encoding="utf-8")
    writer = csv.writer(output)

    row_count = 0
    for row in reader:
        language_result = classify(row[0])
        if language_result[0] == "en":
            writer.writerow(row)
        row_count += 1
        print(f"Language checked: {row_count}")


def remove_emoji():
    """
    Removes emoji from the titles
    :return: csv with only non-emoji titles
    """
    # Set up files
    source = open("data_language_cleaned.csv", "r", encoding="utf-8")
    reader = csv.reader(source)
    output = open("data_cleaned.csv", "w", newline='\n', encoding="utf-8")
    writer = csv.writer(output)

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    row_count = 0
    for row in reader:
        row[0] = str(emoji_pattern.sub(r'', row[0]))
        writer.writerow(row)
        row_count += 1
        print(f"Emoji removed: {row_count}")


remove_first_column()
remove_non_en()
remove_emoji()
os.remove("data_columns_removed.csv")
os.remove("data_language_cleaned.csv")
