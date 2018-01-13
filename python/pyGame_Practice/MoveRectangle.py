import pygame


blue = (0,0,255)
orange = (200,200,0)
black = (255,255,255)
white = (1,1,1)

def initializePyGame():
    pygame.init()

def setScreenRatio():
    screenDisplay = pygame.display.set_mode((800,600))
    return screenDisplay

def drawRectangle(surface,  changeColor, pos):
    if changeColor:
        pygame.draw.rect(surface, blue, pos) # rect takes parameter (x,y,width, height)
    else:
        pygame.draw.rect(surface, orange, pos)

def gameLoop(surface):
    isBlue = True
    startPosX = 30
    startPosY = 30
    width = 50
    height = 50

    drawRectangle(surface, isBlue, (startPosX, startPosY, width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    startPosX +=5
                if event.key == pygame.K_LEFT:
                    startPosX -= 5
                if event.key == pygame.K_UP:
                    startPosY -= 5   # take a note of this
                if event.key == pygame.K_DOWN:
                    startPosY += 5   # take a note of this
        '''
        below if statements will not allow the rectangle to move outside the boundary of the 
        window.
        width = initial width of the rectangle
        height = intial height of the rectangle
        startPosX = starting x cordinate position of the rectangle
        startPosY = starting y cordinate position of the rectangle
        '''
        if startPosX + width > surface.get_width():
            startPosX = surface.get_width() - width
        if startPosX < 0:
            startPosX = 0
        if startPosY + height > surface.get_height():
            startPosY = surface.get_height() - height
        if startPosY < 0:
            startPosY = 0

        surface.fill(black)
        drawRectangle(surface, isBlue, (startPosX, startPosY, width, height))
        pygame.display.update()
        pygame.time.Clock().tick(60)


def main():
    initializePyGame()
    screenRatio = setScreenRatio()
    gameLoop(screenRatio)

def quitGame():
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()