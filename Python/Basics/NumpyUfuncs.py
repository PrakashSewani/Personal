"""
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

ufuncs also take additional arguments, like:

where boolean array or condition defining where the operations should take place.

dtype defining the return type of elements.

out output array where the return value should be copied.
"""
x=[5,22,534,33]
y=[44,312,324,65]
z=[]

for i,j in zip(x,y):
    z.append(i+j)
print(z)

"""
To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""

import numpy as np

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))

"""
np.add, np.subtract, np.multiply, np.divide, np.power, np.mod, np.remainder, np.divmod, np.absolute
"""
#Basically functions hai kaafi jo use nhi karne wala, agar use aaye toh dekh lena


