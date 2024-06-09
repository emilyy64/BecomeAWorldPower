import pygame
from display_vars import screen
from fonts import head_font, reg_font

class PopUp:
	def __init__(self, x, y, w, h, color, title):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.rect = pygame.Rect(x, y, w, h)
		self.title = title
		self.title_display = head_font.render(self.title, True, (0, 0, 0))


class Storage(PopUp):
	def __init__(self, x, y, w, h, color, title):
		super().__init__(x, y, w, h, color, title)

	def draw(self, close_btn, storage):
		pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.title_display, (self.x + self.w/2.7, self.y + 20))
		close_btn.draw()
		start_y = 100
		for key, value in storage.items():
			key_display = reg_font.render(key, True, (0, 0, 0))
			value_display = reg_font.render(str(value), True, (0, 0, 0))
			screen.blit(key_display, (self.x + 40, self.y + start_y))
			screen.blit(value_display, (self.x + self.w - 80, self.y + start_y))
			start_y += 40

class RequestBoard(PopUp):
	def __init__(self, x, y, w, h, color, title):
		super().__init__(x, y, w, h, color, title)

	def draw(self, close_btn):
		pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.title_display, (self.x + self.w/2.5, self.y + 20))
		close_btn.draw()