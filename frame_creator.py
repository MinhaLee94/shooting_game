import pygame

pygame.init()  # initialization (essential)

# screen resolution
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Shooting game")

# event loop (To continue the game, pygame requires event loop to keep running)
isRunning = True
while isRunning:
    for event in pygame.event.get():  # tracking event
        if event.type == pygame.QUIT:  # when the user presses close button
            isRunning = False

# End game
pygame.quit()
