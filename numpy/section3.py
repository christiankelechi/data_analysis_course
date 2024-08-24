import numpy as np

# Creating array from list with type float
a = np.array([[2,4,1], [[[3, 6, 2]]],[1,4,5]])
print ("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
# Printing type of arr object
print("Array is of type: ", type(a))

# Printing array dimensions (axes)
print("No. of dimensions: ", a.ndim)

# Printing shape of array
print("Shape of array: ", a.shape)