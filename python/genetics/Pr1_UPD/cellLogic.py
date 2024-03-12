import pygame
import math
import settings as st
import cellBrain

cellSize = st.cellSize()
fieldSize = st.fieldSize()
tS = cellSize * fieldSize
frameRate = 20

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, xCoordinate, yCoordinate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((cellSize, cellSize))
        self.image.fill((0, 192, 0))
        self.rect = self.image.get_rect()
        self.rect.x = xCoordinate * cellSize
        self.rect.y = yCoordinate * cellSize
        self.brainWiring = cellBrain.NeuralNetwokrk()
        self.pigmentation()
        self.lifeTimer = 1
        self.isBumped = 0
        self.isAlive = 1
        self.marked = False
        
    def mark(self):
        self.marked = True

    def setBrain(self, imprint):
        self.brainWiring.geneticSet(imprint)

    def getBrainScan(self):
        return self.brainWiring.geneticSnan()

    def setPosition(self, xCoordinate, yCoordinate):
        self.rect.x = xCoordinate * cellSize
        self.rect.y = yCoordinate * cellSize

    def pigmentation(self):
        geneSample = self.brainWiring.geneticSnan()
        R = 96
        G = 128
        B = 96
        '''for i in range(1, geneSample[0][0] + 1):
            R += geneSample[i] * 10
        R = abs(R)
        for i in range(geneSample[0][0] + 1, geneSample[0][2]):
            B += geneSample[i] * 10
        B = abs(B)'''
        self.image.fill((R, G, B))

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect

    def decide(self):
        thoughts = self.brainWiring.getOutput()
        decision = ""
        if thoughts[2] > abs(thoughts[0]) and abs(thoughts[2]) > abs(thoughts[1]):
            return "stay"
        if abs(abs(thoughts[0]) - abs(thoughts[1])) < 0.2:
            if thoughts[0] >= 0:
                decision += "R"
            else:
                decision += "L"
            if thoughts[1] >= 0:
                decision += "T"
            else:
                decision += "B"
        else:
            if abs(thoughts[0]) > abs(thoughts[1]):
                if thoughts[0] >= 0:
                    decision += "R"
                else:
                    decision += "L"
            else:
                if thoughts[1] >= 0:
                    decision += "B"
                else:
                    decision += "T"
        return decision

    def act(self):
        direction = self.decide()
        if direction == "stay":
            pass
        if "T" in direction and self.rect.y > 0:
            self.rect.y -= cellSize
        if "B" in direction and self.rect.y < tS - cellSize:
            self.rect.y += cellSize
        if "L" in direction and self.rect.x > 0:
            self.rect.x -= cellSize
        if "R" in direction and self.rect.x < tS - cellSize:
            self.rect.x += cellSize
    
    def mutation(self):
        self.brainWiring.brainMutation()

    def update(self):
        self.brainWiring.renewInput([self.rect.x / tS, self.rect.y / tS, self.lifeTimer/100, math.sin(math.pi / 100 * self.lifeTimer), 0])
        self.act()
        self.lifeTimer += 1
        self.brainWiring.forward()

