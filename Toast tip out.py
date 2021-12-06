# Blue team
# Tip out Calc

import csv



with open('Shifts_Closed_2021_12_02.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
    