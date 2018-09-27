import math
import numpy as np

def rad_to_deg(rad_angle):
    '''
    Translate rad to deg

    Parameters
    -------
    angle : float or numpy.ndarray [rad]
    
    Returns
    -------
    deg_angle : float or numpy.ndarray [deg]
    '''

    deg_angle = 180.0 * rad_angle / math.pi

    return deg_angle

def deg_to_rad(deg_angle):
    '''
    Translate deg to radian

    Parameters
    -------
    angle : float or numpy.ndarray [deg]
        unit is radians
    Returns
    -------
    rad_angle : float or numpy.ndarray [rad]
        correct range angle
    '''
    rad_angle = math.pi * deg_angle / 180.0

    return rad_angle

def angle_range_corrector(angle, MAX=math.pi, MIN=-math.pi):
    '''
    Check angle range and correct the range

    Parameters
    -------
    angle : numpy.ndarray
        unit is radians
    MAX : float
        maximum of range [rad] , default math.pi
    MIN : float
        minimum of range [rad], default -math.pi
    Returns
    -------
    correct_angle : numpy.ndarray
        correct range angle
    '''
    correct_angle = np.empty_like(angle)

    for i in range(len(angle)):
        if correct_angle[i] > MAX:
            while correct_angle[i] > MAX:
                correct_angle[i] -=  2 * math.pi
        elif correct_angle[i] < MIN:
            while correct_angle[i] < MIN:
                correct_angle[i] +=  2 * math.pi
    
    return correct_angle
