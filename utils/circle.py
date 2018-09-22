import numpy as np
import matplotlib.pyplot as plt
import math

def circle_make(center_x, center_y, radius):
    '''
    :param center_x 円の中心x座標
    :param center_y 円の中心y座標
    :param size 円の半径
    '''
    point_num = 100 # 分解能

    circle_x = []
    circle_y = []

    for i in range(point_num + 1):
        circle_x.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_y.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    return circle_x, circle_y

def plot_singles(x, y):
    '''
    :param x プロットするもののx成分
    :param y プロットするもののy成分
    '''
    fig = plt.figure()
    axis = fig.add_subplot(111)

    axis.plot(x, y)

    plt.savefig('sample.png')

if __name__ == '__main__':
    x = 1.0
    y = 1.0
    radius = 1.0

    xs, ys = circle_make(x, y, radius)
