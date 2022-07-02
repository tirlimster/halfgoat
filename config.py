from multiprocessing.connection import deliver_challenge
import pygame
from pygame.locals import *
import checker.new_check as checker
import time

alph = [
        ('а', 8.01),
        ('б', 1.59),
        ('в', 4.54),
        ('г', 1.7),
        ('д', 2.98),
        ('е', 8.45),
        ('ё', 0.04),
        ('ж', 0.94),
        ('з', 1.65),
        ('и', 7.35),
        ('й', 1.21),
        ('к', 3.49),
        ('л', 4.4),
        ('м', 3.21),
        ('н', 6.7),
        ('о', 10.97),
        ('п', 2.81),
        ('р', 4.73),
        ('с', 5.47),
        ('т', 6.26),
        ('у', 2.62),
        ('ф', 0.26),
        ('х', 0.97),
        ('ц', 0.48),
        ('ч', 1.44),
        ('ш', 0.73),
        ('щ', 0.36),
        ('ъ', 0.04),
        ('ы', 1.9),
        ('ь', 1.74),
        ('э', 0.32),
        ('ю', 0.64),
        ('я', 2.01)
]

cons = {
    'а': 0,
    'б': 1,
    'в': 1,
    'г': 1,
    'д': 1,
    'е': 0,
    'ё': 0,
    'ж': 1,
    'з': 1,
    'и': 0,
    'й': 1,
    'к': 1,
    'л': 1,
    'м': 1,
    'н': 1,
    'о': 0,
    'п': 1,
    'р': 1,
    'с': 1,
    'т': 1,
    'у': 0,
    'ф': 1,
    'х': 1,
    'ц': 1,
    'ч': 1,
    'ш': 1,
    'щ': 1,
    'ъ': 2,
    'ы': 0,
    'ь': 2,
    'э': 0,
    'ю': 0,
    'я': 0
}

minv = 6
minc = 10

SEED = 1543
BW, BH = 50, 50
WIDTH, HEIGHT = 20, 20
A, B = WIDTH * BW, HEIGHT * BH
MENUWIDTH = 800

checker.build()

iconImg = pygame.image.load("pics/Icon.png")

pygame.init()
pygame.display.set_icon(iconImg)
pygame.display.set_caption("Semigoat")
font = pygame.font.SysFont("comicsansms", 50)
display = pygame.display.set_mode((A + MENUWIDTH, B))
clock = pygame.time.Clock()

FPS = 60

LIGHT_YELLOW = (255, 255, 153)
LIGHT_RED = (255, 153, 153)
LIGHT_GREEN = (150, 250, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 180, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (120, 120, 120)

TEXT_HIGHLIGHT_COLOUR = LIGHT_GREEN
HIGHLIGHT_COLOUR = LIGHT_YELLOW
HIGHLIGHT_CORRECT = LIGHT_GREEN
HIGHLIGHT_WRONG = LIGHT_RED

COLOURS = [GREEN, RED, BLUE, ORANGE]
t1 = 0

deliverEvents = dict()

def registerForEvent(type, function, checker=lambda event: True):
    global deliverEvents
    if type not in deliverEvents:
        deliverEvents[type] = []
    deliverEvents[type].append((checker, function))

def clearRegisteredEvents():
    global deliverEvents
    deliverEvents.clear()

def tech_pygame():
    global deliverEvents
    global t1
    pygame.display.update()
    display.fill(WHITE)
    clock.tick(FPS)
    t1 = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type in deliverEvents:
            for checker, reaction in deliverEvents[event.type]:
                if checker(event):
                    reaction()