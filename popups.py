import pygame
from display_vars import screen
from fonts import head_font, reg_font, larger_font
from blit_lines import blit_lines

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
		start_y = 120
		for key, value in storage.items():
			key_display = larger_font.render(key, True, (0, 0, 0))
			value_display = larger_font.render(str(value), True, (0, 0, 0))
			screen.blit(key_display, (self.x + 40, self.y + start_y))
			screen.blit(value_display, (self.x + self.w - 80, self.y + start_y))
			start_y += 60

class RequestBoard(PopUp):
	def __init__(self, x, y, w, h, color, title):
		super().__init__(x, y, w, h, color, title)

	def draw(self, close_btn, requests):
		pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.title_display, (self.x + self.w/2.5, self.y + 20))
		close_btn.draw()
		for request in requests:
			request.open_btn.draw(65)

class RequestPopup(PopUp):
	def __init__(self, x, y, w, h, color, title, content):
		super().__init__(x, y, w, h, color, title)
		self.content = content
		self.content_display = reg_font.render(self.content, True, (0, 0, 0))
		

	def draw(self, close_btn, accept_btn, reject_btn):
		pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.title_display, (self.x + 40, self.y + 20))
		blit_lines(self.content, self.x + 40, self.y + 150, 650, (0, 0, 0))
		close_btn.draw()
		accept_btn.draw(30)
		reject_btn.draw(30)