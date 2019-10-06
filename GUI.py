import pygame

def draw_ground(pos, size):
    global screen
    pygame.draw.rect(screen, (100, 100, 100), (pos[0], pos[1], size[0], size[1]), 0)


def drawRocket(pos, size):
    global screen
    pygame.draw.rect(screen, (255, 0, 0), (pos[0], pos[1], size[0], size[1]), 0)


def update(rocket_pos, rocket_size, ground_pos, ground_size):
    global screen
    screen.fill((0, 0, 0))
    draw_ground(ground_pos, ground_size)
    drawRocket(rocket_pos, rocket_size)
    pygame.display.update()


def init(display_size):
    global screen
    pygame.init()
    screen = pygame.display.set_mode(display_size)
