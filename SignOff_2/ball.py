import random
import pygame
class Ball:
    def __init__(self, x, y, radius, color, screen_width):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.choice([-2, 2])
        self.vy = -2
        self.screen_width = screen_width
        self.prev_positions = []

    #sets the ball in motion
    def move(self):
        self.prev_positions.append((self.x, self.y))
        if len(self.prev_positions) > 10:
            self.prev_positions.pop(0)

        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        # Draw afterimages
        for i, (x, y) in enumerate(self.prev_positions[::-1]):
            alpha = int(200 - i * (200 / len(self.prev_positions)))  # Adjust alpha for transparency
            pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2], alpha), (x, y), self.radius - i)

        # Draw current ball
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    #checks if ball collides with borders
    def check_boundary_collision(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen_width:
            self.vx *= -1
        if self.y - self.radius <= 0:
            self.vy *= -1

    #checks if ball collides with paddle
    def check_paddle_collision(self, paddle):
        if self.y + self.radius >= paddle.y and self.x >= paddle.x and self.x <= paddle.x + paddle.width:
            self.vy *= -1

    #checks wether ball collides with brick
    def check_brick_collision(self, bricks):
        for brick in bricks:
            if self.y - self.radius <= brick.y + brick.height and self.x >= brick.x and self.x <= brick.x + brick.width:
                self.vy *= -1
                bricks.remove(brick)
                return True
        return False