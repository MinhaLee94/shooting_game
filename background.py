import pygame

pygame.init()  # initialization (essential)

# screen resolution
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Shooting game")

# setting the background image
background = pygame.image.load(
    "C:\\Users\\shjun\\OneDrive\\문서\\python_development\\simple_game\\background.png")

# event loop (To continue the game, pygame requires event loop to keep running)
isRunning = True
while isRunning:
    for event in pygame.event.get():  # tracking event
        if event.type == pygame.QUIT:  # when the user presses close button
            isRunning = False

    screen.blit(background, (0, 0))  # drawing background
    pygame.display.update()  # pygame requires constant drawing like frame by frame

# End game
pygame.quit()
