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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(qtd):
    print("i: \n", i)
    for m in range(meses):
        print("m: \n", m)
        taxa = random.uniform(0.01, 0.15)
        print("Taxa: \n", taxa)
        taxas.append(taxa)
        print("Taxas: \n", taxas)
        taxas1 = np.asarray(taxas)
        print("Taxas1: \n", taxas1)
        print("Taxa[", m, "] = ", taxa)

        valorFinal = valorInicial * ((1 + taxa) ** meses)
        print("ValorFinal: \n", valorFinal)
        valores.append(valorFinal)
        print("Valores: \n", valores)
        valores1 = np.asarray(valores)
        print("Valores1: \n", valores1)
        valorInicial = valorFinal

    #taxaG = np.linspace(taxas, taxas, num=meses)
    mesesG = np.linspace(0, meses, num=meses)
    print("Meses: \n", mesesG)

    #x1.append(taxaG)
    #x11 = np.asarray(x1)
    #devPad = x11.std()
    #y2.append(mesesG)
    #y22 = np.asarray(y2)
    ax.plot(taxas1, mesesG, valores1)
plt.show()
#print("x1", x1)
#print("x11", x11)
#print("y2", y2)
#print("y22", y22)
#print("Standard Deviation of sample is ", np.std()
