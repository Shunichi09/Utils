import pytest
import numpy as np
import math
import os, sys
import random

from utils.functions.math.angle import deg_to_rad, rad_to_deg, fit_angle_in_range

class TestAngle(object):
    def test_deg_to_rad(self):
        assert np.round(deg_to_rad(np.array([90.0])), 5) == np.array([round(math.pi * 0.5, 5)])
        assert round(deg_to_rad(70.0), 5) == 1.22173
        assert round(deg_to_rad(240.0), 5) == 4.18879
        assert round(deg_to_rad(70), 5) == 1.22173

    def test_rad_to_deg(self):
        assert np.round(rad_to_deg(np.array([math.pi * 0.5])), 5) == np.array([90.0])
        assert round(rad_to_deg(1.22173), 3) == 70.0
        assert round(rad_to_deg(4.18879), 3) == 240.0

    def test_fit_angle_in_range_scalar(self):
        angles = np.random.rand(10) + 3.0
        test_pass = True
        correct_angles = fit_angle_in_range(angles)

        for i, angle in enumerate(correct_angles):
            if angle < 0.0:
                assert False
            elif angle > 2 * math.pi:
                assert False
            elif round(math.cos(float(angle)), 5) != round(math.cos(angles[i]), 5):
                assert False
            elif round(math.sin(float(angle)), 5) != round(math.sin(angles[i]), 5):
                assert False

    def test_fit_angle_in_range_matrix(self):
        angles = np.random.rand(1, 10) + 3.0
        correct_angles = fit_angle_in_range(angles)

        for i, angle in enumerate(correct_angles[0]):
            if angle < 0.0:
                assert False
            elif angle > 2 * math.pi:
                assert False
            elif round(math.cos(float(angle)), 5) != round(math.cos(angles[0, i]), 5):
                assert False
            elif round(math.sin(float(angle)), 5) != round(math.sin(angles[0, i]), 5):
                assert False
        
if __name__ == '__main__':
    pytest.main()