import pygame
from fonts import head_font
from display_vars import screen


class Button:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def handle_event(self,event):
         pass

class StartButton(Button):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color)
        self.label = label
        self.label_display = head_font.render(self.label, True, (0, 0, 0))

    def handle_event(self, event):
         if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                return "colony_selection"
         else:
              return "start"
         
    def draw(self):
        pygame.draw.rect(screen, self.color, self)
        screen.blit(self.label_display, (self.x + 60, self.y))


class ConfirmButton(Button):
     def __init__(self, x, y, w, h, color, label):
          super().__init__(x, y, w, h, color)
          self.label = label
          self.label_display = head_font.render(self.label, True, (0, 0, 0))

     def handle_event(self, event):
          if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                return "intro"
          else:
                return "colony_selection" 
     
     def draw(self):
        pygame.draw.rect(screen, self.color, self)
        screen.blit(self.label_display, (self.x + 65, self.y))
