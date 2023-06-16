import csv

def analyze():
    with open('ratings.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        max_votes = 0
        most_voted_restaurant = ''

        for row in csv_reader:
            restaurant, votes = row[0], int(row[1])
            if votes > max_votes:
                max_votes = votes
                most_voted_restaurant = restaurant

    return "The top voted place is"  + most_voted_restaurant + " with " + str(max_votes) + " votes."

