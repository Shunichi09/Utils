import math

class TwoWheeledRobot():
    """
    Robot class of Two_wheeled robot model

    Attributes
    ----------
    x : float in meters
        now position x
    y : float in meters
        now position y 
    th : float in radians
        now position th
    history_x : list of float
        time history position x 
    history_y : list of float
        time history position y
    history_th : list of float 
        time history th
    max_acceleration : float in [m/s^2]
    min_acceleration : float in [m/s^2]
    max_ang_acceleration : float in [rad/s^2]
    min_ang_acceleration : float in [rad/s^2]
    max_velo : float in [m/s]
    min_velo : float in [m/s]
    max_ang_velo : float in [rad/s]
    min_ang_velo : float in [rad/s]
    """

    def __init__(self, init_x, init_y, init_th, 
                max_acceleration=1.0, min_acceleration=-1.0, max_ang_acceleration=1.75, min_ang_acceleration=-1.75, 
                max_velo=1.5, min_velo=-1.5, max_ang_velo=math.pi, min_ang_velo=-math.pi):
        """
        Parameters
        -----------
        init_x : float in meters
            initial position x
        init_y : float in meters
            initial position y 
        init_th : float in radians
            initial position th
        max_acceleration : float in [m/s^2], optional
            default is 1.0
        min_acceleration : float in [m/s^2], optional
            default is -1.0
        max_ang_acceleration : float in [rad/s^2], optional
            default is 1.75 (100 deg/s^2)
        min_ang_acceleration : float in [rad/s^2], optional
            default is -1.75 (100 deg/s^2)
        max_velo : float in [m/s], optional
            default is 1.5 
        min_velo : float in [m/s], optional
            default is -1.5
        max_ang_velo : float in [rad/s], optional
            default is math.pi
        min_ang_velo : float in [rad/s], optional
            default is -math.pi
        """
        # initial state
        self.x = init_x
        self.y = init_y
        self.th = init_th
        self.u_v = 0.0
        self.u_th = 0.0

        # save time history
        self.history_x = [init_x]
        self.history_y = [init_y]
        self.history_th = [init_th]
        self.history_u_v = [0.0]
        self.history_u_th = [0.0]

        # accelalation limit of robot
        self.max_acceleration = max_acceleration
        self.min_acceleration = min_acceleration
        self.max_ang_acceleration= max_ang_acceleration
        self.min_ang_acceleration= min_ang_acceleration
        # velocity limit of robot
        self.max_velo = max_velo # m/s
        self.min_velo = min_velo # m/s
        self.max_ang_velo = max_ang_velo # rad/s
        self.min_ang_velo = min_ang_velo # rad/s

    def update_state(self, u_v, u_th, dt=0.01): # stateを更新
        """ Update the state of robot

        Parameter
        ----------
        u_v : float in [m/s]
            t time of velocity input 
        u_th : float in [rad/s]
            t time of angular velocity input
        dt : float in seconds, optional
            sampling time, default is 0.01 [s]

        Return
        ----------
        x : float [m]
            now position x
        y : float [m]
            now position y
        th : float [rad]
            now angle th
        """
        # checking the speed of input
        u_v, u_th = self._check_input(u_v, u_th, dt)

        # update the state
        next_x = u_v * math.cos(self.th) * dt + self.x
        next_y = u_v * math.sin(self.th) * dt + self.y
        next_th = u_th * dt + self.th

        self.history_x.append(next_x)
        self.history_y.append(next_y)
        self.history_th.append(next_th)
        self.history_u_v.append(u_v)
        self.history_u_th.append(u_th)

        self.x = next_x
        self.y = next_y
        self.th = next_th

        return self.x, self.y, self.th # stateを更新
    
    def _check_input(self, u_v, u_th, dt):
        """ Check the speed range

        Parameter
        ----------
        u_th : float in [rad/s]
            t time of angular velocity input
        u_v : float in [m/s]
            t time of velocity input 
        dt : float in seconds
            sampling time
        
        Return
        ----------
        correct_u_v : float in [m/s]
            possible velocity inputs
        correct_u_th : float [rad/s]
            possible angular velocity inputs
        """

        # checking the speed
        if u_v > self.max_velo:
            u_v = self.max_velo
        
        if u_v < self.min_velo:
            u_v = self.min_velo
        
        if u_th > self.max_ang_velo:
            u_th = self.max_ang_velo

        if u_th < self.min_ang_velo:
            u_th = self.min_ang_velo
        
        acceleration = (u_v - self.u_v) / dt
        ang_acceleration = (u_th - self.u_th) / dt
        
        if acceleration > self.max_acceleration:
            u_v = self.u_v + self.max_acceleration * dt
        
        if acceleration < self.min_acceleration:
            u_v = self.u_v + self.min_acceleration * dt
        
        if ang_acceleration > self.max_ang_acceleration:
            u_th = self.u_th + self.max_ang_acceleration * dt
        
        if ang_acceleration < self.min_ang_acceleration:
            u_th = self.u_th + self.min_ang_acceleration * dt
        
        return u_v, u_th

class OmniWheeledRobot():
    """
    Robot class of Omni_wheeled robot model

    Attributes
    ----------
    x : float in meters
        now position x
    y : float in meters
        now position y 
    th : float in radians
        now position th
    history_x : list of float
        time history position x 
    history_y : list of float
        time history position y
    history_th : list of float 
        time history th
    max_x_acceleration : float in [m/s^2]
    min_x_acceleration : float in [m/s^2]
    max_y_acceleration : float in [m/s^2]
    min_y_acceleration : float in [m/s^2]
    max_ang_acceleration : float in [rad/s^2]
    min_ang_acceleration : float in [rad/s^2]
    max_velo : float in [m/s]
    min_velo : float in [m/s]
    max_ang_velo : float in [rad/s]
    min_ang_velo : float in [rad/s]
    """

    def __init__(self, init_x, init_y, init_th, 
                max_x_acceleration=1.0, min_x_acceleration=-1.0, max_y_acceleration=1.0, min_y_acceleration=-1.0,
                max_ang_acceleration=1.75, min_ang_acceleration=-1.75, 
                max_x_velo=1.5, min_x_velo=-1.5, 
                max_y_velo=1.5, min_y_velo=-1.5, 
                max_ang_velo=math.pi, min_ang_velo=-math.pi):
        """
        Parameters
        -----------
        init_x : float in meters
            initial position x
        init_y : float in meters
            initial position y 
        init_th : float in radians
            initial position th
        max_x_acceleration : float in [m/s^2], optional
            default is 1.0
        min_x_acceleration : float in [m/s^2], optional
            default is -1.0
        max_y_acceleration : float in [m/s^2], optional
            default is 1.0
        min_y_acceleration : float in [m/s^2], optional
            default is -1.0
        max_ang_acceleration : float in [rad/s^2], optional
            default is 1.75 (100 deg/s^2)
        min_ang_acceleration : float in [rad/s^2], optional
            default is 1.75 (100 deg/s^2)
        max_velo : float in [m/s], optional
            default is 1.5 
        min_velo : float in [m/s], optional
            default is -1.5
        max_ang_velo : float in [rad/s], optional
            default is math.pi
        min_ang_velo : float in [rad/s], optional
            default is -math.pi
        """
        # initial state
        self.x = init_x
        self.y = init_y
        self.th = init_th
        self.u_v_x = 0.0
        self.u_v_y = 0.0
        self.u_th = 0.0

        # save time history
        self.history_x = [init_x]
        self.history_y = [init_y]
        self.history_th = [init_th]
        self.history_u_v_x = [0.0]
        self.history_u_v_y = [0.0]
        self.history_u_th = [0.0]

        # accelalation limit of robot
        self.max_x_acceleration = max_x_acceleration
        self.min_x_acceleration = min_x_acceleration
        self.max_y_acceleration = max_y_acceleration
        self.min_y_acceleration = min_y_acceleration
        self.max_ang_acceleration = max_ang_acceleration
        self.min_ang_acceleration = min_ang_acceleration
        # velocity limit of robot
        self.max_x_velo = max_x_velo # m/s
        self.min_x_velo = min_x_velo # m/s
        self.max_y_velo = max_y_velo # m/s
        self.min_y_velo = min_y_velo # m/s
        self.max_ang_velo = max_ang_velo # rad/s
        self.min_ang_velo = min_ang_velo # rad/s

    def update_state(self, u_v_x, u_v_y, u_th, dt=0.01):
        """ Update the state of robot

        Parameter
        ----------
        u_v_x : float in [m/s]
            t time of velocity input
        u_v_y : float in [m/s]
            t time of velocity input 
        u_th : float in [rad/s]
            t time of angular velocity input
        dt : float in seconds, optional
            sampling time, default is 0.01 [s]

        Return
        ----------
        x : float [m]
            now position x
        y : float [m]
            now position y
        th : float [rad]
            now angle th
        """
        # checking the speed of input
        u_v_x, u_v_y, u_th = self._check_input(u_v_x, u_v_y, u_th, dt)

        # update the state
        next_x = u_v_x * dt + self.x
        next_y = u_v_y * dt + self.y
        next_th = u_th * dt + self.th

        self.history_x.append(next_x)
        self.history_y.append(next_y)
        self.history_th.append(next_th)
        self.history_u_v_x.append(u_v_x)
        self.history_u_v_y.append(u_v_y)
        self.history_u_th.append(u_th)

        self.x = next_x
        self.y = next_y
        self.th = next_th

        return self.x, self.y, self.th # stateを更新
    
    def _check_input(self, u_v_x, u_v_y, u_th, dt):
        """ Check the speed range

        Parameter
        ----------
        u_v_x : float in [m/s]
            t time of velocity input
        u_v_y : float in [m/s]
            t time of velocity input 
        u_th : float in [rad/s]
            t time of angular velocity input
        dt : float in seconds, optional
            sampling time, default is 0.01 [s]
        
        Return
        ----------
        correct_u_v_x : float in [m/s]
            possible velocity inputs
        correct_u_v_y : float in [m/s]
            possible velocity inputs
        correct_u_th : float [rad/s]
            possible angular velocity inputs
        """

        # checking the speed
        if u_v_x > self.max_x_velo:
            u_v_x = self.max_x_velo
        
        if u_v_x < self.min_x_velo:
            u_v_x = self.min_x_velo
        
        if u_v_y > self.max_y_velo:
            u_v_y = self.max_y_velo
        
        if u_v_y < self.min_y_velo:
            u_v_y = self.min_y_velo
        
        if u_th > self.max_ang_velo:
            u_th = self.max_ang_velo

        if u_th < self.min_ang_velo:
            u_th = self.min_ang_velo
        
        acceleration_x = (u_v_x - self.u_v_x) / dt
        acceleration_y = (u_v_y - self.u_v_y) / dt
        ang_acceleration = (u_th - self.u_th) / dt
        
        if acceleration_x > self.max_x_acceleration:
            u_v_x = self.u_v_x + self.max_x_acceleration * dt
        
        if acceleration_x < self.min_x_acceleration:
            u_v_x = self.u_v_x + self.min_x_acceleration * dt
        
        if acceleration_y > self.max_y_acceleration:
            u_v_y = self.u_v_y + self.max_y_acceleration * dt
        
        if acceleration_y < self.min_y_acceleration:
            u_v_y = self.u_v_y + self.min_y_acceleration * dt

        if ang_acceleration > self.max_ang_acceleration:
            u_th = self.u_th + self.max_ang_acceleration * dt
        
        if ang_acceleration < self.min_ang_acceleration:
            u_th = self.u_th + self.min_ang_acceleration * dt
        
        return u_v_x, u_v_y, u_th