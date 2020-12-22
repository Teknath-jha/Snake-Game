# Teknath krishna jha 
# Walchand college of engineering sangli
# CSE
# All dimensions are taken as per poco f1 

# Basic window setup 
# part 1

import pygame 
import time 
import random

# initializing pygame
pygame.init()

# colors
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
yellow = (255,255,0)

# window surface size 
width=90
window_width =1080

window_height =1500




gameDisplay = pygame.display.set_mode((window_width , window_height))


# window name 
pygame.display.set_caption('$n@ke g@me Teknath jha')

# text font 
font = pygame.font.SysFont(None , 25 , bold=True)

# on quit 
def myquit():
	pygame.quit()
	sys.exit()

clock = pygame.time.Clock()
FPS = 5
blockSize = 50
noPixel = 0

'''
sizeGrd = window_width // blockSize
row = 0
col = 0
for nextline in range(sizeGrd):
'''

# part 2
# function to each block of draw snake
def snake(blockSize, snakelist):

    #x = 250 - (segment_width + segment_margin) * i
    i=1

    for size in snakelist:
        if i==1:
            i=0
            pygame.draw.rect(gameDisplay, blue ,[size[0]+5,size[1],blockSize,blockSize],100)
        else:
            i=1
            pygame.draw.rect(gameDisplay, black ,[size[0]+5,size[1],blockSize,blockSize])
        

def message_to_screen(msg, color):
    # render bold text background is cyan
    screen_text = font.render(msg, True, 'red' ,'cyan')
    # position of text on surface 
    gameDisplay.blit(screen_text, [((window_width)/2)-350, ((window_height)/2) -50])

 # part 3
def gameLoop():

    # game status


    gameExit = False
    gameOver = False

    lead_x = (window_width+width)/2
    lead_y = (window_height+width)/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0
    
    # Initial snake dimension
    snakelist = []
    snakeLength = 1

    # food position
    # round for round off values for integer 
    randomAppleX = round(random.randrange(0, (window_width-width)-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, (window_height-width)-blockSize)/10.0)*10.0


    while not gameExit:
        # Execution of below while loop when game will over
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()

                # windows
                # leftArrow = event.key == pygame.K_LEFT
                # rightArrow = event.key == pygame.K_RIGHT
                # upArrow = event.key == pygame.K_UP
                # downArrow = event.key == pygame.K_DOWN


                # Androids
                leftArrow = event.key == pygame.K_4 
                rightArrow = event.key ==pygame.K_6 
                upArrow = event.key == pygame.K_2 
                downArrow = event.key ==  pygame.K_8 
                # for user speed self exceeding 
                # speed = event.key ==  pygame.K_5 

             #Reduce and exceed from opposite ends as per instructions as left ,right, up , down 
                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= (window_width-width) or lead_x < 0+width or lead_y >= (window_height-width) or lead_y < 0+width:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill('cyan')


        AppleThickness = 50
        # About food position and size in terminal in back-end
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        snake(blockSize, snakelist)

        # left most 
        pygame.draw.rect(gameDisplay,yellow,[0,0,width,window_height])
        # right most 
        pygame.draw.rect(gameDisplay,yellow,[window_width-width,0,width,window_height])
        # bottom most
        pygame.draw.rect(gameDisplay,yellow,[0,window_height-width,window_width,width])
        # top most 
        pygame.draw.rect(gameDisplay,yellow,[0,0,window_width,width])


        pygame.display.update()      

# Comparision of food and snake mouth position 
        if lead_x >= (randomAppleX - AppleThickness) and lead_x <= (randomAppleX + AppleThickness-2):

            if lead_y >= (randomAppleY - AppleThickness) and lead_y <= (randomAppleY + AppleThickness-2):

                randomAppleX = round(random.randrange(0+width, (window_width-width)-blockSize)/10.0)*10.0

                randomAppleY = round(random.randrange(0+width, (window_height-width)-blockSize)/10.0)*10.0
                # finally snake ate food 
                snakeLength += 1   

# Frames per second here it is 5fps

        clock.tick(FPS)

    pygame.quit()
    quit()

# Calling 

gameLoop()

