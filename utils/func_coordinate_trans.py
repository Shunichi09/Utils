import math
import numpy as np
import copy 

def coordinate_transformation_in_angle(base_angle):
    '''
    Translate the coordinate in the angle

    Parameters
    -------
    angle : float [rad]
    
    Returns

    -------
    
    '''

    deg_angle = 180.0 * base_angle / math.pi

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
