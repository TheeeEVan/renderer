import math
from matrix import Matrix44

# generates a rotation matrix for rotations on given axis (in radians)
def rotationMatrix(x, y, z):
    # https://en.wikipedia.org/wiki/Rotation_matrix#General_3D_rotations
    return Matrix44([
        [math.cos(z) * math.cos(y), math.cos(z) * math.sin(y) * math.sin(x) - math.sin(z) * math.cos(x), math.cos(z) * math.sin(y) * math.cos(x) + math.sin(z) * math.sin(x), 0],
        [math.sin(z) * math.cos(y), math.sin(z) * math.sin(y) * math.sin(x) + math.cos(z) * math.cos(x), math.sin(z) * math.sin(y) * math.cos(x) - math.cos(z) * math.sin(x), 0],
        [-math.sin(y), math.cos(y) * math.sin(x), math.cos(y) * math.cos(x), 0],
        [0, 0, 0, 1]
    ])