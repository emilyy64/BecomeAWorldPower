import pygame
from display_vars import screen, screen_h, screen_w
from popups import Storage, RequestBoard
from buttons import StorageButton, RequestButton, CloseBtn
from fonts import head_font

money_icon = pygame.transform.scale(pygame.image.load("sprite_images\money_icon.png"), (60,60))
happiness_icon = pygame.transform.scale(pygame.image.load("sprite_images\happiness_icon.png"), (60,60))
health_icon = pygame.transform.scale(pygame.image.load("sprite_images\health_icon.png"), (60,60))
pop_icon = pygame.transform.scale(pygame.image.load("sprite_images\pop_icon.png"), (60,60))

storage_popup = Storage(screen_w/3.9, 120, screen_w - (2*(screen_w/3.9)), 700, (255, 255, 255), "Storage")
storage_btn = StorageButton(1500, 880, 290, 70, (255, 255, 255), "Storage")
requests_btn = RequestButton(1400, 880, "sprite_images/requests_icon.png")
requests_btn.scale_image(60, 60)
requests_popup = RequestBoard(screen_w/8, 120, screen_w - (2*(screen_w/8)), 700, (255, 255, 255), "Requests")
close_requests_btn = CloseBtn(requests_popup.x + requests_popup.w - 100, requests_popup.y + 40, "sprite_images/close.png")
close_storage_btn = CloseBtn(storage_popup.x + storage_popup.w - 100, storage_popup.y + 40, "sprite_images/close.png")


def blit_ui(season, week, colony):
    if week in [5, 9, 13]:
        week = 1
    elif week in [4, 8, 12, 16]:
        week = 4
    else:
        week = week % 4
    season_display = head_font.render(season, True, (255, 255, 255))
    week_display = head_font.render("Week " + str(week), True, (255, 255, 255))
    screen.fill((98, 130, 122))
    screen.blit(season_display, (screen_w/2 - len(season)*25 - 10, 20))
    screen.blit(week_display, (screen_w/2 + len(season)*15, 20))
    screen.blit(money_icon, (80,880))
    screen.blit(colony.money_display, (150, 890))
    screen.blit(happiness_icon, (280,880))
    screen.blit(colony.happiness_display, (350, 890))
    screen.blit(health_icon, (480,880))
    screen.blit(colony.health_display, (550, 890))
    screen.blit(pop_icon, (680,880))
    screen.blit(colony.pop_display, (750, 890))
    storage_btn.draw(65)
    requests_btn.draw()

