#!/usr/bin/python3
"""An extremely pointless game to learn pygame with."""

#variables!
import pygame
import random
import os

WIDTH = 600
HEIGHT = 800
FPS = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PINK = (255,0,255)
CYAN = (0,255,255)

class Player(pygame.sprite.Sprite):
  def __init__ (self):
    pygame.sprite.Sprite.__init__(self)
    self.image = player_img
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH/2,HEIGHT/2)
    self.xDirection = 1
    self.yDirection = 1

  def update(self):
    self.rect.x += self.xDirection
    self.rect.y += self.yDirection
    if self.rect.right == WIDTH and self.xDirection == 1 :
      self.xDirection = -1
    if self.rect.left == 0 and self.xDirection == -1:
      self.xDirection = 1
    if self.rect.bottom == HEIGHT and self.yDirection == 1:
      self.yDirection = -1
    if self.rect.top == 0 and self.yDirection == -1:
      self.yDirection = 1

# Beginning!

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame template")

game_folder = os.path.dirname(__file__)
asset_folder = os.path.join(game_folder, 'asset')
player_img = pygame.image.load(os.path.join(asset_folder,'flower.png')).convert()

print("game folder:", game_folder)
print("asset folder:", asset_folder)
print("image name:", os.path.join(asset_folder,'flower.png'))

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()

player2 = Player()
allSprites.add(player2)

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
  screen.fill(BLUE)
  allSprites.draw(screen)
  pygame.display.flip()

pygame.quit()
