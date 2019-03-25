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
        for i in range(0, N):
            m = Measurement(data['anchorId'][i], data['tagId'][i], data['rssi'][i], data['timestamp'][i])
            measurements.append(m)
        return measurements

    @staticmethod
    def zrangebyscore(r, tagId, begin, end):
        """
        Parameters:
            tagId (int) - id of tag for which to get measurements

        """
        zset = "tag" + str(tagId) + "_data"
        data = r.zrangebyscore(zset, begin, end, withscores=True)
        measurements = []
        for d in data:
            parts = d[0].split(':')
            timestamp = d[1]
            measurements.append(Measurement(parts[0], tagId, parts[1], timestamp))
        return measurements

    @staticmethod
    def zremrangebyrank(r, tagId, begin, end):
        zset = "tag" + str(tagId) + "_data"
        return r.zremrangebyrank(zset, begin, end)

    def save(self, r):
        dataId = r.incr('data_counter')
        key = 'tag' + self.tagId + "_data"
        score = int(self.timestamp)
        element = self.anchorId + ":" + self.rssi + ":" + str(dataId)
        r.zadd(key, {element:score})
