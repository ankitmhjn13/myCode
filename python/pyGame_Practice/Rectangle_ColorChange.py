import pygame

blue = (0,0,255)
orange = (200,200,0)

def initializePyGame():
    pygame.init()

def setScreenRatio():
    screenDisplay = pygame.display.set_mode((800,600))
    return screenDisplay

def drawRectangle(surface,  changeColor):
    if changeColor:
        pygame.draw.rect(surface, blue, (30,30,60,60))
    else:
        pygame.draw.rect(surface, orange, (30, 30, 60, 60))
def gameLoop(surface):
    isBlue = True
    drawRectangle(surface, isBlue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                isBlue = not isBlue
                drawRectangle(surface, isBlue)

        pygame.display.update()

def main():
    initializePyGame()
    screenRatio = setScreenRatio()
    gameLoop(screenRatio)

def quitGame():
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()