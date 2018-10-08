import math
import numpy as np
import copy 

def rad_to_deg(rad_angle):
    """
    Translate rad to deg

    Parameters
    -------
    angle : float or numpy.ndarray [rad]
    
    Returns
    -------
    deg_angle : float or numpy.ndarray [deg]
    """

    deg_angle = 180.0 * rad_angle / math.pi

    return deg_angle

def deg_to_rad(deg_angle):
    """
    Translate deg to radian

    Parameters
    -------
    angle : float or numpy.ndarray [deg]
        unit is radians
        
    Returns
    -------
    rad_angle : float or numpy.ndarray [rad]
        correct range angle
    """

    rad_angle = math.pi * deg_angle / 180.0

    return rad_angle

def fit_angle_in_rad_range(angles, min_angle=0.0, max_angle=(2 * math.pi)):
    """
    Check angle range and correct the range

    Parameters
    -------
    angle : array-like
        unit is radians
    min_angle : float 
        maximum of range in radians, default 0.0
    max_angle : float 
        minimum of range in radians, default 2 * math.pi

    Returns
    -------
    correct_angle : numpy.ndarray
        correct range angle in radians
    """

    if max_angle < min_angle:
        raise ValueError('max angle must be greater than min angle')
    if (max_angle - min_angle) < 2.0 * math.pi:
        raise ValueError('difference between max_angle and min_angle must be greater than 2.0 * pi')
    
    output = np.array(angles)
    output_shape = output.shape

    output = output.flatten()
    output -= min_angle
    output %= 2 * math.pi
    output += 2 * math.pi
    output %= 2 * math.pi
    output += min_angle

    output = np.minimum(max_angle, np.maximum(min_angle, output))
    return output.reshape(output_shape)

def fit_angle_in_deg_range(angles, min_angle=0.0, max_angle=(360.0)):
    """
    Check angle range and correct the range

    Parameters
    -------
    angle : array-like
        unit is degrees
    min_angle : float 
        maximum of range in degrees, default 0.0
    max_angle : float 
        minimum of range in degrees, default 360.0

    Returns
    -------
    correct_angle : numpy.ndarray
        correct range angle in degrees
    """

    if max_angle < min_angle:
        raise ValueError("max angle must be greater than min angle")
    if (max_angle - min_angle) < 360.0:
        raise ValueError("difference between max_angle and min_angle must be greater than 360.0")

    output = np.array(angles)
    output_shape = output.shape

    output = output.flatten()
    output -= min_angle
    output %= 360.0
    output += 360.0
    output %= 360.0
    output += min_angle

    output = np.minimum(max_angle, np.maximum(min_angle, output))
    return output.reshape(output_shape)

