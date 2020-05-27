import pygame
import random
import os
pygame.init()
pygame.mixer.init()
# Defining colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
screen_width = 900
screen_height = 600
# creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake_with_Riya")           # Game caption

font = pygame.font.SysFont(None, 50)  # Global variable
clock = pygame.time.Clock()


def text_screen(text, color, x, y):

    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))  # Update screen


def plot_snake(gameWindow, color, snk_list, snake_size):

    for x, y in snk_list:

        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def Welcome():
    exit_game = False
    while not exit_game:
        # gameWindow.fill(black)
        bgimg = pygame.image.load("snakespecs.jpg")
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))
        text_screen("WELCOME TO SNAKE GAME", red, 180, 50)
        text_screen("PRESS ENTER TO PLAY", red, 210, 100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('background.mp3')
                        pygame.mixer.music.play()

                        gameloop()

        pygame.display.update()
        clock.tick(60)


# game loops
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15

    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width / 1.5)  # creating food for snake
    food_y = random.randint(20, screen_height / 1.5)
    score = 0
    init_velocity = 5
    fps = 50
    snk_list = []
    snk_length = 1

    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        high_score = f.read()

    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            #  gameWindow.fill(white)
            bgimg1 = pygame.image.load("snakeblack.jpg")
            bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg1, (0, 0))
            text_screen("Game Over ! Press Enter To Continue", red, 180, 500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_RSHIFT:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 10
                food_x = random.randint(20, screen_width/1.5)
                food_y = random.randint(20, screen_height/1.5)
                snk_length += 5
                if score > int(high_score):
                    high_score = score
            gameWindow.fill(black)  # Filling up window with color
            text_screen("score : " + str(score) + " High Score : " + str(high_score), red, 5, 5) # to print it on screen
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, snake_x, snake_y, snake_size, snake_size)
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

    quit()


Welcome()
