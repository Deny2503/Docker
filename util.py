import csv
import os
import sys

csv_file = os.getenv("CSV_FILE", "data.csv")

if not os.path.exists(csv_file):
    print(f"Error: File '{csv_file}' not found!")
    sys.exit(1)

print(f"Reading CSV file: {csv_file}")

with open(csv_file, newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    for row in reader:
        print("ROW:", row)
