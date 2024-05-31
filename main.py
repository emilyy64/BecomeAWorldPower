import pygame
import buttons
import colonies


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 200)
reg_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 50)
smaller_font = pygame.font.Font('fonts/LombardicNarrow-GvWG.ttf', 30)

pygame.display.set_caption("AP CSP Pygame!")


# set up variables for the display
screen_w = 1200
screen_h = 1000
size = (screen_w, screen_h)
screen = pygame.display.set_mode(size)
background_color = (98, 130, 122)
page = "main_game"

# Coord Cursor
x = 0
y = 0
position = f"({x}, {y}"
display_position = smaller_font.render(position, True, (255, 255, 255))

# start screen
title = "Imperialize"
sbtn_x = screen_w/2.45
sbtn_y = screen_h/2
start_button = buttons.Button(sbtn_x, sbtn_y, 200, 70, (255, 255, 255))
sbtn_text = "Start"
display_title = title_font.render(title, True, (255, 255, 255))
display_sbtn_text = reg_font.render(sbtn_text, True, (0, 0, 0))

# colony selection
nec_x = screen_w/2.2
nec_y = -80
nec = colonies.Nec(nec_x, nec_y, "sprite_images/new_england_colonies.png")
nec.scale_image(.95)
mc = colonies.Mc(nec_x-200, nec_y+130,"sprite_images/middle_colonies.png")
sc = colonies.Sc(nec_x-355, nec_y+500,"sprite_images/southern_colonies.png")
sc.scale_image(1.13)



# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True


# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEMOTION:
            (x, y) = event.pos
            position = f"({x}, {y}"
            display_position = smaller_font.render(position, True, (255, 255, 255))
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if page == "start":
            if event.type == pygame.MOUSEBUTTONUP and start_button.rect.collidepoint(event.pos):
                page = "main_game"
        if page == "main_game":
            if event.type == pygame.MOUSEMOTION:
                if nec.rect.collidepoint(event.pos):
                    print("hovering: nec")
                elif mc.rect.collidepoint(event.pos):
                    print("hovering: mc")
                elif sc.rect.collidepoint(event.pos):
                    print("hovering: sc")



# Blit
    screen.fill((98, 130, 122))
    # screen.blit(map_background, (0,0))
    screen.blit(display_position, (x+10, y+5))
    if page == "start":
        screen.blit(display_title, (screen_w/8, screen_h/3.7))
        pygame.draw.rect(screen, start_button.color, start_button)
        screen.blit(display_sbtn_text, (sbtn_x + 50, sbtn_y + 10))
    if page == "main_game":
        screen.blit(nec.image, (nec.rect[0]-135, nec.rect[1]))
        screen.blit(mc.image, (mc.rect[0]-65, mc.rect[1]))
        screen.blit(sc.image, sc.rect)




    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
