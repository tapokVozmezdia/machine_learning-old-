import random 
import settings
import math

numberOfInputNeurons = 5
numberOfHiddenLayers = 1
numberOfHiddenNeuronsPerLayer = 3
numberOfOutputNeurons = 3

class Neuron():
    def __init__(self, givenInput = 1):
        self.input = givenInput
        self.output = givenInput
    def renewInput(self, givenInput):
        self.input = givenInput

class InputNeuron(Neuron):
    def __init__(self):
        super().__init__()
        self.weights = [random.randint(-400, 400) / 100 for i in range(0, numberOfHiddenNeuronsPerLayer)]
    def getWeights(self):
        return self.weights.copy()
    def normalizeOutput(self):
        self.output = self.input

class HiddenNeuron(Neuron):
    def __init__(self, isLast = False):
        super().__init__()
        if isLast == False:
            weightsNeeded = numberOfHiddenNeuronsPerLayer
        else:
            weightsNeeded = numberOfOutputNeurons
        self.weights = [random.randint(-400, 400) / 100 for i in range(0, weightsNeeded)]
    def neuronActivasion(self):
        self.output = (math.e**(2 * self.input) - 1)/(math.e**(2 * self.input) + 1)
    def getWeights(self):
        return self.weights.copy()
    
class OutputNeuron(Neuron):
    def __init__(self):
        super().__init__()
    def neuronActivasion(self):
        self.output = (math.e**(2 * self.input) - 1)/(math.e**(2 * self.input) + 1)

class NeuralNetwokrk():

    def __init__(self):
        self.inputNeurons = [InputNeuron() for i in range(0, numberOfInputNeurons)]
        self.hiddenNeurons = [[] for i in range(0, numberOfHiddenLayers)]
        for layerNumber in range(0, numberOfHiddenLayers):
            for neuronInLayerNumber in range(0, numberOfHiddenNeuronsPerLayer):
                if (layerNumber == numberOfHiddenLayers - 1):
                    isLast = True
                else:
                    isLast = False
                self.hiddenNeurons[layerNumber].append(HiddenNeuron(isLast))
        self.outputNeurons = [OutputNeuron() for i in range(0, numberOfOutputNeurons)]
    
    def renewInput(self, argList):
        for i in range(0, len(self.inputNeurons)):
            self.inputNeurons[i].renewInput(argList[i])
            self.inputNeurons[i].normalizeOutput()
            #print(self.inputNeurons[i].output)
    
    def forward(self):
        for i in range(0, numberOfHiddenLayers):
            if i == 0:
                for j in range(0, numberOfHiddenNeuronsPerLayer):
                    newValue = 0
                    for k in range(0, numberOfInputNeurons):
                        newValue += self.inputNeurons[k].output * self.inputNeurons[k].weights[j]
                    self.hiddenNeurons[i][j].renewInput(newValue)
                    self.hiddenNeurons[i][j].neuronActivasion()
            else:
                for j in range(0, numberOfHiddenNeuronsPerLayer):
                    newValue = 0
                    for k in range(0, numberOfHiddenNeuronsPerLayer):
                        newValue += self.hiddenNeurons[i - 1][k].output * self.hiddenNeurons[i - 1][k].weights[j]
                    self.hiddenNeurons[i][j].renewInput(newValue)
                    self.hiddenNeurons[i][j].neuronActivasion()
        for i in range(0, numberOfOutputNeurons):
            newValue = 0
            for j in range(0, numberOfHiddenNeuronsPerLayer):
                newValue += self.hiddenNeurons[-1][j].output * self.hiddenNeurons[-1][j].weights[i]
            self.outputNeurons[i].renewInput(newValue)
            self.outputNeurons[i].neuronActivasion()

    def getOutput(self):
        return [self.outputNeurons[i].output for i in range(0, numberOfOutputNeurons)]

    def geneticSnan(self):
        imprint = []
        portion = [[numberOfInputNeurons, numberOfHiddenLayers, numberOfHiddenNeuronsPerLayer, numberOfOutputNeurons]]
        imprint += portion
        for i in range(0, numberOfInputNeurons):
            imprint += self.inputNeurons[i].getWeights()
        for i in range(0, numberOfHiddenLayers):
            for j in range(0, numberOfHiddenNeuronsPerLayer):
                imprint += self.hiddenNeurons[i][j].getWeights()
        return imprint

'''testNet = NeuralNetwokrk()
testNet.renewInput([2, 2, 2, 2, 2])
for i in range(0, numberOfInputNeurons):
    print(testNet.inputNeurons[i].output)
testNet.forward()
for i in range(0, numberOfOutputNeurons):
    print(testNet.outputNeurons[i].output)

print(testNet.inputNeurons[0].weights[0])
w = testNet.inputNeurons[0].getWeights()
w[0] = 65
print(testNet.inputNeurons[0].weights[0])
print(testNet.geneticSnan())'''