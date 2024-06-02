import pygame
from buttons import StartButton, ConfirmButton
import colonies
from fonts import head_font, reg_font, title_font 
from display_vars import screen, screen_h, screen_w

# set up variables for the display
background_color = (98, 130, 122)
page = "colony_selection"

# Coord Cursor
x = 0
y = 0
position = f"({x}, {y}"
display_position = reg_font.render(position, True, (255, 255, 255))

# start screen
title = "Imperialize"
start_button = StartButton(screen_w/2.45, screen_h/2, 300, 100, (255, 255, 255), "Start")
display_title = title_font.render(title, True, (255, 255, 255))

# colony selection
cs_title = "Choose your colonies"
display_cstitle = head_font.render(cs_title, True, (255, 255, 255))
nec_x = screen_w/2.5
nec_y = -60
nec = colonies.Nec(nec_x, nec_y)
mc = colonies.Mc(nec_x-200, nec_y+130)
sc = colonies.Sc(nec_x-355, nec_y+500)
nec_hover = mc_hover = sc_hover = False
selected_colony_name = ""
selected_colony = ""
confirm_btn = ConfirmButton(1530, 750, 350, 100, (255,255,255), "Confirm")


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEMOTION:
            (x, y) = event.pos
            position = f"({x}, {y}"
            display_position = reg_font.render(position, True, (255, 255, 255))
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if page == "start":
            page = start_button.handle_event(event)
        if page == "colony_selection":
            if event.type == pygame.MOUSEMOTION:
                nec_hover = nec.rect.collidepoint(event.pos)
                mc_hover = mc.rect.collidepoint(event.pos)
                sc_hover = sc.rect.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nec.rect.collidepoint(event.pos):
                    selected_colony_name = "nec"
                    selected_colony = nec
                elif mc.rect.collidepoint(event.pos):
                    selected_colony_name = "mc"
                    selected_colony = mc
                elif sc.rect.collidepoint(event.pos):
                    selected_colony_name = "sc"
                    selected_colony = sc
                else:
                    selected_colony_name = ""
            page = confirm_btn.handle_event(event)


# Blit
    screen.fill((98, 130, 122))
    # screen.blit(map_background, (0,0))

    if page == "start":
        screen.blit(display_title, (screen_h/2 + 50, screen_h/3.7))
        start_button.draw()
    if page == "colony_selection":
        screen.blit(display_cstitle, (20, 20))
        nec.draw()
        mc.draw()
        sc.draw()
        if (nec_hover or selected_colony_name == "nec") and selected_colony_name not in ("sc","mc"):
            nec.blit_info()
        elif (mc_hover or selected_colony_name == "mc") and selected_colony_name not in ("nec","sc"):
            mc.blit_info()
        elif (sc_hover or selected_colony_name == "sc") and selected_colony_name not in ("nec","mc"):
            sc.blit_info()
        if selected_colony_name:
            confirm_btn.draw()
    if page == "intro":
        screen.blit(selected_colony.name_display, (selected_colony.x, selected_colony.y + 80))
    screen.blit(display_position, (x+10, y+5))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
