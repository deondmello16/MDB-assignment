import csv
import random
import string

# Define the header row for the CSV file
header = ["name", "srn", "semester", "section", "avg_marks"]

# Define the list of possible values for each column
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
srn_prefix = 'ENG'
semesters = ['1', '2', '3', '4', '5', '6', '7', '8']
sections = ['A', 'B', 'C']
min_marks = 50
max_marks = 100

# Define the number of entries to generate
num_entries = 100

# Generate the entries and write them to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(header)
    # Generate and write each entry
    for i in range(num_entries):
        name = random.choice(names)
        srn_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        srn = srn_prefix + srn_suffix
        semester = random.choice(semesters)
        section = random.choice(sections)
        avg_marks = round(random.uniform(min_marks, max_marks), 2)
        row = [name, srn, semester, section, avg_marks]
        writer.writerow(row)
