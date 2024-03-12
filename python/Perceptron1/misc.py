# Реализация перцептрона
class perceptron():

    def __init__(self, weight):
        self.inputOne = 0
        self.inputTwo = 0
        self.output = 0
        self.weight1 = weight
        self.weight2 = -1 * weight

    def newInput(self, newInputOne, newInputTwo):
        self.inputOne = newInputOne
        self.inputTwo = newInputTwo

    def forward(self):

        if self.inputOne * self.weight1 + self.inputTwo * self.weight2 >= 0:
            self.output = "Class 1"
        else:
            self.output = "Class 2"

        return self.output