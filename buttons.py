import pygame
from fonts import head_font, reg_font,larger_font
from display_vars import screen, screen_h, screen_w


class TextButton:
    def __init__(self, x, y, w, h, color, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.label = label
        self.label_display = head_font.render(self.label, True, (0, 0, 0))
    
    def handle_event(self,event):
         pass
    
    def draw(self, x):
        pygame.draw.rect(screen, self.color, self)
        screen.blit(self.label_display, (self.x + x, self.y))

class ImageButton:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


    def scale_image(self, w, h):
        self.image = pygame.transform.scale(self.image, (w, h))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class ChangePageButton(TextButton):
    def __init__(self, x, y, w, h, color, label, current_page, next_page):
        super().__init__(x, y, w, h, color, label)
        self.current_page = current_page
        self.next_page = next_page

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return self.next_page
        else:
            return self.current_page       

class StorageButton(TextButton):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
        self.label_display = larger_font.render(self.label, True, (0, 0, 0))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return True

class CloseBtn(ImageButton):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.scale_image(50, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return False
        else:
            return True

class RequestButton(ImageButton):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return True

class OpenRequestButton(TextButton):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return True
    
    def draw(self, x):
        pygame.draw.rect(screen, self.color, self)
        screen.blit(self.label_display, (self.x + x, self.y))
    
class AcceptButton(TextButton):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
    
    def handle_event(self, event, request, colony, requests):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            request.on_confirm(colony)
            colony.update_stat_displays()
            requests.pop(request.index)
            return True
        else:
            return False
            

class RejectButton(TextButton):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
    
    def handle_event(self, event, request, colony, requests):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            request.on_reject(colony)
            colony.update_stat_displays()
            requests.pop(request.index)
            return True
        else:
            return False
        
class NextButton(TextButton):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return False
        else:
            return True
        