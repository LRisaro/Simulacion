from math import log
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as ln

nums = list()
tiempo = list()
e = 1
for i in range(0,20):
    if e==1:
        if (np.random.uniform() < 0.95):
            nums.insert(i,1)

        else:
            nums.insert(i,0)
            e = 0
    else:
        if (np.random.uniform() < 0.4):
            nums.insert(i, 1)
            e = 1

        else:
            nums.insert(i, 0)
    tiempo.insert(i,i)

plt.plot(tiempo,nums)
plt.show()

