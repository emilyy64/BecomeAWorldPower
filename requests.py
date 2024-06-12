import pygame
import random
from display_vars import screen, screen_w, screen_h
from fonts import reg_font
from buttons import OpenRequestButton
from popups import RequestPopup

class Request:
    def __init__(self, x, y, w, sender, index):
        self.x = x
        self.y = y
        self.w = w
        self.h = 500
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.sender = sender
        self.desc = ""
        self.open_btn = OpenRequestButton(self.x, self.y, self.w, self.h, (230, 204, 132), "Request")
        self.show = False
        self.index = index

    def on_confirm(self, colony):
        pass

    def on_reject(self, colony):
        pass

    def update_self(self, desc):
        self.desc = desc
        self.desc_display = reg_font.render(self.desc, True, (0, 0, 0))
        self.popup = RequestPopup(screen_w/3.5, 200, screen_w - (screen_w/3.5)*2, 500, (230, 204, 132), self.sender, self.desc)

class Request1(Request):
    def __init__(self, x, y, w, sender, index):
        super().__init__(x, y, w, sender, index)
        self.update_self(f"{sender} requests food")
    
    def on_confirm(self, colony):
        colony.storage["food"] -= 10
        colony.happiness += 10
        colony.update_weekly_report(["food", "happiness"], [-10, 10])
    
    def on_reject(self, colony):
        colony.happiness -= 10
        colony.update_weekly_report(["happiness"], [-10])



class Request2(Request):
    def __init__(self, x, y, w, sender, index):
        super().__init__(x, y, w, sender, index)
        self.update_self(f"{sender} requests money to build a new school")
    
    def on_confirm(self, colony):
        colony.money -= 500
        colony.happiness -= 50
        colony.update_weekly_report(["money", "happiness"], [-500, -50])
    
    def on_reject(self, colony):
        colony.happiness += 10
        colony.update_weekly_report(["happiness"], [10])


class Request3(Request):
    def __init__(self, x, y, w, sender, index):
        super().__init__(x, y, w, sender, index)
        self.update_self(f"{sender} advises to increase taxes on colonists")
    
    def on_confirm(self, colony):
        colony.money += 100
        colony.happiness -= 50
        colony.update_weekly_report(["money", "happiness"], [100, -50])

    
    def on_reject(self, colony):
        colony.happiness += 10
        colony.update_weekly_report(["happiness"], [10])


request_types = [Request1, Request2, Request3]