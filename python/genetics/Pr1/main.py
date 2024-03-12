import pygame
import random
import settings as st
import cellLogic

def blitAll(populationCount):
    for i in range(0, populationCount):
        screen.blit(allCells[i].getImage(), allCells[i].getRect())

cellSize = st.cellSize()
fieldSize = st.fieldSize()
frameRate = 12

pygame.init()
screen = pygame.display.set_mode((cellSize * fieldSize, cellSize * fieldSize))
pygame.display.set_caption("Nanomachines, son V2")
clock = pygame.time.Clock()
grid = [0] * (fieldSize * fieldSize)

allSprites = pygame.sprite.Group()
allCells = []

running = True
print(len(grid))
def startingPopulation():
    for i in range(0, 100):
        xCoordinate = random.randint(0, fieldSize - 1)
        yCoordinate = random.randint(0, fieldSize - 1)
        print(xCoordinate, yCoordinate)
        while(grid[xCoordinate + (yCoordinate * fieldSize)] != 0):
            xCoordinate = random.randint(0, fieldSize - 1)
            yCoordinate = random.randint(0, fieldSize - 1)
        allCells.append(cellLogic.Cell(xCoordinate, yCoordinate))
        grid[xCoordinate + yCoordinate * fieldSize] = 1
        allSprites.add(allCells[i])

startingPopulation()

while running:
    screen.fill((0, 0, 0))
    blitAll(len(allCells))
    clock.tick(frameRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    allSprites.update()
    pygame.display.flip()

pygame.quit()