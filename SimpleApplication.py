import numpy as np
import matplotlib.pyplot as plt
import random

"""Inserção de valores """

valorInicial = float(input("Insira o valor do investimento: "))#data1 armazena o valor do capital inicial

meses = int(input("Insira o valor de meses: "))# a armazena o valor de meses

mesesG = np.linspace(0, meses, num=50)

taxaG = float(input("Insira a taxa de juros: "))

valorFinal = valorInicial * ((1 + taxaG) ** mesesG)
print(valorFinal)

plt.plot(mesesG, valorFinal)
plt.xlabel('Número de períodos')
plt.ylabel('Valor Futuro')
plt.title("Investimento Simples")
plt.show()
