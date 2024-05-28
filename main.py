import pygame
import buttons
import sprites.colonies


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 100)
reg_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 50)
smaller_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 30)

pygame.display.set_caption("AP CSP Pygame!")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
background_color = (98, 130, 122)
page = "main_game"

# start screen
title = "Imperialize"
sbtn_x = 280
sbtn_y = 350
start_button = buttons.StartButton(sbtn_x, sbtn_y, 200, 70, (255, 255, 255))
sbtn_text = "Start"
display_title = title_font.render(title, True, (255, 255, 255))
display_sbtn_text = reg_font.render(sbtn_text, True, (0, 0, 0))

# colony selection
nec = sprites.colonies.Colony(50,50,"Imperialize/sprite_images/new_england_colonies.png")


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True


# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if page == "start":
            if event.type == pygame.MOUSEBUTTONUP and start_button.rect.collidepoint(event.pos):
                page = "main_game"

# Blit
    screen.fill((98, 130, 122))
    # screen.blit(map_background, (0,0))
    if page == "start":
        screen.blit(display_title, (170, 150))
        pygame.draw.rect(screen, start_button.color, start_button)
        screen.blit(display_sbtn_text, (sbtn_x + 50, sbtn_y + 10))
    if page == "main_game":
        screen.blit(nec.image, nec.rect)




    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
