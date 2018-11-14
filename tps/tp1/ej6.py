import numpy as np
import matplotlib.pyplot as plt

nums = list()
for i in range(0,10000):
    nums.insert(i,np.random.geometric(0.5))

plt.hist(nums,bins=30)
plt.show()