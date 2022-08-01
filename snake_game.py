import pygame
from pygame.locals import *
import time
import random

class Apple:
    def __init__(self,surface):
        #Loading the apple image (in assets folder)...for the apple
        self.apple=pygame.image.load("assets/apple.jpg").convert()
        self.surface=surface
        self.x=random.randint(0,24)*40 #Max width of the board is 1000 pixels
        self.y=random.randint(0,15)*40 #Max height of the board is 640 pixels

    def draw(self):
        # Code for drawing the apple
        self.surface.blit(self.apple,(self.x,self.y))
        pygame.display.flip()
    
    #Shifting the apple to a random new position
    def move(self):
        self.x=random.randint(0,24)*40 #Max width of the board is 1000 pixels
        self.y=random.randint(0,15)*40 #Max height of the board is 640 pixels

class Snake:
    def __init__(self,surface):
        #Loading the block image (in assets folder)...for the snake
        self.block=pygame.image.load("assets/block.jpg").convert()
        #Declaring the intial block coordinates to be equal to 0,0
        self.block_x=40
        self.block_y=40
        self.surface=surface
        self.direction="right"
        self.length=1
        # Creating two arrays of length 'length' having the x and y coordinates of each block of the snake
        self.x=[40]*self.length
        self.y=[40]*self.length

    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        # Filling the surface with the stated RGB values
        self.surface.fill((180, 250, 172))
        # Code for drawing the snake
        for i in range(self.length):
            self.surface.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move(self):
        # Updating body of the snake
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        # update head
        # Moving 40 units to right/up/down/left because the length of each block is 40 and to maintain alignment
        if self.direction == 'left':
            self.x[0] -= 40
        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40
        self.draw()
        

class Game:
    def __init__(self,surface):
        #Initialize pygame module
        # pygame.init()
        # # Initializing window for display with window dimension (in pixels) as parameters
        # self.surface=pygame.display.set_mode((1000,640))
        self.surface=surface
        self.snake=Snake(self.surface)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(0,0,0))
        self.surface.blit(score,(850,10))
        pygame.display.flip()
    
    def is_collision(self, x1, y1, x2, y2):
        if x1>=x2 and x1<x2+40:
            if y1>=y2 and y1<y2+40:
                return True
        return False

    def show_game_over(self):
        self.surface.fill((180, 250, 172))
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(0,0,0))
        self.surface.blit(score,(200,250))
        line2 = font.render("Press ENTER to play again!", True, (0,0,0))
        self.surface.blit(line2,(200, 300))

        pygame.display.flip()

    # Directions for normal mode
    def getDirection1(self,event):
        if event.key==K_LEFT:
            self.snake.direction="left"
        if event.key==K_RIGHT:
            self.snake.direction="right"
        if event.key==K_UP:
            self.snake.direction="up"
        if event.key==K_DOWN:
            self.snake.direction="down"

    def run(self,option=1):
            print(option)
            running=True
            pause=False
            # Handling button click events (close window upon clicking of exit button, move block up upon clicking of up arrow key, etc.)
            while running:
                if pause==True and event.type==KEYDOWN and event.key == K_RETURN:
                    pause = False
                    self.snake = Snake(self.surface)
                    self.apple = Apple(self.surface)
                if option==1:
                    for event in pygame.event.get():
                        # Handling up,down,right and left keys
                        if event.type==KEYDOWN:
                            if not pause:
                                # Normal mode
                                self.getDirection1(event)
                                
                                
                        # Handling click of exit button
                        elif event.type==QUIT:
                                running=False
                
                elif option==2:
                    print("Hello")
                
                else:
                    print("Hello")

                if not pause:
                    # Move the block every 0.25 seconds by 10 units in the current direction
                    time.sleep(0.25)
                    self.snake.move()
                    self.apple.draw()
                    if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
                        # If the head of the snake collides with the apple, move the apple to a new random position
                        self.apple.move()
                        self.snake.increase_length()
                    self.display_score()
                    # snake colliding with itself
                    for i in range(2, self.snake.length):
                        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                            # Show score and game over message
                            self.show_game_over()
                            pause = True
                    # snake colliding with the boundries of the window
                    if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 640):
                        # Show score and game over message
                        self.show_game_over()
                        pause = True
        
class Menu:
    def __init__(self,surface):
        #Initialize pygame module
        self.surface=surface
        # Initializing window for display with window dimension (in pixels) as parameters

    def draw(self):
        self.surface.fill((180, 250, 172))
        pygame.display.flip()
        pygame.display.set_caption("Snake Game")

        optionRunning = True
        font = pygame.font.SysFont('Arial',60)
        title = font.render(f"SNAKE GAME",True,(0,0,0))
        self.surface.blit(title,(325,50))
        font = pygame.font.SysFont('Arial',40)
        score = font.render(f"Select Mode: ",True,(0,0,0))
        self.surface.blit(score,(375,225))
        line2 = font.render("1. Normal Mode", True, (245, 61, 61))
        self.surface.blit(line2,(375, 300))
        line3 = font.render("2. Voice Mode", True, (41, 65, 242))
        self.surface.blit(line3,(375, 350))
        line4 = font.render("3. Gesture Mode", True, (23, 74, 17))
        self.surface.blit(line4,(375, 400))
        
        while optionRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    optionRunning = False
                    return "FALSE"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        optionRunning = False
                        return "1"
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        optionRunning = False
                        return "2"
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        optionRunning = False
                        return "3"

            pygame.display.update()

if __name__=="__main__":
    pygame.init()
    surface = pygame.display.set_mode((1000, 640))
    iterator=True
    while iterator:
        menu=Menu(surface)
        selected_option=menu.draw()
        #selected_option="2"
        print(selected_option)
        if selected_option=="FALSE":
            break

        if selected_option=="1":
            option=1
            game=Game(surface)
            game.run(option)

        if selected_option=="2":
            option=2
            game=Game(surface)


