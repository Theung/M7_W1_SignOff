import pygame
import random
from TSPDecoder import *

def main():
    # In Processing, this is where void setup() would be #
    # screen sizes
    screen_width = 800
    screen_height = 600

    size = (screen_width, screen_height)  # Set the screen size
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode(size)  # Initialize the pygame screen
    clock = pygame.time.Clock()  # Initialize a pygame timer

    black = (0, 0, 0)  # Define the color black
    red = (255, 0 ,0)  # Define the color red
    white = (255, 255, 255)
    TSP = TSPDecoder()


    # Set up the rectangle parameters
    rect_x = 100
    rect_y = 50
    rect_width = 50
    rect_height = 50
    rect_speed = 5

    # Set up the circle parameters
    circle_radius = 20
    circle_x = screen_width // 2
    circle_y = screen_height // 2
    circle_speed = 5

    # Set up the arrow parameters
    arrow_size = 20
    arrows = []

    def generate_arrows():
        side = random.randint(1, 4)  # 1: top, 2: right, 3: bottom, 4: left
        if side == 1:  # from top
            x = random.randint(0, screen_width - arrow_size)
            y = 0
            speed_x = random.randint(-3, 3)
            speed_y = random.randint(1, 3)
        elif side == 2:  # from right
            x = screen_width - arrow_size
            y = random.randint(0, screen_height - arrow_size)
            speed_x = random.randint(-3, -1)
            speed_y = random.randint(-3, 3)
        elif side == 3:  # from bottom
            x = random.randint(0, screen_width - arrow_size)
            y = screen_height - arrow_size
            speed_x = random.randint(-3, 3)
            speed_y = random.randint(-3, -1)
        else: # from left
            x = 0
            y = random.randint(0, screen_height - arrow_size)
            speed_x = random.randint(1, 3)
            speed_y = random.randint(-3, 3)
        arrows.append((x, y, speed_x, speed_y))
        # Function to read TSP sensor input (simulate it for this example)



    while TSP.available:
        # In Processing, this is where void draw() would be #

        # Check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # Get all pressed keys
        frame = TSP.readFrame()


        # Calculate average values for each region
        top_left_avg = np.mean(frame[0:13, 0:9])
        top_right_avg = np.mean(frame[0:13, 9:18])
        bottom_right_avg = np.mean(frame[13:27, 9:18])
        bottom_left_avg = np.mean(frame[13:27, 0:9])

        # Adjust circle position based on touch location
        if top_left_avg > (top_right_avg + bottom_right_avg + bottom_left_avg):
            circle_x -= circle_speed
        elif top_right_avg > (top_left_avg + bottom_right_avg + bottom_left_avg ):
            circle_x += circle_speed
        elif bottom_right_avg > (top_left_avg + top_right_avg + bottom_left_avg):
            circle_y += circle_speed
        elif bottom_left_avg > (top_left_avg + top_right_avg + bottom_right_avg):
            circle_y -= circle_speed

        # Move arrows and check for collision with the circle
        updated_arrows = []
        for arrow in arrows:
            arrow_x, arrow_y, arrow_speed_x, arrow_speed_y = arrow
            arrow_x += arrow_speed_x
            arrow_y += arrow_speed_y
            if (circle_x - arrow_x) ** 2 + (circle_y - arrow_y) ** 2 <= circle_radius ** 2:
                pygame.quit()
            if 0 <= arrow_x <= screen_width - arrow_size and 0 <= arrow_y <= screen_height - arrow_size:
                updated_arrows.append((arrow_x, arrow_y, arrow_speed_x, arrow_speed_y))
        arrows = updated_arrows

        # Generate arrows randomly
        if random.random() < 0.02:
            generate_arrows()

        # Clear the screen
        screen.fill(white)  # Fill the whole screen with the color white

        # Draw the circle
        pygame.draw.circle(screen, black, (circle_x, circle_y), circle_radius)

        # Draw arrows
        for arrow in arrows:
            pygame.draw.rect(screen, red, (arrow[0], arrow[1], arrow_size, arrow_size))

        pygame.display.flip()  # Update the screen

        clock.tick(60)  # Limits frame rate to 60 FPS


# Run the main function only if this module is executed as the main script
if __name__ == "__main__":
    # call the main function
    main()
