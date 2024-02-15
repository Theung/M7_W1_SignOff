import pygame

class Paddle:
    def __init__(self, x, y, width, height, color, screen_width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen_width = screen_width

    def move(self, direction):
        if direction == "LEFT":
            self.x -= 5
        elif direction == "RIGHT":
            self.x += 5
        # Bound the paddle within the screen width
        self.x = max(0, min(self.x, self.screen_width - self.width))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
