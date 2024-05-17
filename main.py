import pygame
import buttons


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
page = "naming"

# start screen
title = "Imperialize"
sbtn_x = 280
sbtn_y = 350
start_button = buttons.StartButton(sbtn_x, sbtn_y, 200, 70, (255, 255, 255))
sbtn_text = "Start"

# naming screen
name = ""
input_text = ""
name_prompt = "Enter your name"
text_box_x = 240
text_box_y = 300
text_box = pygame.Rect(text_box_x, text_box_y, 300, 50)
is_exceeding_len = False
no_input = False
name_message = "Max 20 Characters"
display_name_message = smaller_font.render(name_message, True, (255, 0, 0))
enter_btn = buttons.Button(text_box_x + 60, text_box_y + 60, 180, 50, (255, 0, 255))

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
            if event.type == pygame.KEYUP and not name:
                if len(input_text) < 19:
                    input_text += event.unicode
                    display_input_text = smaller_font.render(input_text, True, (0, 0, 0))
                elif len(input_text) == 19:
                    is_exceeding_len = True
            if event.type == pygame.MOUSEBUTTONUP and enter_btn.rect.collidepoint(event.pos):
                if not input_text:
                    name = input_text
                print(name)


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
        pygame.draw.rect(screen, enter_btn.color, enter_btn)
        if input_text:
            screen.blit(display_input_text, (text_box_x + 10, text_box_y + 10))
        if is_exceeding_len:
            screen.blit(display_name_message, (text_box_x + 10, text_box_y + 70))


    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
