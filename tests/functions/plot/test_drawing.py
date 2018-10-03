import pytest
import numpy as np
import math

from utils.functions.plot.drawing import circle_make, circle_make_with_angles, square_make_with_angles

class TestDrawing(object):
    def test_cicle_make(self):
        x = 1.0
        y = 2.0
        radius = 5.1
        xs, ys = circle_make(x, y, radius)
        dis_check = False

        for i in range(len(xs)):
            dis = math.sqrt((xs[i] - x)**2 + (ys[i] - y)**2)
            if round(dis, 3) != radius:
                dis_check = True

        assert len([i for i in xs if i > x + radius]) == 0 # maximum x
        assert len([i for i in ys if i > y + radius]) == 0 # maximum y
        assert len([i for i in xs if i < x - radius]) == 0 # minimum x
        assert len([i for i in ys if i < y - radius]) == 0 # minimum y
        assert not dis_check # distance checking

    def test_cicle_make_with_angle(self):
        x = 1.0
        y = 2.0
        angle = 2.1
        radius = 5.6
        dis_check_1 = False
        dis_check_2 = False

        xs, ys, angle_xs, angle_ys = circle_make_with_angles(x, y, radius, angle)

        for i in range(xs.shape[0]):
            dis = math.sqrt((xs[i] - x)**2 + (ys[i] - y)**2)
            if round(dis, 3) != radius:
                dis_check = True

        dis = math.sqrt((angle_xs[1] - x)**2 + (angle_ys[1] - y)**2)
        if round(dis, 3) != radius:
            dis_check_2 = True

        assert len([i for i in xs if i > x + radius]) == 0 # maximum x
        assert len([i for i in ys if i > y + radius]) == 0 # maximum y
        assert len([i for i in xs if i < x - radius]) == 0 # minimum x
        assert len([i for i in ys if i < y - radius]) == 0 # minimum y
        assert not dis_check_1 # distance checking
        assert not dis_check_2

    def test_square_make_with_angle(self):
        x = 1.0
        y = 2.0
        angle = 2.0
        size = 1.0

        xs, ys, angle_xs, angle_ys = square_make_with_angles(x, y, size, angle)

        assert xs.shape[0] == 5

        for i in range(xs.shape[0]):
            dis = math.sqrt((xs[i] - x)**2 + (ys[i] - y)**2)
            assert round(dis, 5) == round(math.sqrt(2.0), 5)
            
        assert round(xs[0], 5) == -0.32544
        assert round(ys[0], 5) == 2.49315
        assert round(xs[1], 5) == 0.50685
        assert round(ys[1], 5) == 0.67456
    
if __name__ == '__main__':
    pytest.main()