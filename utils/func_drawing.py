import math
import numpy as np

def circle_make(center_x, center_y, radius):
    '''
    Create circle matrix

    Parameters
    -------
    center_x : float
        the center x position of the circle
    center_y : float
        the center y position of the circle
    radius : float

    Returns
    -------
    circle x : numpy.ndarray
    circle y : numpy.ndarray
    '''

    point_num = 100 # 分解能

    circle_xs = []
    circle_ys = []

    for i in range(point_num + 1):
        circle_xs.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_ys.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    return np.array(circle_xs), np.array(circle_ys)

def circle_make_with_angles(center_x, center_y, radius, angle):
    '''
    Create circle matrix with angle line matrix
    
    Parameters
    -------
    center_x : float
        the center x position of the circle
    center_y : float
        the center y position of the circle
    radius : float
    angle : float [rad]
    
    Returns
    -------
    circle xs : numpy.ndarray
    circle ys : numpy.ndarray
    angle line xs : numpy.ndarray
    angle line ys : numpy.ndarray
    '''

    point_num = 100 # 分解能

    circle_xs = []
    circle_ys = []

    for i in range(point_num + 1):
        circle_xs.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_ys.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    angle_line_xs = [center_x, center_x + math.cos(angle) * radius]
    angle_line_ys = [center_y, center_y + math.sin(angle) * radius]

    return np.array(circle_xs), np.array(circle_ys), np.array(angle_line_xs), np.array(angle_line_ys)