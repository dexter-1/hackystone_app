import scipy.optimize
import numpy as np

# BA2135 PARAMS
n = 0.9320
A = -53.5399
# MYHAL_RM370 PARAMS
# n = 0.3387
# A =  -67.2842
# NSCI CR PARAMS
#n = 1.4267
#A = -59.0636

def compute_rssi(distance):
    return -10*n*np.log(distance) + A

def compute_distance(measurements, anchors):
    """Computes the distance of a point from the corresponding anchor of a measurement
    """
    rssi = np.array([m.rssi for m in measurements])
    distance = np.exp((A-rssi)/(10*n))
    return distance

def compute_position(measurements, anchors):
    """
    Parameters:
    measurements - array - array of measurements
    anchors - map - anchors
    """
    distances = compute_distance(measurements, anchors)
    anchorX = np.zeros(len(measurements))
    anchorY = np.zeros(len(measurements))
    for i in range(0, len(measurements)):
        anchorX[i] = anchors[measurements[i].anchorId].X
        anchorY[i] = anchors[measurements[i].anchorId].Y 
    def lossfct(x):
        return distances**2 - (x[0]-anchorX)**2 - (x[1]-anchorY)**2
    x0 = np.array([0,0])
    return scipy.optimize.least_squares(lossfct, x0).x