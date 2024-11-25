import pygame
import random

pygame.init()

window = pygame.display.set_mode((400,400))



#Square

square_height = 50
square_weidth = 50
square_x = 200
square_y = 200
square_color = (255,0,0) # Red color



c1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)
c2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)
c3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)
c4 = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        square_x = square_x - 1
    elif keys[pygame.K_RIGHT]:
        square_x = square_x + 1
    elif keys[pygame.K_UP]:
        square_y = square_y - 1
    elif keys[pygame.K_DOWN]:
        square_y = square_y + 1




    if square_x > 400:
        square_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)
    elif square_x < 0:
        square_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),)
    elif square_y < 0:
        square_color = c3
    elif square_y > 400:
        square_color = c4





    window.fill((0,0,0))
    
    
    pygame.draw.rect(window,square_color,(square_x,square_y,square_weidth,square_height))
    pygame.time.delay(3)
    pygame.display.update()


pygame.quit


