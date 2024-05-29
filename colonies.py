import pygame

class Colony:

    def __init__(self, x, y, scale, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * scale, self.image_size[1] * scale)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

