import csv

def csv_to_dict(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {}
        for row in reader:
            for column, value in row.items():
                if column in data:
                    data[column].append(value)
                else:
                    data[column] = value
    return data
