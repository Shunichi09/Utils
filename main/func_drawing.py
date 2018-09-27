import math

def circle_make(center_x, center_y, radius):
    '''
    Create circle matrix
    Parameters
    -------
    center_x : float
        円の中心x座標
    center_y : float
        円の中心y座標
    radius : float
        円の半径

    Returns
    -------
    circle x : numpy.ndarray
        円のx座標群
    circle y : numpy.ndarray
        円のy座標群
    '''

    point_num = 100 # 分解能

    circle_x = []
    circle_y = []

    for i in range(point_num + 1):
        circle_x.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_y.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    return circle_x, circle_y

def circle_make_with_angles(center_x, center_y, angle, radius):
    '''
    Create circle matrix with angle lines
    Parameters
    -------
    center_x : float
        円の中心x座標
    center_y : float
        円の中心y座標
    radius : float
        円の半径
    angle : float
        傾き，向き

    Returns
    -------
    circle x : numpy.ndarray
        円のx座標群
    circle y : numpy.ndarray
        円のy座標群
    angle_line x : numpy.ndarray
        円の傾きのx座標群
    angle_line y : numpy.ndarray
        円の傾きのy座標群
    '''

    point_num = 100 # 分解能

    circle_x = []
    circle_y = []

    for i in range(point_num + 1):
        circle_x.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_y.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    angle_line_x = [center_x, center_x + math.cos(angle) * radius]
    angle_line_y = [center_y, center_y + math.sin(angle) * radius]

    return circle_x, circle_y, angle_line_x, angle_line_y