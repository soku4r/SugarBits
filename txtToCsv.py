import csv

with open('restz2.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)
    with open('restz2.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('longitude', 'latitude'))
        writer.writerows(lines)