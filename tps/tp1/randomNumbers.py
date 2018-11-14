import numpy as np
import matplotlib.pyplot as plt

num = list()
c = 135/64
n = 0

# while n<=10000:
#
#     j = np.random.uniform()
#     u = np.random.uniform()
#     x = 20*j*(1 - j)**3
#
#     if (u < x/c):
#         n = n + 1
#         num.insert(n,j)

# for i in range(0,1000):
#     num.insert(i,np.random.uniform())

plt.hist(num, bins=150)
plt.show()