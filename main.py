import pygame
import buttons


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.Font('C:/Users/bt_4n2_01/Downloads/Imperialize-main/Imperialize-main/fonts/LombardicNarrow-GvWG.ttf', 100)
pygame.display.set_caption("AP CSP Pygame!")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
background_color = (98, 130, 122)
title = "Imperialize"

start_button = buttons.StartButton(100, 100, 200, 400, (255, 255, 255))

# render the text for later
display_title = title_font.render(title, True, (255, 255, 255))




# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True


# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

# Blit
    screen.fill((98, 130, 122))
    # screen.blit(map_background, (0,0))
    screen.blit(display_title, (0, 0))
    pygame.draw.rect(screen, start_button.color, start_button)
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
