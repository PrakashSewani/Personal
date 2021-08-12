from numpy import random
import numpy as np

x=random.randint(1273)#remove int to print float
print(x)

x=random.randint(100,size=(5))
print(x)

x=random.choice([3,6,5,8])
print(x)

x=random.choice([3,5,6,9] , p=[0.1,.4,0.5,0.0], size=(50))#probability distribution function
print(x)

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)