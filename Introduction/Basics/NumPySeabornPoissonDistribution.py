from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
Poisson Distribution is a Discrete Distribution.

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurences e.g. 2 for above problem.

size - The shape of the returned array.
"""

x=random.poisson(lam=2,size=10)
print(x)

sns.distplot(random.poisson(lam=2,size=1000), kde=False)
plt.show()
