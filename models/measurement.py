"""Measurement model
"""

from hackystone_app.utils import csv_parser

class Measurement:

    def __init__(self, anchorId, tagId, rssi, timestamp):
        self.anchorId = anchorId
        self.tagId = tagId
        self.rssi = rssi
        self.timestamp = timestamp

    @staticmethod
    def readcsv(file):
        data = csv_parser.readcsv(file)
        measurements = []
        N = len(data['tagId'])
        for i in range(0, len(data['tagId'])):
            m = Measurement(data['anchorId'][i], data['tagId'][i], data['rssi'][i], data['timestamp'][i])
            measurements.append(m)
        return measurements

    @staticmethod
    def read_from_redis(r, score):
        pass

    def write_to_redis(r):
        pass
