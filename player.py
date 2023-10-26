import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Loading rectagnles around the player so that they can be moved
        self.walk_1 = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
        self.walk_2 = pygame.image.load("images/player/player_walk_2.png").convert_alpha()
        self.stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
        self.walk_frames = [self.walk_1, self.walk_2]
        self.walk_index = 0

        self.image = pygame.image.load("images/player/player_stand.png").convert_alpha()

        self.rect = self.image.get_rect(topleft=(50, 270))
        self.score = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 3
            self.animate()
        elif keys[pygame.K_d]:
            self.rect.x += 3
            self.animate()

    def animate(self):
        self.walk_index += .25
        if self.walk_index >= len(self.walk_frames):
            self.walk_index = 0
        self.image = self.walk_frames[int(self.walk_index)]

    def update(self):
        self.get_input()
