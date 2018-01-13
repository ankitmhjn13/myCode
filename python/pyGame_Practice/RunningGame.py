import pygame
import random

white = (255,255,255)
black = (1,1,1)
headingColor = (150,150,0)


scoreColor = (255,0,0)
playButtonColor = (0,255,0)
quitButtonColor = (255,0,0)
txtColor = black

def getFont(fontName, size):
    textSurface = pygame.font.SysFont(fontName, size)
    return textSurface

def getButton( surface, text, x, y, w, h, btncolor, txtColor):
    #below event loop will check if user has clicked inside the button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        mousePosition = pygame.mouse.get_pos() #to get the position of the click of the mouse
        mouseClick = pygame.mouse.get_pressed() #to check which mouse button is pressed (left, right pr center)
        if mouseClick[0] == 1 :
            if x + w > mousePosition[0] > x and y + 50 > mousePosition[1] > y:
                if text == 'Start':
                    gameLoop(surface)
                else:
                    quitGame()

    pygame.draw.rect(surface, btncolor,(x,y,w,h) )
    font = getFont('freesansbold.ttf', 30)
    textSurface = font.render(text, True, txtColor)
    textRectangular = textSurface.get_rect()
    textRectangular.center = ((x + (w/ 2)), (y + (h / 2)))
    surface.blit(textSurface, textRectangular)

def gameMenu(surface):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        font = getFont('freesansbold.ttf', 100)
        textSurface = font.render('Racing Game', False, headingColor)
        textRectangle = textSurface.get_rect()
        textRectangle.center = (surface.get_width()/2, surface.get_height()/2)
        getButton(surface, 'Start', 150, 450, 150, 50, playButtonColor, txtColor)
        getButton(surface, 'Quit!!', 450, 450, 150, 50, quitButtonColor, txtColor)
        surface.blit(textSurface, textRectangle)
        pygame.display.update()


def initializeImages():
    carImage = pygame.image.load('images/car.jpg')
    treeImage = pygame.image.load('images/tree.jpg')
    return carImage, treeImage

def initializePyGame():
    pygame.init()

def getTree(surface, img, startPosX, startPosY, ):
    surface.blit(img, (startPosX,startPosY))

def defineScreenResolution(width, height):
    surface = pygame.display.set_mode((width, height))
    return surface

def main():
    initializePyGame()
    surface = defineScreenResolution(800, 700)
    gameMenu(surface)
    gameLoop(surface)

def getCar(surface, img, x, y):
    surface.blit(img, (x,y))

def carCrashed(surface):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        font = getFont('freesansbold.ttf', 100)
        textSurface = font.render('Racing Game', False, headingColor)
        textRectangle = textSurface.get_rect()
        textRectangle.center = (surface.get_width()/2, surface.get_height()/2)
        getButton(surface, 'Play Again', 150, 450, 150, 50, playButtonColor, txtColor)
        getButton(surface, 'Quit!!', 450, 450, 150, 50, quitButtonColor, txtColor)
        surface.blit(textSurface, textRectangle)
        pygame.display.update()

def displayScore(surface, score):
    font = getFont('freesansbold.ttf',20)
    textSurface = font.render('Score: '+str(score), False, scoreColor)
    surface.blit(textSurface, (0,0))

def gameLoop(surface):
    cImage, tImage = initializeImages()
    surfaceWidth = surface.get_width()
    surfaceHeight = surface.get_height()
    carHeight = 120
    carWidth = 70
    c_StartX = surfaceWidth/2
    c_StartY = surfaceHeight-carHeight
    c_ChangeX = 0
    treeDisplaySpeed = 1
    t_width = 70
    t_startY = t_width
    t_startX = random.randrange(0, surfaceWidth)
    t_height = 120
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    c_ChangeX = 5
                if event.key == pygame.K_LEFT:
                    c_ChangeX = -5

            '''
            below if block is used to make the movement of the object smooth 
            if the below loop will not be used then the every time to move the object 
            we need to press the left or the right key agaain
            '''
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    c_ChangeX = 0

        c_StartX += c_ChangeX

        if c_StartX + carWidth > surfaceWidth:
            c_StartX = surfaceWidth - carWidth

        if c_StartX < 0:
            c_StartX = 0

        surface.fill(white)
        t_startY += treeDisplaySpeed # to move the tree image from top to bottom
        getTree(surface, tImage, t_startX, t_startY)
        getCar(surface, cImage, c_StartX, c_StartY)
        displayScore(surface, score)
        if t_startY > surfaceHeight: #this if condition will again generate the tree from new coordinates
            t_startY = 0
            t_startX = random.randrange(0,surfaceWidth)
            score += 1

        #to check if the car hit the tree
        if c_StartY < t_startY + t_height:
            print('Y crossover')
            if c_StartX > t_startX and c_StartX < t_startX + t_width or c_StartX + carWidth > t_startX and c_StartX + carWidth < t_startX + t_width:
                carCrashed(surface)
        pygame.display.update()
        pygame.time.Clock().tick(60)

def quitGame():
    pygame.quit()
    quit()

if __name__ =="__main__":
    main()