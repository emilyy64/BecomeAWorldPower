import pygame

class Colony:

    def __init__(self, x, y, scale, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        self.scale = scale

    def scale_image(self):
        scale_size = (self.image_size[0] * self.scale, self.image_size[1] * self.scale)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()


class Nec(Colony):
    def __init__(self, x, y, scale, image):
        super().__init__(x, y, scale, image)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


