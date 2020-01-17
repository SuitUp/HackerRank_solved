import numpy as np 

n, m = map(int, input().split())

arr = np.array([input().strip().split() for _ in range(n)], int)
#print(arr)
transpose_arr = arr.transpose()
flatten_arr = arr.flatten()
print(transpose_arr)
print(flatten_arr)