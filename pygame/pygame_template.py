#!/usr/bin/python3
"""An extremely pointless game to learn pygame with."""

import pygame
import random

WIDTH = 500
HEIGHT = 600
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PINK = (255,0,255)
CYAN = (0,255,255)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("There Is No Escape From This Monstrosity")
clock = pygame.time.Clock()

# Game loop!
running = True
while running:
  screen.fill(PINK)
  pygame.display.flip()
  screen.fill(CYAN)
  pygame.display.flip()
  screen.fill(GREEN)
  pygame.display.flip()
  screen.fill(BLACK)
  pygame.display.flip()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      #print("NO!!!! THOU SHALT NOT LEAVE!!!!")
      running = False
   # if event.type == pygame.MOUSEMOTION:
    #  print("wigglywiggly")

pygame.quit()
