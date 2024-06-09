import pygame
from buttons import ChangePageButton, StorageButton, CloseBtn, RequestButton, CompleteTaskBtn
import colonies
from fonts import head_font, reg_font, title_font 
from display_vars import screen, screen_h, screen_w
from popups import Storage, RequestBoard


def run_week(week, ):
    week_over = False
    show_storage = False
    show_requests = False
    while not week_over:
        is_popup = False if not show_storage and not show_requests else True
        requests = [1,2,3]
        if week > 0 and week < 5:
            season = "Spring"
        if week > 4 and week < 9:
            season = "Summer"
        if week > 8 and week < 13:
            season = "Fall"
        if week > 12 and week < 17:
            season = "Winter"
        season_display = head_font.render(season, True, (255, 255, 255))

        if not is_popup:
            if not show_storage:
                show_storage = storage_btn.handle_event(event)
            if not show_requests:
                show_requests = requests_btn.handle_event(event)
            complete_task_btn.handle_event(event, requests)
            if not requests:
                week += 1
        else:
            if show_storage:
                show_storage = close_storage_btn.handle_event(event)
            if show_requests:
                show_requests = close_requests_btn.handle_event(event)
        if not requests:
            week_over = True

        screen.blit(season_display, (screen_w/2.5, 20))
        screen.blit(week_display, (screen_w/2.5 + 220, 20))
        screen.blit(money_icon, (80,880))
        screen.blit(selected_colony.money_display, (150, 890))
        screen.blit(happiness_icon, (280,880))
        screen.blit(selected_colony.happiness_display, (350, 890))
        screen.blit(health_icon, (480,880))
        screen.blit(selected_colony.health_display, (550, 890))
        screen.blit(pop_icon, (680,880))
        screen.blit(selected_colony.pop_display, (750, 890))
        complete_task_btn.draw(65)
        storage_btn.draw(65)
        requests_btn.draw()
        if show_requests:
            requests_popup.draw(close_requests_btn)
        if show_storage:
            storage_popup.draw(close_storage_btn, selected_colony.storage)
    
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
money_icon = pygame.transform.scale(pygame.image.load("sprite_images\money_icon.png"), (60,60))
happiness_icon = pygame.transform.scale(pygame.image.load("sprite_images\happiness_icon.png"), (60,60))
health_icon = pygame.transform.scale(pygame.image.load("sprite_images\health_icon.png"), (60,60))
pop_icon = pygame.transform.scale(pygame.image.load("sprite_images\pop_icon.png"), (60,60))

season = "Spring:"
season_display = head_font.render(season, True, (255, 255, 255))
week = 1
week_display = head_font.render("Week " + str(week), True, (255, 255, 255))
storage_popup = Storage(screen_w/3.9, 120, screen_w - (2*(screen_w/3.9)), 700, (255, 255, 255), "Storage")
show_storage = False
storage_btn = StorageButton(1500, 880, 290, 70, (255, 255, 255), "Storage")
close_storage_btn = CloseBtn(storage_popup.x + storage_popup.w - 100, storage_popup.y + 40, "sprite_images/close.png")
show_requests = False
requests_btn = RequestButton(1400, 880, "sprite_images/requests_icon.png")
requests_btn.scale_image(60, 60)
is_popup = False
requests_popup = RequestBoard(screen_w/8, 120, screen_w - (2*(screen_w/8)), 700, (255, 255, 255), "Requests")
close_requests_btn = CloseBtn(requests_popup.x + requests_popup.w - 100, requests_popup.y + 40, "sprite_images/close.png")
complete_task_btn = CompleteTaskBtn(1000, 900, 500, 200, (255,255,255), "Complete")

# testing
page = "main"
selected_colony = nec
###############################


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
        if page == "intro":
            page = next_btn.handle_event(event)
        if page == "main":
            for i in range(0, 16):
                run_week()



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
