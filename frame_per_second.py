import pygame

pygame.init()  # initialization (essential)

# screen resolution
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Shooting game")

# FPS
clock = pygame.time.Clock()

# retrieving the background image
background = pygame.image.load(
    "C:\\Users\\shjun\\OneDrive\\문서\\python_development\\simple_game\\background.png")

# retrieving the character sprite
character = pygame.image.load(
    "C:\\Users\\shjun\\OneDrive\\문서\\python_development\\simple_game\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# chracter movement by coordinate
to_x = 0
to_y = 0

# movement speed
character_speed = 0.6

# event loop (To continue the game, pygame requires event loop to keep running)
isRunning = True
while isRunning:
    dt = clock.tick(60)  # setting the fps of the screen
    for event in pygame.event.get():  # tracking event
        if event.type == pygame.QUIT:  # when the user presses close button
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # adjusting movement speed according to the fps
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

# Keeping character inside of the screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # pygame requires constant drawing like frame by frame

# End game
pygame.quit()
