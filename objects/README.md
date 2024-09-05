# .pyobj spec

## Color Line
A line that starts with `c` followed by a list of values represents a color. The values represent the red, green, and blue values of the color, respectively. Each color is numbered in the order it appears in the file starting from 0.

### Example
```py
c[255, 0, 0] # color 0 (red)
c[255, 255, 255] # color 1 (white)
```
## Origin Line
A line that starts with `o` followed by a list of values represents the origin of the obejct. The values represent the x, y, and z coordnates of the origin respectively. Generally there is only one of these. If there are multiple the last one is used. The origin is used as the point which the object is rotated on.
### Example
```py
o[2, 5, -3]
```
## Vertex Line
A line that starts with `v` followed by a list of values represents a vertex in the object. The values represent the x, y, and z coordnates of the vertex respectively. These are used to create faces. Each vertex is numbered in the order they appear in the file starting from 0.
### Example
```py
v[1, 1, -3] # vertex 0
v[3, 5, -7] # vertex 1
```

## Face Line
A line that starts with `f` followed by a number and two lists of values represents a face in the object. The first number is the color the face should use. The first list represents the vertices used to construct the face. These vertices will be used in the order they are given to construct a polygon. The second list represents the normal of the face, which should be a normalized vector.
### Example
```py
f1[1, 2, 4, 5][0, 1, 0] # face using color 1; vertices 1, 2, 4, and 5; and facing up
```