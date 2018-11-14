import matplotlib.pyplot as plt
import numpy as np

#Xn+1 = (Xn + c) mod m

m = 2**32
c = 1664525
a = 1013904223
seed = 94059 #PARTE ENTERA DEL PROMEDIO DE NUESTROS PADRONES (94335 + 93784)/2

#IMPRIMIR LOS PRIMEROS 6
# for i in range(0,6):
#
#     x = (a*seed + c) % m
#     print(x)
#     seed = x

#MODIFICACION PARA DEVOLVER NUMEROS ENTRE 0 Y 1. HISTOGRAMA
nums = list()
for i in range(0,100000):

    x = ((a*seed + c) % m)
    nums.insert(i,x/m)
    seed = x

plt.hist(nums,color='green')
plt.title('Distribucion de los numeros aleatorios obtenidos',color = 'blue')
plt.xlabel('Numeros obtenidos', color = 'blue')
plt.ylabel('Cantidad de apariciones',color = 'blue')
plt.show()