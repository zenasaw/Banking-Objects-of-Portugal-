import csv
import time
with open('code/data/raw/amzn.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        print(row)

from datetime import datetime


class StockData:
    def __init__(self, path):
        self.path = path
        self.data = None

    def load(self):
        """A function to assing the csv dataset to a list of lists.
        Does not include headers.

        All data is expected to be a string
        """
        # to keep us in compliance with EU standards, we must log the datetime
        # of all data loads
        epoch = time.time()
        self._date = datetime.utcfromtimestamp(epoch).\
            strftime('%Y-%m-%d %H:%M:%S')
        print("DATA LOADED AT", self._date)

        # open data using csv reader
        with open(self.path, newline='') as file:
            reader = csv.reader(file)
            # skip header row
            next(reader, None)
            # append list of strings into list
            self.data = []
            for row in reader:
                self.data.append(row)
