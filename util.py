# just a lot of conversions 

from vector import Vector3
from vertex import Vertex

def parseIntList(str):
    if str[0] != "[" or str[-1] != "]":
        raise ValueError("Can't parse non list")

    temp = str[1:-1].split(",")

    return [int(x.strip()) for x in temp]

def parseFloatList(str):
    if str[0] != "[" or str[-1] != "]":
        raise ValueError("Can't parse non list")

    temp = str[1:-1].split(",")

    return [float(x.strip()) for x in temp]

def listToVector(a):
    if len(a) != 3:
        raise ValueError("List must have length of 3")
    return Vector3(a[0], a[1], a[2])

def listToVertex(a):
    if len(a) != 3:
        raise ValueError("List must have length of 3")
    return Vertex(a[0], a[1], a[2])
