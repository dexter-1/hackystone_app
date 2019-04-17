import time
import numpy as np
from hackystone_app.models.measurement import Measurement
from hackystone_app.models.anchor import Anchor
import hackystone_app.algorithms.algorithms as algorithms

class TagPositionCalculator:
    """Class to compute the position of a tag with the given tagId if possible.
    """

    def __init__(self, r):
        self.anchorMap = Anchor.hgetall(r)

    def compute_tag_position(self, r, tagId, deltaT = 7):
        """Goes into the redis database to extract all measurements of tagId
        taken between the current time t0 and t0-deltaT.
        If there are measurements from at least 3 anchors, makes a computation and returns the result, otherwise returns None.

        Parameters:
        r - redis connection
        tagId - str - tag ID
        deltaT - float - time in seconds
        anchorMap - map - map from anchorId to anchor objects
        """
        currentTime = time.time()
        measurements = Measurement.zrangebyscore(r, tagId, currentTime-deltaT, float('inf'))
        measurements.reverse()
        mToUse = []
        anchorIds = set()
        for m in measurements:
            if m.anchorId not in anchorIds:
                anchorIds.add(m.anchorId)
                mToUse.append(m)
        if len(anchorIds) < 3:
            return np.array([None, None])
        return algorithms.compute_position(mToUse, self.anchorMap)