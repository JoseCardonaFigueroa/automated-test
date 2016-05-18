import csv


def read_csv():
    with open('data_source/source.csv','rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar= '|')
        lines = []
        for row in reader:
            lines.append(row[0])
        return lines
