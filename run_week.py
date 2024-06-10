import pygame
from blit_ui import blit_ui
from fonts import head_font
from buttons import StorageButton, RequestButton, CloseBtn, AcceptButton, RejectButton
from popups import Storage, RequestBoard
from display_vars import screen, screen_h, screen_w
import random
from requests import request_types

storage_popup = Storage(screen_w/3.9, 120, screen_w - (2*(screen_w/3.9)), 700, (255, 255, 255), "Storage")
storage_btn = StorageButton(1500, 880, 290, 70, (255, 255, 255), "Storage")
requests_btn = RequestButton(1400, 880, "sprite_images/requests_icon.png")
requests_btn.scale_image(60, 60)
rb_x = screen_w/8
rb_w = screen_w - (2*rb_x)
requests_popup = RequestBoard(rb_x, 120, rb_w, 700, (166, 115, 64), "Requests")
close_requests_btn = CloseBtn(requests_popup.x + requests_popup.w - 100, requests_popup.y + 40, "sprite_images/close.png")
close_storage_btn = CloseBtn(storage_popup.x + storage_popup.w - 100, storage_popup.y + 40, "sprite_images/close.png")
close_request_btn = CloseBtn(screen_w/3.5 + screen_w - (screen_w/3.5)*2 - 80, 240, "sprite_images/close.png")
accept_btn = AcceptButton(screen_w/3.5 + 40, 560, 250, 100, (0, 255, 0), "Accept")
reject_btn = RejectButton(screen_w/3.5 + (screen_w - (screen_w/3.5)*2) - 300, 560, 250, 100, (255, 0, 0), "Reject")
request_completed = False

def run_week(week, colony, run):
    colonists = ["George Cleanington", "James Wonroe", "Alexander Beefington", "John Blue", "Benny Franklin", "Thomas Pain", "Roger Sureman", "James Willson", "John John", "Henry Roberts", "Mary Jane", "Sarah Michaels", "Susannah Smith", "Jane White", "Jane Franklin", "Madison Jackson" ]
    week_over = False
    show_storage = False
    show_requests = False
    is_request_open = False
    requests = []
    active_request = None
    for i in range(3):
        x = rb_x + (rb_w/3)*i + 60
        rand_req = request_types[random.randint(0, len(request_types)-1)]
        rand_sender = colonists[random.randint(0, len(colonists) - 1)]
        requests.append(rand_req(x, 240, rb_w/3 - 110, rand_sender, i))
    if week > 0 and week < 5:
        season = "Spring"
    if week > 4 and week < 9:
        season = "Summer"
    if week > 8 and week < 13:
        season = "Fall"
    if week > 12 and week < 17:
        season = "Winter"
    while not week_over and run:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
            is_popup = False if not show_storage and not show_requests and not is_request_open else True
            
            if not is_popup:
                if not show_storage:
                    show_storage = storage_btn.handle_event(event)
                if not show_requests:
                    show_requests = requests_btn.handle_event(event)
            else:
                if show_storage:
                    show_storage = close_storage_btn.handle_event(event)
                if show_requests:
                    if not is_request_open:
                        show_requests = close_requests_btn.handle_event(event)
                    for request in requests:
                        if not is_request_open:
                            request.show = request.open_btn.handle_event(event)
                            is_request_open = request.show
                        if request.show:
                            show_requests = False
                            active_request = request
                if is_request_open:
                    is_request_open = close_request_btn.handle_event(event)
                    request_completed = accept_btn.handle_event(event, active_request, colony, requests) or reject_btn.handle_event(event, active_request, colony, requests)
                    if request_completed:
                        is_request_open = False
                        colony.update_stat_displays()
                        for i in range(len(requests)):
                            requests[i].index = i
                if not is_request_open:
                    active_request = None
                    for request in requests:
                        request.show = False
            if not requests:
                colony.pop = int(round(colony.pop*colony.pop_growth_rate))
                week_over = True
                colony.update_stat_displays()

        blit_ui(season, week, colony)
        if show_requests:
            requests_popup.draw(close_requests_btn, requests)
        if is_request_open:
            active_request.popup.draw(close_request_btn, accept_btn, reject_btn)
        if show_storage:
            storage_popup.draw(close_storage_btn, colony.storage)
        pygame.display.update()
        
        if week_over:
            return True
    
    pygame.quit()