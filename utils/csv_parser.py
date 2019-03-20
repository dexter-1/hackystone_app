import csv

def readcsv(file):
    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        columns = {}
        for header in headers:
            columns[header] = []
        for row in reader:
            for i in range(0, len(row)):
                columns[headers[i]].append(row[i])
    return columns