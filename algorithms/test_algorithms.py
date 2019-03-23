import numpy as np
from hackystone_app.algorithms import algorithms
from hackystone_app.models.anchor import Anchor
from hackystone_app.models.measurement import Measurement

def test_compute_position():
    anchorIds = ["1", "2", "3", "4"]
    anchors = [Anchor(anchorIds[0], 0, 0), Anchor(anchorIds[1], 10, 0), Anchor(anchorIds[2], 10, 10), Anchor(anchorIds[3], 0, 10)]
    anchorMap = {}
    for i in range(0, len(anchorIds)):
        anchorMap[anchorIds[i]] = anchors[i]
    point = np.array([7, 3])
    measurements = []
    tagId = "1"
    timestamp = 0
    for anchor in anchorMap.values():
        dist = np.linalg.norm(np.array([anchor.X, anchor.Y]) - point)
        rssi = algorithms.compute_rssi(dist)
        measurements.append(Measurement(anchor.anchorId, tagId, rssi, timestamp))
    predicted_pos = algorithms.compute_position(measurements, anchorMap)
    assert np.linalg.norm(predicted_pos - point) < 10e-6

def run():
    test_compute_position()

if __name__ == "__main__":
    run()