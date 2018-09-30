import pytest
import numpy as np
import math
import os, sys
import random

from utils.func_coordinate_trans import coordinate_transformation_in_angle, coordinate_transformation_in_position

def test_coordinate_transformation_in_angle():

    positions_1 = np.array([[1.0], [2.0]])
    base_angle = 1.25

    translated_positions_1 = coordinate_transformation_in_angle(positions_1, base_angle)
    
    positions_2 = np.array([[1.2, 2.4], [0.5, -0.8]])
    base_angle = -2.8

    translated_positions_2 = coordinate_transformation_in_angle(positions_2, base_angle)

    assert round(math.sqrt((positions_1[0, 0])**2 + (positions_1[1, 0])**2), 5) \
            == round(math.sqrt((translated_positions_1[0, 0])**2 + (translated_positions_1[1, 0])**2), 5)
    assert round(math.sqrt((positions_2[0, 0])**2 + (positions_2[1, 0])**2), 5) \
            == round(math.sqrt((translated_positions_2[0, 0])**2 + (translated_positions_2[1, 0])**2), 5)
    assert round(math.sqrt((positions_2[0, 1])**2 + (positions_2[1, 1])**2), 5) \
            == round(math.sqrt((translated_positions_2[0, 1])**2 + (translated_positions_2[1, 1])**2), 5)
    assert round(translated_positions_1[0, 0], 5) == 2.21329
    assert round(translated_positions_1[1, 0], 5) == -0.31834
    assert round(translated_positions_2[0, 0], 5) == -1.29816
    assert round(translated_positions_2[1, 0], 5) == -0.06913
    assert round(translated_positions_2[0, 1], 5) == -1.99334
    assert round(translated_positions_2[1, 1], 5) == 1.55775

def test_coordinate_transformation_in_position():

    positions_1 = np.array([[1.0], [2.0]])
    base_positions = np.array([[1.25], [2.2]])

    translated_positions_1 = coordinate_transformation_in_position(positions_1, base_positions)
    
    positions_2 = np.array([[1.2, 2.4], [0.5, -0.8]])
    base_positions = np.array([[1.25], [-2.5]])

    translated_positions_2 = coordinate_transformation_in_position(positions_2, base_positions)

    assert round(translated_positions_1[0, 0], 5) == -0.25
    assert round(translated_positions_1[1, 0], 5) == -0.2
    assert round(translated_positions_2[0, 0], 5) == -0.05
    assert round(translated_positions_2[1, 0], 5) == 3.0
    assert round(translated_positions_2[0, 1], 5) == 1.15
    assert round(translated_positions_2[1, 1], 5) == 1.7