import pygame
import random
import time

pygame.init()

width, height = 400, 400
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake")

x, y = 200, 200
delta_x, delta_y = 10, 0

food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

coco_x, coco_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

clock = pygame.time.Clock()

body_list = [(x, y)]

game_over = False

funcionando = True

tecla = pygame.key.get_pressed()

font = pygame.font.SysFont("bahnschrift", 25)

def snake():
    global x, y, food_x, food_y, coco_x, coco_y, game_over
    x = (x + delta_x)%width
    y = (y + delta_y)%height

    if((x, y) in body_list):
        game_over = True
        return

    body_list.append((x, y))

    if(coco_x == x and coco_y == y):
        game_over = True
        return

    if(food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
    else:
        del body_list[0]


    game_screen.fill((210, 180, 140))
    score = font.render('score: ' + str(len(body_list)), True, (255, 255, 0))
    game_screen.blit(score, [0, 0])
    pygame.draw.rect(game_screen, (0, 0, 0), [coco_x, coco_y, 10, 10])
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])
    for (i,j) in body_list:
        pygame.draw.rect(game_screen, (0, 139, 139), [i, j, 10, 10])
    pygame.display.update()

while funcionando:

    if(game_over):
        game_screen.fill((0, 0, 0,))
        score = font.render("score: " + str(len(body_list)), True, (255, 255, 0))
        game_screen.blit(score, [0, 0])
        msg = font.render("FIM DE JOGO!", True, (255, 255, 255))
        game_screen.blit(msg, [width//3, height//3])
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):    
            if(event.key == pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if(delta_x != -10):
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if(delta_y != 10):
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                    delta_y = 10
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_q]:
                funcionando = False     
        else:
            continue                 
            
    if(not events):
        snake()    
    clock.tick(20)
