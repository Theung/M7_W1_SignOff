import pygame
import sys
from ball import Ball
from paddle import Paddle
from brick import Brick

# Constants (unchanged)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_RADIUS = 10
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_COLOR = (255, 0, 0)
FPS = 60

# Function to handle events (unchanged)
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Function to update game state (unchanged except for passing keys)
def update_game_state(paddle, ball, bricks):
    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    paddle.move(keys)  # Pass the keys to the move method of the paddle
    ball.move()
    ball.check_boundary_collision()
    ball.check_paddle_collision(paddle)
    if ball.check_brick_collision(bricks):
        return True
    if ball.y - ball.radius >= SCREEN_HEIGHT:
        return False
    return True

# Function to draw objects (unchanged)
def draw_objects(screen, paddle, ball, bricks):
    screen.fill(BLACK)
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout")
    clock = pygame.time.Clock()
    paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT, BLUE, SCREEN_WIDTH)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, WHITE, SCREEN_WIDTH)
    bricks = []
    for i in range(BRICK_ROWS):
        for j in range(BRICK_COLS):
            brick = Brick(j * BRICK_WIDTH, i * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR)
            bricks.append(brick)

    running = True
    while running:
        handle_events()
        running = update_game_state(paddle, ball, bricks)
        draw_objects(screen, paddle, ball, bricks)
        clock.tick(FPS)

    font = pygame.font.SysFont(None, 64)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
