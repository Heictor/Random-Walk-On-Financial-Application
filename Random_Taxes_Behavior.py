import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

"""Inserção de Valores"""

valorInicial = float(input("Insira o valor da aplicação: "))
print("Valor Inicial: \n", valorInicial)

meses: int = int(input("Insira a quantidade de meses: "))
print("Meses: \n", meses)

x1 = []
y2 = []
taxas = []
valores = []
meses1 = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(1):
    print("i: \n", i)
    for m in range(meses):
        print("m: \n", m)
        taxa = random.uniform(-0.05, 0.05)
        print("Taxa: \n", taxa)
        taxas.append(taxa)
        print("Taxas: \n", taxas)
        taxas1 = np.asarray(taxas)
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
fig.savefig('3D_i_n_FV.png')
plt.show()

fig = plt.figure()
plt.plot(taxas1, valores1)
plt.grid()
plt.xlabel('Taxas')
plt.ylabel('Valor Futuro')
plt.title('Comportamento de uma aplicação financeira')
fig.savefig('i_FV.png')
plt.show()

fig = plt.figure()
plt.plot(meses11, valores1)
plt.grid()
plt.xlabel('Meses')
plt.ylabel('Valor Futuro')
plt.title('Comportamento de uma aplicação financeira')
fig.savefig('n_FV.png')
plt.show()

