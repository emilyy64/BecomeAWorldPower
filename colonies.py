import pygame
from fonts import larger_font
from blit_lines import blit_lines
from display_vars import screen

class Colony:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale_image(self, scale):
        scale_size = (self.image_size[0] * scale, self.image_size[1] * scale)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

    def draw(self):
        pass

    def blit_info(self):
        pass


class Nec(Colony):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image =  pygame.image.load("Imperialize-main/sprite_images/new_england_colonies.png")
        self.image_size = self.image.get_size()
        self.scale_image(0.95)
        self.rect = pygame.Rect(self.x+135, self.y, self.image_size[0]-270, self.image_size[1]-150)
        self.name = "New England Colonies"
        self.name_display = larger_font.render(self.name, True, (255, 255, 255))
        self.desc = ["Colonies: New Hampshire, Massachusetts, Rhode Island, Connecticut", "Environment: Rocky terrain, harsh climate", "Economy: Fishing, Lumbering, Minimal farming for personal needs"]



    def blit_info(self):
        screen.blit(self.name_display, (self.x + 340, self.y + 140))
        start_y = self.y + 200
        for i in self.desc:
            num_lines = blit_lines(i, self.x + 360, start_y, 300)
            start_y += num_lines*45


    def draw(self):
        screen.blit(self.image, (self.rect[0]-135, self.rect[1]))

    
class Mc(Colony):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image =  pygame.image.load("Imperialize-main/sprite_images/middle_colonies.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x+65, self.y, self.image_size[0]-140, self.image_size[1]-100)
        self.name = "Middle Colonies"
        self.name_display = larger_font.render(self.name, True, (255, 255, 255))
        self.desc = ["Colonies: New York, Pennysylvania, New Jersey, Delaware", "Environment: Fertile soil. Location makes these colonies important distribution centers", "Economy: Ship building, lumber, wheat, grains"]



    def blit_info(self):
        screen.blit(self.name_display, (self.x + 540, self.y + 140))
        start_y = self.y + 200
        for i in self.desc:
            num_lines = blit_lines(i, self.x + 560, start_y, 300)
            start_y += num_lines*45
   

    def draw(self):
        screen.blit(self.image, (self.rect[0]-65, self.rect[1]))


class Sc(Colony):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image =  pygame.image.load("Imperialize-main/sprite_images/southern_colonies.png")
        self.image_size = self.image.get_size()
        self.scale_image(1.13)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.name = "Southern Colonies"
        self.name_display = larger_font.render(self.name, True, (255, 255, 255))
        self.desc = ["Colonies: Virginia, North Carolina, South Carolina, Georgia", "Environment: Mostly plains, good for farming", "Economy: Majorly agricultural, plantations"]


    
    def blit_info(self):
        screen.blit(self.name_display, (self.x + 640, self.y + 140))
        start_y = self.y + 200
        for i in self.desc:
            num_lines = blit_lines(i, self.x + 660, start_y, 300)
            start_y += num_lines*45


    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
