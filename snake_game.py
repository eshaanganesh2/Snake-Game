import pygame
from pygame.locals import *
import time
import random
import cv2
import HandTrackingModule as htm

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
        # self.handtracking=HandTracking()
        #self.gestureDirection=2

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
    
    def getDirection2(self):
        # if gestureDirection.value==1:
        #     self.snake.direction="left"
        # elif gestureDirection.value==2:
        #     self.snake.direction="right"
        # elif gestureDirection.value==3:
        #     self.snake.direction="up"
        # elif gestureDirection.value==4:
        #     self.snake.direction="down"
        # else:
        #     self.snake.direction=direction
        x=q.get()
        print(x)
        direction="right"
        if x==1:
            self.snake.direction="left"
        elif x==2:
            self.snake.direction="right"
        elif x==3:
            self.snake.direction="up"
        elif x==4:
            self.snake.direction="down"
        else:
            self.snake.direction=direction

    # Second parameter is for the gesture number...1 for left, 2 for right, 3 for up and 4 for down
    def run(self,option=1):
            print(option)
            running=True
            pause=False

            # Start the hand detection model only if the game is to be played in gesture mode
            if option==2:
                # Handling button click events (close window upon clicking of exit button, move block up upon clicking of up arrow key, etc.)
                wCam, hCam = 640, 480

                cap = cv2.VideoCapture(0)
                cap.set(3, wCam)
                cap.set(4, hCam)

                detector = htm.handDetector(detectionCon=0.75)

                # Landmark numbers for the fingertips
                tipIds = [4, 8, 12, 16, 20]
            # Handling button click events (close window upon clicking of exit button, move block up upon clicking of up arrow key, etc.)
            while running:
                # Normal mode
                if option==1:
                    for event in pygame.event.get():
                        if pause==True and event.type==KEYDOWN and event.key == K_RETURN:
                            pause = False
                            self.snake = Snake(self.surface)
                            self.apple = Apple(self.surface)
                        # Handling up,down,right and left keys
                        if event.type==KEYDOWN:
                            if not pause:
                                # Normal mode
                                self.getDirection1(event)

                        # Handling click of exit button
                        elif event.type==QUIT:
                            running=False
                            return

                # Gesture Controlled mode
                elif option==2:
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            running=False
                            return
                    #pygame.event.get()
                    #print("Hello",gestureDirection.value)
                    # try:
                    #     q.get(timeout=1)
                    # except:
                    #     print("queue is empty")
                    # print(option,"option")
                        if pause==True and event.type==KEYDOWN and event.key == K_RETURN:
                            pause = False
                            self.snake = Snake(self.surface)
                            self.apple = Apple(self.surface)
                            totalFingers=2
                    if not pause:
                        # self.getDirection2()
                        try:
                            _, img = cap.read()
                            img = detector.findHands(img)
                            lmList = detector.findPosition(img, draw=False)

                            if len(lmList) != 0:
                                fingers = []
                                # Thumb
                                fingers.append(1 if lmList[tipIds[0]][1] >
                                            lmList[tipIds[0] - 1][1] else 0)

                                # 4 Fingers
                                for id in range(1, 5):
                                    fingers.append(1 if lmList[tipIds[id]][2]
                                                < lmList[tipIds[id] - 2][2] else 0)

                                totalFingers = fingers.count(1)
                                if totalFingers > 0 and totalFingers < 5:
                                    cv2.rectangle(img, (20, 225), (170, 425),
                                                (0, 255, 0), cv2.FILLED)
                                    cv2.putText(img, str(totalFingers), (45, 375),
                                                cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

                            cv2.putText(img, f'1:Left, 2:Right, 3:Up, 4:Down ', (50, 50), cv2.FONT_HERSHEY_PLAIN,
                                        2, (255, 0, 0), 2)

                            if totalFingers==1:
                                self.snake.direction="left"
                            elif totalFingers==2:
                                self.snake.direction="right"
                            elif totalFingers==3:
                                self.snake.direction="up"
                            elif totalFingers==4:
                                self.snake.direction="down"
                            else:
                                self.snake.direction="right"
                            cv2.imshow("Image", img)
                            cv2.waitKey(1)
                            print(self.snake.direction)

                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                Run = False

                        except Exception as e:
                            print(e)
                            pass
                            # while not q.empty():
                            #     q.get() 
                            #print(self.snake.direction)

                else:
                    option=1

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
        #optionScreen = pygame.image.load("assets/options.png").convert()
        font = pygame.font.SysFont('Arial',60)
        title = font.render(f"SNAKE GAME",True,(0,0,0))
        self.surface.blit(title,(325,50))
        font = pygame.font.SysFont('Arial',40)
        score = font.render(f"Select Mode: ",True,(0,0,0))
        self.surface.blit(score,(375,225))
        line2 = font.render("1. Normal Mode", True, (245, 61, 61))
        self.surface.blit(line2,(375, 300))
        line3 = font.render("2. Gesture Mode", True, (41, 65, 242))
        self.surface.blit(line3,(375, 350))
        
        while optionRunning:
            #self.surface.blit(optionScreen, (0, 0))
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
            game.run(option)
