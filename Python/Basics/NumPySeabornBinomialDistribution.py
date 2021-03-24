from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.
"""

x=random.binomial(n=10,p=0.5,size=10)
print(x)

sns.distplot(random.binomial(n=10,p=0.5,size=1000), hist=True,kde=True)
plt.show()