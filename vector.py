class Vector3():
    # defaults to (0,0,0)
    def __init__(self, x = 0., y = 0., z = 0.):
        self.x = x
        self.y = y
        self.z = z
        # w is simply used for calculations and should always return to 1
        self.w = 1
        
    # returns length of vector
    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

    # returns vector with length 1
    def normalize(self):
        return Vector3(self.x / self.length(), self.y / self.length(), self.z / self.length())

    # adds two vectors
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # subtract two vectors
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # mulitply by a scalar or matrix
    def __mul__(self, c):
        return Vector3(self.x * c, self.y * c, self.z * c)

    # division just muliplys by inverse 
    def __truediv__(self, c):
        return Vector3(self.x / c, self.y / c, self.z / c)
    
    # returns the dot product of two vectors
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # returns cross product of two vectors
    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y, # x
            self.z * other.x - self.x - other.z, # y
            self.x * other.y - self.y * other.x  # z
        )
        
    def transform(self, matrix, origin):
        # convert coords to passed origin
        relativeCoords = Vector3(self.x - origin.x, self.y - origin.y, self.z - origin.z)

        # multiply
        result = matrMult(relativeCoords, matrix)

        # convert back and set coords
        self.x = result.x + origin.x
        self.y = result.y + origin.y
        self.z = result.z + origin.z

def matrMult(vector, matrix):
    # i cannot loop for this one since vectors use x, y, z
    x = vector.x * matrix[0][0] + vector.y * matrix[1][0] + vector.z * matrix[2][0] + vector.w * matrix[3][0]
    y = vector.x * matrix[0][1] + vector.y * matrix[1][1] + vector.z * matrix[2][1] + vector.w * matrix[3][1]
    z = vector.x * matrix[0][2] + vector.y * matrix[1][2] + vector.z * matrix[2][2] + vector.w * matrix[3][2]
    w = vector.x * matrix[0][3] + vector.y * matrix[1][3] + vector.z * matrix[2][3] + vector.w * matrix[3][3]
    # divide each by w to normalize
    return Vector3(x/w, y/w, z/w)