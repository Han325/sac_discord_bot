import csv

def write_to_csv(*args):
    # Open or create the CSV file in write mode
    with open('strings.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for arg in args:
            writer.writerow([arg])
