import pygame


class Button:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


class StartButton(Button):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    def on_click(self):
        return "naming"



