# class for a 4x4 matrix
class Matrix44():
    # default to identity matrix
    matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    
    def __init__(self, matrix = None):
        if matrix != None:
            self.matrix = matrix

    # [] access operator
    def __getitem__(self, key):
        return self.matrix[key]

    # multiply two matricies
    def __mul__(self, other):
        # this will store result
        matr = []
        
        for i in range(4):
            matr.append([])
            for j in range(4):
                matr[i].append(0)
                for k in range(4):
                    matr[i][j] += self[i][k] * other[k][j]

        # construct new matrix based on result
        return Matrix44(matr)