import pygame
import sys
from ball import Ball
from paddle import Paddle
from brick import Brick

# Constants
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

def handle_events():
    """
    Handle pygame events such as quitting the game.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_game_state(paddle, ball, bricks):
    """
    Update the game state based on user input and collision detection.
    """
    # Handle user input for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("LEFT")
    if keys[pygame.K_RIGHT]:
        paddle.move("RIGHT")

    # Move the ball and check for collisions with boundaries, paddle, and bricks
    ball.move()
    ball.check_boundary_collision()
    ball.check_paddle_collision(paddle)
    if ball.check_brick_collision(bricks):
        return True

    # Check for game over condition
    if ball.y - ball.radius >= SCREEN_HEIGHT:
        return False

    return True

def draw_objects(screen, paddle, ball, bricks):
    """
    Draw game objects on the screen.
    """
    # Clear the screen
    screen.fill(BLACK)

    # Draw paddle, ball, and bricks
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    # Update the display
    pygame.display.flip()

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout")

    # Set up the clock
    clock = pygame.time.Clock()

    # Create the paddle and ball objects
    paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT, BLUE, SCREEN_WIDTH)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, WHITE, SCREEN_WIDTH)

    # Create the bricks
    bricks = []
    for i in range(BRICK_ROWS):
        for j in range(BRICK_COLS):
            brick = Brick(j * BRICK_WIDTH, i * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR)
            bricks.append(brick)

    # Main game loop
    running = True
    while running:
        # Handle events
        handle_events()

        # Update game state and check for game over
        running = update_game_state(paddle, ball, bricks)

        # Draw game objects
        draw_objects(screen, paddle, ball, bricks)

        # Cap the frame rate
        clock.tick(FPS)

    # Game over screen
    font = pygame.font.SysFont(None, 64)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
