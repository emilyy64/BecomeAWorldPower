import pygame
from buttons import ChangePageButton, StorageButton, CloseBtn, RequestButton
import colonies
from fonts import head_font, reg_font, title_font 
from display_vars import screen, screen_h, screen_w
from popups import Storage, RequestBoard
from run_week import run_week

    
# set up variables for the display
background_color = (98, 130, 122)
page = "start"

# Coord Cursor
x = 0
y = 0
position = f"({x}, {y})"
display_position = reg_font.render(position, True, (255, 255, 255))

# start screen
title = "Imperialize"
start_button = ChangePageButton(screen_w/2.45, screen_h/2, 300, 100, (255, 255, 255), "Start", "start", "colony_selection")
display_title = title_font.render(title, True, (255, 255, 255))

# colony selection
cs_title = "Choose your colonies"
display_cstitle = head_font.render(cs_title, True, (255, 255, 255))
nec_x = screen_w/2.2
nec_y = -60
nec = colonies.Nec(nec_x, nec_y)
mc = colonies.Mc(nec_x-200, nec_y+130)
sc = colonies.Sc(nec_x-355, nec_y+500)
nec_hover = mc_hover = sc_hover = False
selected_colony_name = ""
selected_colony = ""
confirm_btn = ChangePageButton(1530, 750, 350, 100, (255,255,255), "Confirm", "colony_selection", "intro")

#intro
next_btn = ChangePageButton(screen_w/2.5, 750, 350, 100, (255,255,255), "Next", "intro", "main")

# main
week = 1

# testing
# page = "main"
# selected_colony = nec
###############################


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    if page != "main":
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
            if page == "intro":
                page = next_btn.handle_event(event)
    if page == "main":
        for i in range(0, 16):
            run_week(week, selected_colony, run)
            week += 1

# Blit
    screen.fill(background_color)
    # screen.blit(map_background, (0,0))

    if page == "start":
        screen.blit(display_title, (screen_w/3.4, screen_h/3.7))
        start_button.draw(65)
    if page == "colony_selection":
        screen.blit(display_cstitle, (20, 20))
        nec.draw(-135, 0)
        mc.draw(-65, 0)
        sc.draw(0, 0)
        if (nec_hover or selected_colony_name == "nec") and selected_colony_name not in ("sc", "mc"):
            nec.blit_info(340, 140)
        elif (mc_hover or selected_colony_name == "mc") and selected_colony_name not in ("nec", "sc"):
            mc.blit_info(540, 140)
        elif (sc_hover or selected_colony_name == "sc") and selected_colony_name not in ("nec", "mc"):
            sc.blit_info(640, 140)
        if selected_colony_name:
            confirm_btn.draw(65)
    if page == "intro":
        selected_colony.blit_intro_desc()
        next_btn.draw(65)

    screen.blit(display_position, (x+10, y+5))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
