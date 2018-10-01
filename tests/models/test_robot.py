import pytest
import math

from utils.models.robot import TwoWheeledRobot, OmniWheeledRobot

class TestRobot(object):
    def test_TwoWheeleRobot_initial_conditions(self):
        robot = TwoWheeledRobot(0.5, -0.5, 1.1)

        assert robot.x == 0.5
        assert robot.y == -0.5
        assert robot.th == 1.1
        assert robot.max_acceleration == 1.0
        assert robot.min_acceleration == -1.0
        assert robot.max_ang_acceleration == 1.75
        assert robot.min_ang_acceleration == -1.75
        assert robot.max_velo == 1.5
        assert robot.min_velo == -1.5
        assert robot.max_ang_velo == math.pi
        assert robot.min_ang_velo == -math.pi

    def test_OmniWheeledRobot_initial_conditions(self):
        robot = OmniWheeledRobot(0.5, -0.5, 1.1)

        assert robot.x == 0.5
        assert robot.y == -0.5
        assert robot.th == 1.1
        assert robot.max_x_acceleration == 1.0
        assert robot.min_x_acceleration == -1.0
        assert robot.max_y_acceleration == 1.0
        assert robot.min_y_acceleration == -1.0
        assert robot.max_ang_acceleration == 1.75
        assert robot.min_ang_acceleration == -1.75
        assert robot.max_x_velo == 1.5
        assert robot.min_x_velo == -1.5
        assert robot.max_y_velo == 1.5
        assert robot.min_y_velo == -1.5
        assert robot.max_ang_velo == math.pi
        assert robot.min_ang_velo == -math.pi
    
    def test_TwoWheeleRobot_update_conditions(self):
        robot = TwoWheeledRobot(0.5, -0.5, 1.1)

        robot.update_state(1.0, 1.0, dt=1.0)

        assert round(robot.x, 5) == round(1.0 * math.cos(1.1) + 0.5, 5)
        assert round(robot.y, 5) == round(1.0 * math.sin(1.1) + -0.5, 5)
        assert robot.th == 2.1
    
    def test_TwoWheeleRobot_update_conditions_with_overlimit_inputs(self):
        robot = TwoWheeledRobot(0.5, -0.5, 1.1)

        robot.update_state(1.0, 1.0)

        assert round(robot.x, 5) == round(1.0 * 0.01 * math.cos(1.1) + 0.5, 5)
        assert round(robot.y, 5) == round(1.0 * 0.01 * math.sin(1.1) - 0.5, 5)
        assert robot.th == 1.1 + 1.75 * 0.01

    def test_OmniWheeleRobot_update_conditions(self):
        robot = OmniWheeledRobot(0.5, -0.5, 1.1)

        robot.update_state(1.0, 1.0, 1.0, dt=1.0)

        assert round(robot.x, 5) == round(1.0 + 0.5, 5)
        assert round(robot.y, 5) == round(1.0 - 0.5, 5)
        assert robot.th == 1.1

    def test_OmniWheeleRobot_update_conditions_with_overlimit_inputs(self):
        robot = OmniWheeledRobot(0.5, -0.5, 1.1)

        robot.update_state(1.0, 1.0, 1.0)

        assert round(robot.x, 5) == round(1.0 * 0.01 + 0.5, 5)
        assert round(robot.y, 5) == round(1.0 * 0.01 - 0.5, 5)
        assert robot.th == 1.1 + 1.75 * 0.01







