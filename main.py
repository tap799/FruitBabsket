import pygame
import sys
from player import Player
from fruits import Fruits, Beehive

# pygame setup
GROUND_LEVEL = 270
pygame.init()
SCOREFONT = pygame.font.Font("font/ADLaMDisplay-Regular.ttf", 32)
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True

foxy = Player()
player_group = pygame.sprite.GroupSingle()
# noinspection PyTypeChecker
player_group.add(foxy)

fruits = Fruits()
fruit_group = pygame.sprite.Group()

beehive = Beehive()
beehive_group = pygame.sprite.Group()

# Loading images to surfaces, used for the background
bg_base = pygame.image.load("images/bg/bg-base.png").convert_alpha()
bg_canopy = pygame.image.load("images/bg/bg-canopy.png").convert_alpha()


def collide_fruit():
    fruit_collision = pygame.sprite.spritecollide(player_group.sprite, fruit_group, False)
    for fruit in fruit_collision:
        if fruit.rect.bottom >= foxy.rect.top:
            foxy.score += 1
            fruit.kill()
            collect_sound = pygame.mixer.Sound("sounds/collect.wav")
            collect_sound.play()



def collide_beehive():
    global running
    beehive_collision = pygame.sprite.spritecollide(player_group.sprite, beehive_group, False)
    for beehive in beehive_collision:
        if beehive.rect.bottom >= foxy.rect.top:
            running = False


# Timers: Creating a timer for every 1.5 seconds, a new fruit will be randomly selected and put into a random position
fruit_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fruit_timer, 1500)

beehive_timer = pygame.USEREVENT + 2
pygame.time.set_timer(beehive_timer, 3500)

bg_music = pygame.mixer.Sound("sounds/bg.wav")
bg_music.play(loops=-1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == fruit_timer:
            # noinspection PyTypeChecker
            fruit_group.add(Fruits())
        if event.type == beehive_timer:
            # noinspection PyTypeChecker
            beehive_group.add(Beehive())

    font_surface = SCOREFONT.render(f"score:{foxy.score}", True, "white")
    # foxy.update()
    screen.blit(bg_base, (0, 0))
    screen.blit(bg_canopy, (0, 0))

    player_group.draw(screen)
    player_group.update()

    collide_fruit()
    collide_beehive()

    fruit_group.draw(screen)
    fruit_group.update()

    beehive_group.draw(screen)
    beehive_group.update()

    screen.blit(font_surface, (10, 10))

    clock.tick(60)  # limits FPS to 60
    pygame.display.update()

pygame.quit()
