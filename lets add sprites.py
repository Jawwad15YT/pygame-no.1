import pygame
import random
pygame.init()

window = pygame.display.set_mode((380,380))


#ball props

Ball_color = (255,255,255)
Ball_rad = 20
ball_x = 200
ball_y = 200
ball_speed = 5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    window.fill((0,0,0,))


    if ball_x > 380 or ball_x < 20:
        Ball_color = color
    

    if ball_y > 380 or ball_y < 20:
        Ball_color = color
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x = ball_x - ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x = ball_x + ball_speed
    if keys[pygame.K_UP]:
        ball_y = ball_y - ball_speed
    if keys[pygame.K_DOWN]:
        ball_y = ball_y + ball_speed
    
    
    
    
     
   
   
   
    
    
    
    
    pygame.draw.circle(window,Ball_color,(ball_x,ball_y),Ball_rad)

    pygame.time.delay(5)
    pygame.display.update()
