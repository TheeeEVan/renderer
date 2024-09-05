import pygame


class Face():
    def __init__(self, color, vertices, normal):
        self.color = color
        self.vertices = vertices
        self.normal = normal
        
    def update(self, rotation):
        # store each projection in a list
        self.projections = [v.project() for v in self.vertices]

        # calculate average z of face for z-buffer
        self.avgZ = sum([v.z for v in self.projections]) / len(self.projections)

    # returns current brightness of face
    def getLightness(self, light):
        return self.normal.dot(light)

    # draws face on screen
    def draw(self, surface, light):
        lightness = self.getLightness(light)
        
        # clamp lightness so faces dont disappear
        lightness = max(0.2, lightness)
        
        # convert projection coords to [0, surface_width]
        positions = [((proj.x + 1) * surface.get_width()/2, (proj.y + 1) * surface.get_height()/2) for proj in self.projections]

        # adjust color to match lightness
        adjustedColor = pygame.Color(round(self.color.r * lightness), round(self.color.g * lightness), round(self.color.b * lightness))

        # draw a polygon based on last projection
        pygame.draw.polygon(surface, adjustedColor, [(coord[0], coord[1]) for coord in positions])