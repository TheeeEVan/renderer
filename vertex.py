from config import *
import math
from matrix import Matrix44
from vector import *

class Vertex(Vector3):
    def __init__(self, x, y, z):
        self.FOV = FOV
        super().__init__(x, y, z)
        
    def project(self):
        scale = 1/(math.tan(self.FOV*math.pi/360))
        
        # projection matrix
        # https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/building-basic-perspective-projection-matrix.html
        matrix = Matrix44([
            [scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, -(CLIP_FAR/(CLIP_FAR-CLIP_NEAR)), -1],
            [0, 0 , -(CLIP_FAR*CLIP_NEAR/(CLIP_FAR-CLIP_NEAR)), 0]
        ])

        # multiply by projection matrix and return resulting vector
        return matrMult(self, matrix)

    
        
        
            