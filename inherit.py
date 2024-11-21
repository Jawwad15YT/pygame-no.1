#Pygame

import pygame
import random


pygame.init()

Screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Minecraft 2")

while True:

   for event in pygame.event.get():

     if event.type == pygame.QUIT:

         pygame.quit()
    
   Screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
   pygame.time.delay(1000)
   pygame.display.update()


pygame.quit()