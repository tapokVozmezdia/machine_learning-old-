import pygame
import random
import settings as st
import cellLogic

def condition(cell):
    '''if cell.rect.center[1] < fieldSize * 10 / 2 and cell.rect.center[0] > fieldSize * 10 / 2: #ПРАВЫЙ ВЕРХ
        return 1
    else:
        return 0'''
    if (cell.rect.center[0] > fieldSize * 10 / 2): #ПРАВЫЙ ВЕРХ
        return 1
    else:
        return 0
    
def addCond(cell):
    if (cell.rect.center[0] < fieldSize * 10 / 2): #ПРАВЫЙ ВЕРХ
        return 1
    else:
        return 0
def checkIfAlive(cell):
    if condition(cell) == 1:
        return 1
    else:
        return 0

def blitAll(populationCount):
    for i in range(0, populationCount):
        screen.blit(allCells[i].getImage(), allCells[i].getRect())

def clearGrid():
    global grid 
    grid = [0] * fieldSize
    for i in range(fieldSize):
        grid[i] = [0] * fieldSize

def crossingOver(imprint1, imprint2):
    offspring1 = [imprint1[0]]
    offspring2 = [imprint2[0]]
    for i in range(1, len(imprint1)):
        offspring1.append([])
        offspring2.append([])
        for j in range(0, len(imprint1[i])):
            crossLine = random.random()
            if j / len(imprint1[i]) < crossLine:
                offspring1[i].append(imprint1[i][j])
                offspring2[i].append(imprint2[i][j])
            else:
                offspring1[i].append(imprint2[i][j])
                offspring2[i].append(imprint1[i][j])
    offsprings = [offspring1, offspring2]
    return offsprings

def startingPopulation():
    for i in range(0, st.startingPopulation):
        xCoordinate = random.randint(0, fieldSize - 1)
        yCoordinate = random.randint(0, fieldSize - 1)
        #print(xCoordinate, yCoordinate)
        while(grid[xCoordinate][yCoordinate] != 0):
            xCoordinate = random.randint(0, fieldSize - 1)
            yCoordinate = random.randint(0, fieldSize - 1)
        allCells.append(cellLogic.Cell(xCoordinate, yCoordinate))
        aliveCells.append(1)
        grid[xCoordinate][yCoordinate] = 1
        allSprites.add(allCells[i])

def newGenerationCross():
    #print(f"GEN {gen + 1} FORMING")
    pass


def newGeneration():
    #print(f"GEN {gen + 1} FORMING")
    allSprites.empty()
    global grid
    clearGrid()
    parent1 = 0
    parent2 = 0
    for i in range(0, len(allCells)):
        xCoordinate = 0
        yCoordinate = 0
        while(grid[xCoordinate][yCoordinate] != 0):
            xCoordinate = random.randint(0, fieldSize - 1)
            yCoordinate = random.randint(0, fieldSize - 1)
        if (checkIfAlive(allCells[i]) == 0 or allCells[i].marked):
            allCells[i] = cellLogic.Cell(xCoordinate, yCoordinate)
        else:
            imprint = allCells[i].getBrainScan()                    #
            allCells[i] = cellLogic.Cell(xCoordinate, yCoordinate)  # ПРОСТОЕ ДОБАВЛЕНИЕ КЛЕТКИ БЕЗ СКРЕЩИВАНИЯ
            allCells[i].setBrain(imprint)       
        grid[xCoordinate][yCoordinate] = 1
        if (random.randint(0, 1000) > 995):
            allCells[i].mutation()
            #print(f"Cell {i} mutated!!!")
        allSprites.add(allCells[i])

cellSize = st.cellSize()
fieldSize = st.fieldSize()
frameRateBe = 12
frameRate = 12

pygame.init()
screen = pygame.display.set_mode((cellSize * fieldSize, cellSize * fieldSize))
pygame.display.set_caption("Nanomachines, son V2")
clock = pygame.time.Clock()
global grid 
grid = [0] * fieldSize
for i in range(fieldSize):
    grid[i] = [0] * fieldSize
font = pygame.font.SysFont('arial.ttf', 30)

allSprites = pygame.sprite.Group()
allCells = []
aliveCells = []
adjCk = [1] * st.startingPopulation

running = True
print(len(grid))
startingPopulation()

timer = 0
gen = 0
displayInfo = True

'''testSubject1 = cellLogic.Cell(0, 0)
testSubject2 = cellLogic.Cell(0, 0)
print(testSubject1.getBrainScan())
print(testSubject2.getBrainScan())
offsprings = crossingOver(testSubject1.getBrainScan(), testSubject2.getBrainScan())
print(offsprings[0])
print(offsprings[1])'''

while running:
    screen.fill((0, 0, 0))
    if timer == frameRateBe * 10:
        timer = 0
        newGeneration()
        gen += 1
    if timer == frameRateBe * 5:
        for i in range(0, len(allCells)):
            if (addCond(allCells[i]) == 0):
                allCells[i].mark()
    blitAll(len(allCells))
    text = font.render(f'Gen: {gen}', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (fieldSize * cellSize / 10, fieldSize * cellSize / 10)
    if displayInfo:
        screen.blit(text, textRect)
    clock.tick(frameRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                displayInfo = not(displayInfo)
            if event.key == pygame.K_UP:
                frameRate = frameRateBe * 1000
            if event.key == pygame.K_DOWN:
                frameRate = frameRateBe
    allSprites.update()
    pygame.display.flip()
    timer += 1

pygame.quit()