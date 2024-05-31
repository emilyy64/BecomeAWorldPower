import pygame

class Colony:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()

    def scale_image(self, scale):
        scale_size = (self.image_size[0] * scale, self.image_size[1] * scale)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()


class Nec(Colony):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.rect = pygame.Rect(self.x+135, self.y, self.image_size[0]-300, self.image_size[1]-150)


class Mc(Colony):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.rect = pygame.Rect(self.x+65, self.y, self.image_size[0]-140, self.image_size[1])


class Sc(Colony):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]-100, self.image_size[1]-40)