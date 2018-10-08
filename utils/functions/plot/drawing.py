import math
import numpy as np
from utils.functions.math.coordinate_trans import coordinate_transformation_in_angle

def circle_make(center_x, center_y, radius):
    '''
    Create circle matrix(2D)

    Parameters
    -------
    center_x : float in meters
        the center position of the circle coordinate x
    center_y : float in meters
        the center position of the circle coordinate y
    radius : float in meters

    Returns
    -------
    circle x : numpy.ndarray
    circle y : numpy.ndarray
    '''

    point_num = 100 

    circle_xs = []
    circle_ys = []

    for i in range(point_num + 1):
        circle_xs.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_ys.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    return np.array(circle_xs), np.array(circle_ys)

def circle_make_with_angles(center_x, center_y, radius, angle):
    '''
    Create circle matrix with angle line matrix(2D)
    
    Parameters
    -------
    center_x : float in meters
        the center position of the circle coordinate x
    center_y : float in meters
        the center position of the circle coordinate y
    radius : float in meters
    angle : float in radians
    
    Returns
    -------
    circle xs : numpy.ndarray
    circle ys : numpy.ndarray
    angle line xs : numpy.ndarray
    angle line ys : numpy.ndarray
    '''

    point_num = 100 

    circle_xs = []
    circle_ys = []

    for i in range(point_num + 1):
        circle_xs.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_ys.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    angle_line_xs = [center_x, center_x + math.cos(angle) * radius]
    angle_line_ys = [center_y, center_y + math.sin(angle) * radius]

    return np.array(circle_xs), np.array(circle_ys), np.array(angle_line_xs), np.array(angle_line_ys)

def square_make_with_angles(center_x, center_y, size, angle):
    '''
    Create square matrix with angle line matrix(2D)
    
    Parameters
    -------
    center_x : float in meters
        the center x position of the square
    center_y : float in meters
        the center y position of the square
    size : float in meters
        the square's half-size
    angle : float in radians

    Returns
    -------
    square xs : numpy.ndarray
        lenght is 5 (counterclockwise from right-up)
    square ys : numpy.ndarray
        length is 5 (counterclockwise from right-up)
    angle line xs : numpy.ndarray
    angle line ys : numpy.ndarray
    '''

    # start with the up right points
    # create point in counterclockwise
    square_xys = np.array([[size, size], [-size, size], [-size, -size], [size, -size], [size, size]])
    trans_points = coordinate_transformation_in_angle(square_xys.T, -angle) # this is inverse type
    trans_points += np.array([[center_x], [center_y]])

    square_xs = trans_points[0, :]
    square_ys = trans_points[1, :]

    angle_line_xs = [center_x, center_x + math.cos(angle) * size]
    angle_line_ys = [center_y, center_y + math.sin(angle) * size]

    return square_xs, square_ys, np.array(angle_line_xs), np.array(angle_line_ys)