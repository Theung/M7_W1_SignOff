import pygame

class Brick:
    #class the drag brick and sets it parameters
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.x + 1, self.y + 1, self.width - 2, self.height - 2))
