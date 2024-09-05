from colors import *
from config import *
from face import Face
import math
import pygame
from rotation import rotationMatrix
import util
from vector import Vector3

class Object():
    faces = []
    vertices = []
    # default origin to 0,0,0
    origin = Vector3(0, 0, 0)
    # just used to calculate rotations
    current = 1
    # light faces right down and back
    light = Vector3(-1, -1, 1).normalize()
    
    def __init__(self, filepath):
        # read config
        f = open(filepath, "r")

        # faces depend on other obejcts so we make a temp faces list so that ordering doesn't matter in the file
        tempFaces = []
        colors = []
        
        # read each line
        for x in f:
            # start by finding first list (since all lines have at least one list)
            start = x.find("[")
            end = x.find("]")
            # vertex line
            if x[0] == "v":
                # parse list
                temp = util.parseFloatList(x[start:end + 1])
                # convert to Vertex object
                self.vertices.append(util.listToVertex(temp))
            # face line
            elif x[0] == "f":
                # create dictionary with just index values
                tempFaces.append({
                    "color": int(x[1]),
                    "vertices": util.parseIntList(x[start:end + 1]),
                    # this parses the second list
                    "normal": util.parseFloatList(x[end + 1:][:x[end + 1:].find("]") + 1])
                })
            # origin line
            elif x[0] == "o":
                # parse list
                temp = util.parseFloatList(x[start:end + 1])
                # convert to vector
                self.origin = util.listToVector(temp)
            # color line
            elif x[0] == "c":
                # parse list
                temp = util.parseIntList(x[start:end + 1])
                # construct color object
                colors.append(pygame.Color(temp[0], temp[1], temp[2])) 

        # now that all objects are created we can process faces
        for f in tempFaces:
            self.faces.append(Face(colors[f["color"]], [self.vertices[v] for v in f["vertices"]], Vector3(f["normal"][0], f["normal"][1], f["normal"][2])))
    
    def draw(self, surface):
        # we want to draw faces starting from the back
        # this method of using the average z isn't perfect but works on simple shapes
        sortedZ = sorted(self.faces, key=lambda x: x.avgZ, reverse=True)

        # draw each face in order
        for f in sortedZ:
            f.draw(surface, self.light)

    def update(self):
        # this creates seemingly random but smooth rotations
        self.current += 1
        rotation = Vector3(math.cos(self.current * 0.01) * 0.05, math.cos(self.current * 0.02 + math.pi) * 0.05, math.sin(self.current * 0.03) * 0.05)

        # generate rotation matrix
        rotate = rotationMatrix(rotation.x, rotation.y, rotation.z)

        # transform every vertex
        for v in self.vertices:
            v.transform(rotate, self.origin)

        # transform all the normals
        for f in self.faces:
            f.normal.transform(rotate, Vector3(0,0,0))
            # we can also update faces
            f.update(rotation)