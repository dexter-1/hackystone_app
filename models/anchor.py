"""Anchor model
"""

from hackystone_app.utils import csv_parser

class Anchor:

    def __init__(self, anchorId, X, Y):
        self.anchorId = anchorId
        self.X = X
        self.Y = Y

    @staticmethod
    def readcsv(file):
        data = csv_parser.readcsv(file)
        anchors = []
        N = len(data['anchorId'])
        for i in range(0, N):
            a = Anchor(data['anchorId'][i], data['X'][i], data['Y'][i])
            anchors.append(a)
        return anchors

    @staticmethod
    def hgetall(r):
        hset = 'anchors'
        data = r.hgetall(hset)
        anchors = {}
        for k, v in data.iteritems():
            X,Y = v.split(':')
            anchors[k] = Anchor(k, float(X), float(Y))
        return anchors