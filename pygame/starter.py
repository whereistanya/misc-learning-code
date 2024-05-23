#!/usr/bin/python3
"""An extremely pointless game to learn pygame with."""

#variables!
import pygame
import random

WIDTH = 1600
HEIGHT = 800
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PINK = (255,0,255)
CYAN = (0,255,255)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50,50))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH/2,HEIGHT/2)

  def update(self):
    self.rect.x += 1
    self.rect.y -= 1
    if self.rect.left > WIDTH:
      self.rect.right = 0
    if self.rect.bottom < 0:
      self.rect.top = HEIGHT

# Beginning!

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame template")
clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()

player1 = Player()
allSprites.add(player1)

# Game loop!

running = True
while running:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  #update

  allSprites.update()

  #draw
  screen.fill(BLACK)
  allSprites.draw(screen)
  pygame.display.flip()

pygame.quit()
