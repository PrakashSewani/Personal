import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

sns.distplot([0,1,3,5,9], hist=False)
plt.show()

x=random.normal(size=(2,3))#random distribution of 2*3
print(x)

x=random.normal(loc=1, scale=2, size=(12,13))