import math
import numpy as np
import copy

def coordinate_transformation_in_angle(positions, base_angle):
    '''
    Transformation the coordinate in the angle

    Parameters
    -------
    positions : numpy.ndarray
        this parameter is composed of xs, ys 
        should have (2, N) shape 
    base_angle : float in radians
    
    Returns
    -------
    traslated_positions : numpy.ndarray
        the shape is (2, N)
    
    '''

    positions = positions.reshape(2, -1)

    rot_matrix = [[np.cos(base_angle), np.sin(base_angle)],
                  [-1*np.sin(base_angle), np.cos(base_angle)]]

    rot_matrix = np.array(rot_matrix)
    
    translated_positions = np.dot(rot_matrix, positions)

    return translated_positions

def coordinate_transformation_in_position(positions, base_positions):
    '''
    Transformation the coordinate in the positions

    Parameters
    -------
    positions : numpy.ndarray
        this parameter is composed of xs, ys 
        should have (2, N) shape 
    base_positions : numpy.ndarray
        this parameter is composed of x, y
        shoulg have (2, 1) shape
    
    Returns
    -------
    traslated_positions : numpy.ndarray
    
    '''

    positions = positions.reshape(2, -1)
    base_positions = base_positions.reshape(2, 1)

    translated_positions = positions - base_positions

    return translated_positions

# def coordinate_inv_transformation
if __name__ == '__main__':
    positions_1 = np.array([[1.0], [2.0]])
    base_angle = 1.25

    translated_positions_1 = coordinate_transformation_in_angle(positions_1, base_angle)
    print(translated_positions_1)
