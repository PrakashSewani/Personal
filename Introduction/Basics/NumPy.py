import numpy

arr=numpy.array([1,2,3,4,5])

print(arr)
print(type(arr))
print(arr.dtype)
print(arr[0])

import numpy as np

arr=np.array([1,2,3,4,5,7])

print(arr)
print(type(arr))
print(arr.dtype)
print(arr[4])

#slicing b kar sakta

arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
for i in arr1:
    print(i)

arr2=np.concatenate((arr,arr1))

print(arr2)

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)#returns pos
print(x)

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

