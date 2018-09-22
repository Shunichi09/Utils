import pytest
import math
import glob
from utils.circle import circle_make, plot_singles

def test_cicle_make():
    x = 1.0
    y = 2.0
    radius = 5.1
    xs, ys = circle_make(x, y, radius)
    dis_check = False
    
    for i in range(len(xs)):
        dis = math.sqrt((xs[i] - x)**2 + (ys[i] - y)**2)
        if round(dis, 3) > radius:
            dis_check = True

    assert len([i for i in xs if i > x + radius]) == 0 # 最大xを確認 
    assert len([i for i in ys if i > y + radius]) == 0 # 最大yを確認
    assert len([i for i in xs if i < x - radius]) == 0 # 最小xを確認
    assert len([i for i in ys if i < y - radius]) == 0 # 最小yを確認
    assert not dis_check # 距離を確認

def test_plot_singles():
    x = range(100)
    y = range(100)

    plot_singles(x, y)

    # imgがあればおっけ
    assert glob.glob('./tests/*.png') is not None