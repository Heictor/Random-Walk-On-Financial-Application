import numpy as np
import matplotlib.pyplot as plt
import random
import statistics
from mpl_toolkits.mplot3d import Axes3D

"""Inserção de valores """
qtd = int(input("Número de investimentos")) #qtd armazena a quantidade de possibilidades
print("Quantidade de valores: \n", qtd)

valorInicial = float(input("Insira o valor do investimento: "))#data1 armazena o valor do capital inicial
print("Valor Inicial: \n", valorInicial)

meses: int = int(input("Insira o valor de meses: "))# a armazena o valor de meses
print("Meses: \n", meses)


x1 = []
y2 = []
taxas = []
valores = []
meses1 = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(qtd):
    print("i: \n", i)
    for m in range(meses):
        print("m: \n", m)
        taxa = random.uniform(-0.05, 0.05)
        print("Taxa: \n", taxa)
        taxas.append(taxa)
        print("Taxas: \n", taxas)
        taxas1 = np.asarray(taxas)
        print("Taxas1: \n", taxas1)
        print("Taxa[", m, "] = ", taxa)

        valorFinal = valorInicial
        valores.append(valorFinal)
        print("Valores: \n", valores)
        valores1 = np.asarray(valores)
        print("Valores1: \n", valores1)
        valorFinal = valorInicial * ((1 + taxa) ** 1)
        print("ValorFinal: \n", valorFinal)
        valorInicial = valorFinal
        print("Novo Valor Inicial: \n", valorInicial)

        mes = m
        meses1.append(mes)
        meses11 = np.asarray(meses1)
    print("Meses: \n", meses11)

    ax.plot(taxas1, meses11, valores1)
    plt.xlabel('Taxas')
    plt.ylabel('Meses')
    plt.title('Comportamento de uma aplicação financeira')
plt.show()

fig = plt.figure()
plt.plot(taxas1, valores1)
plt.grid()
plt.xlabel('Taxas')
plt.ylabel('Valor Futuro')
plt.title('Comportamento de uma aplicação financeira')
plt.show()

fig = plt.figure()
plt.plot(meses11, valores1)
plt.grid()
plt.xlabel('Meses')
plt.ylabel('Valor Futuro')
plt.title('Comportamento de uma aplicação financeira')
plt.show()

