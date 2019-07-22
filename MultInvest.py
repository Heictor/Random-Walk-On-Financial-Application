import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

"""Inserção de valores """
qtd = int(input("Número de investimentos")) #qtd armazena a quantidade de possibilidades
print(qtd)

valorInicial = float(input("Insira o valor do investimento: "))#data1 armazena o valor do capital inicial

meses = int(input("Insira o valor de meses: "))# a armazena o valor de meses


x1 = []
y2 = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(qtd):

    taxa = random.uniform(0.01, 0.8)

    taxaG = np.linspace(taxa, taxa, num=50)
    mesesG = np.linspace(0, meses, num=50)
    valorFinal = valorInicial * ((1 + taxaG) ** mesesG)

    x1.append(taxaG)
    x11 = np.asarray(x1)
    y2.append(mesesG)
    y22 = np.asarray(y2)
    ax.scatter(taxaG, mesesG, valorFinal)
plt.show()
