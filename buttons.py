import pygame

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 200, 100)

class StartButton(Button):
