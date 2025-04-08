import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))