import pygame
from random import randint, choice


class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.apple = pygame.image.load("images/fruits/apple.png").convert_alpha()
        self.banana = pygame.image.load("images/fruits/banana.png").convert_alpha()
        self.peach = pygame.image.load("images/fruits/peach.png").convert_alpha()

        self.fruit_list = [self.apple, self.banana, self.peach]

        self.image = choice(self.fruit_list)
        self.rect = self.image.get_rect(topleft=(randint(130, 600), 50))

    def drop(self):
        self.rect.y += 2

    def floor(self):
        if self.rect.y >= 350:
            self.kill()

    def update(self):
        self.drop()
        self.floor()


class Beehive(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.beehive = pygame.image.load("images/fruits/beehive.png").convert_alpha()
        self.image = self.beehive
        self.rect = self.image.get_rect(topleft=(randint(130, 600), 50))

    def drop(self):
        self.rect.y += 2

    def floor(self):
        if self.rect.y >= 350:
            self.kill()

    def update(self):
        self.drop()
        self.floor()
