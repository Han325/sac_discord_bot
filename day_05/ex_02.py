import csv

def read_from_csv():
    with open('strings.csv', 'r') as file:
        reader = csv.reader(file)


        for row in reader:
            print(row[0])

        return reader

read_from_csv()
