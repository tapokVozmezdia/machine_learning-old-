# Простейший перцептрон. Задача классификации в двумерном пространстве
from misc import *
import math
import random
import matplotlib.pyplot as plt

X1 = [random.randint(0, 10) for i in range(0, 5)]
X2 = [random.randint(0, 10) for i in range(0, 5)]
Y1 = [X1[i] + (random.randint(0, 500)) / 100 for i in range(0, 5)]
Y2 = [X2[i] - (random.randint(0, 500)) / 100 for i in range(0, 5)]

X = X1 + X2
Y = Y1 + Y2

dLine = [min(X), max(X)]

testPerceptron = perceptron(0.3)

dividingLine = plt.plot(dLine, dLine, c = "yellow")
blue = plt.scatter(X1, Y1, c = "blue")
red = plt.scatter(X2, Y2, c = "red")

for i in range(0, 10):
    testPerceptron.newInput(X[i], Y[i])
    print(testPerceptron.forward())

plt.grid()
plt.xlabel("Ось Х")
plt.ylabel("Ось У")
plt.title("Визуализация точек")
plt.show()