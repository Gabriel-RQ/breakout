import pygame
import time
import math

from entities import *
from util import *

pygame.init()

# Set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")


pygame.quit()
