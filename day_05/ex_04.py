import csv

def show_restaurants():
    with open('vote.csv', 'r') as file:
        reader = csv.reader(file)

        return reader

def vote(restaurant_name):
    rows = []
    with open('vote.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)
        for row in reader:
            if row[0] == restaurant_name:
                row[1] = str(int(row[1]) + 1)
            rows.append(row)

    with open('vote.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


