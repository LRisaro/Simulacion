import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st
from mpl_toolkits.mplot3d import Axes3D


#Xn+1 = (Xn + c) mod m

m = 10
c = 7
a = 1
seed = 1 #PARTE ENTERA DEL PROMEDIO DE NUESTROS PADRONES (94335 + 93784)/2
M =11
#IMPRIMIR LOS PRIMEROS 6
# for i in range(0,6):
#
#     x = (a*seed + c) % m
#     print(x)
#     seed = x

#MODIFICACION PARA DEVOLVER NUMEROS ENTRE 0 Y 1. HISTOGRAMA
nums = list()
for i in range(0,M):

    x = ((a*seed + c) % m)
    nums.insert(i,x)
    seed = x

# for i in range(0,M):
#     nums[i] /= m


# plt.hist(nums,color='green')
# plt.title('Distribucion de los numeros aleatorios obtenidos',color = 'blue')
# plt.xlabel('Numeros obtenidos', color = 'blue')
# plt.ylabel('Cantidad de apariciones',color = 'blue')
# plt.show()

d = 0

unique, counts = np.unique(nums, return_counts=True)
print(unique)
print(counts)
print('Moda = ' + str(st.mode(nums)))

k = len(unique)
for i in range(0,k):
    d = d + ((counts[i] - M*0.1)**2)/(M*0.1)

print(d)


xs = []
ys = []


for i in range(0,M-1):
    xs.append(  nums[i])
    ys.append(  nums[i+1])

xs3d = []
ys3d = []
zs3d = []
for i in range(0,M-2):
    xs3d.append(  nums[i])
    ys3d.append (nums[i+1])
    zs3d.append (nums[i+2])

plt.scatter(xs,ys)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs3d,ys3d,zs3d)

plt.show()