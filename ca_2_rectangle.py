# Import and initialize pygame 
import pygame
pygame.init()

# Set dimensions of the screen
screen = pygame.display.set_mode((600, 600))

# Define Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Fill the screen with a base color (white)
screen.fill(white)
pygame.display.update()

# Rectangle class
class Rect:
    def __init__(self, color, dimensions):
        self.surface = screen
        self.color = color
        self.dimensions = dimensions

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.dimensions)

# Creating instances of rectangles    
green_rect = Rect(green, (50, 20, 100, 100))
red_rect = Rect(red, (150, 200, 150, 150))
blue_rect = Rect(blue, (300, 400, 200, 200))

# Main game loop to keep the window open
running = True
while running:
    # Handle events (including quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Redraw the background and rectangles
    screen.fill(white)  # Clear the screen (re-fill with white)
    green_rect.draw()
    red_rect.draw()
    blue_rect.draw()
    
    # Update the display to reflect changes
    pygame.display.update()

# Quit the pygame module
pygame.quit()
