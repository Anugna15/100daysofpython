import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print("Shape of the array:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Data type of the array:", arr.dtype)
print("Size of the array:", arr.size)
print("Item size in bytes:", arr.itemsize)
print("Total bytes consumed by the array:", arr.nbytes)
print("Mean of the array:", arr.mean())
print("Sum of the array:", arr.sum())
print("Maximum value in the array:", arr.max())
print("Minimum value in the array:", arr.min())
print("Standard deviation of the array:", arr.std())
print("Variance of the array:", arr.var())
print("Transpose of the array:\n", arr.T)
print("Flattened array:", arr.flatten())
print("Reshaped array:\n", arr.reshape(1, 9))
print("Array after adding 5:\n", arr + 5)
print("Array after multiplying by 2:\n", arr * 2)
print("Array after squaring:\n", arr ** 2)
print("Array after adding two arrays:\n", arr + arr)
print("Array after multiplying two arrays:\n", arr * arr)
print("Array after dividing by 2:\n", arr / 2)
print("Array after subtracting 1:\n", arr - 1)
print("Array after floor division by 2:\n", arr // 2)
print("Array after modulo 2:\n", arr % 2)
print("Array after logical AND with 5:\n", arr & 5)
print("Array after logical OR with 5:\n", arr | 5)
print("Array after logical NOT:\n", ~arr)
print("Array after bitwise XOR with 5:\n", arr ^ 5)
print("Array after bitwise AND with 5:\n", arr & 5)
print("Array after bitwise OR with 5:\n", arr | 5)
print("Array after bitwise NOT:\n", ~arr)
