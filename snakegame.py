# Snake em Python #

# Bibliotecas

import pygame
import random

# Cores RGB

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

# Código #

pygame.init()
pygame.display.set_caption("Snake em Python")
clock = pygame.time.Clock()

width , heigth = 600 , 400

screen = pygame.display.set_mode((width,heigth))

# Snake

square_size = 10
game_velocity = 10

def food_generator():
    
    food_x = round(random.randrange(0 , width - square_size) / square_size) * square_size
    food_y = round(random.randrange(0 , heigth - square_size) / square_size) * square_size
    
    return food_x, food_y

def draw_food(size , x , y):
   
    pygame.draw.rect(screen, green, [x , y , size , size])

def draw_snake(size, pixels):

    for pixel in pixels:
        pygame.draw.rect(screen , white , [pixel[0], pixel[1], size , size])

def draw_points(points):
    
    font = pygame.font.SysFont("Times New Roman", 12)
    text = font.render(f"POINTS: {points}" , False , white)
    screen.blit(text , [8 , 5])

def velocity_selector(key):
    
    if key == pygame.K_DOWN:

        vx_snake = 0
        vy_snake = square_size

    elif key == pygame.K_UP:

        vx_snake = 0
        vy_snake = - square_size

    elif key == pygame.K_RIGHT:
        
        vx_snake = square_size
        vy_snake = 0

    elif key == pygame.K_LEFT:
        
        vx_snake = - square_size
        vy_snake = 0

    return vx_snake , vy_snake


def play():

    game_over = False

    x = width / 2
    y = heigth / 2 

    vx_snake = 0
    vy_snake = 0

    snake_size = 1
    pixels = []

    food_x , food_y = food_generator()

    while not game_over:

        screen.fill(black)

        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                game_over = True

            elif event.type == pygame.KEYDOWN:

                vx_snake , vy_snake = velocity_selector(event.key)

        

        # Desenhar Comida
        draw_food(square_size , food_x , food_y)

        # Atualizar posição do Ator
        if x < 0 or x >= width or y < 0 or y >= heigth:

            game_over = True

        x += vx_snake
        y += vy_snake

        # Desenhar Ator
        pixels.append([x , y])
        
        if len(pixels) > snake_size:
            del(pixels[0])

        for pixel in pixels[:-1]:
            if pixel == [x , y]:
                game_over = True

        draw_snake(square_size, pixels)
        
        # Desenhar Pontuação
        draw_points(snake_size - 1)

        # Criar nova Comida
        if x == food_x and y == food_y:
            
            snake_size += 1
            food_x , food_y = food_generator()

        # Atualização da Tela
        pygame.display.update()
        clock.tick(game_velocity)

play()
