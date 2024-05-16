import pygame
import buttons


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.Font('C:/Users/bt_4n2_01/Downloads/Imperialize-main/Imperialize-main/fonts/LombardicNarrow-GvWG.ttf', 100)
reg_font = pygame.font.Font('C:/Users/bt_4n2_01/Downloads/Imperialize-main/Imperialize-main/fonts/LombardicNarrow-GvWG.ttf', 50)
smaller_font = pygame.font.Font('C:/Users/bt_4n2_01/Downloads/Imperialize-main/Imperialize-main/fonts/LombardicNarrow-GvWG.ttf', 30)

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

# main game screen
name = ""
input_text = ""
name_prompt = "Enter your name"
text_box_x = 240
text_box_y = 300
text_box = pygame.Rect(text_box_x, text_box_y, 300, 50)

# render the text for later
display_title = title_font.render(title, True, (255, 255, 255))
display_sbtn_text = reg_font.render(sbtn_text, True, (0, 0, 0))
display_name_prompt = reg_font.render(name_prompt, True, (255, 255, 255))
display_input_text = smaller_font.render(input_text, True, (0, 0, 0))

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
                page = start_button.on_click()
        if page == "naming":
            if event.type == pygame.KEYUP:
                input_text += event.key
                display_input_text = smaller_font.render(input_text, True, (0, 0, 0))

# Blit
    screen.fill((98, 130, 122))
    # screen.blit(map_background, (0,0))
    if page == "start":
        screen.blit(display_title, (170, 150))
        pygame.draw.rect(screen, start_button.color, start_button)
        screen.blit(display_sbtn_text, (sbtn_x + 50, sbtn_y + 10))
    if page == "naming":
        screen.blit(display_name_prompt, (text_box_x - 30, text_box_y - 70))
        pygame.draw.rect(screen, (255, 255, 255), text_box)
        if input_text:
            screen.blit(display_input_text, (text_box_x - 30, text_box_y - 70))
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
