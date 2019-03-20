import scipy.optimize
import numpy as np

def computeDistance(measurements, anchors):
    """Computes the distance of a point from the corresponding anchor of a measurement
    """
    n = 1.4267
    A = -59.0636
    rssi = np.array([m.rssi for m in measurements])
    distance = np.exp((A-rssi)/(10*n));
    return distance

def computePosition(measurements, anchors):
    """
    Parameters:
    measurements - array - array of measurements
    anchors - map - anchors
    """
    distances = computeDistance(measurements, anchors)
    distances.reshape(len(distances), 1)
    anchorX = np.zeros((len(measurements), 1))
    anchorY = np.zeros((len(measurements, 1))
    for i in range(0, len(measurements)):
        anchorX[i,0] = anchors[measurements.anchorId].X
        anchorY[i,0] = anchors[measurements.anchorId].Y 
    def lossfct(x):
        return distances**2 - (x[0]-anchorX)**2 - (x[1]-anchorY)**2
   x0 = np.array([0,0])
   return scipy.optimize.least_squares(lossfct, x0)