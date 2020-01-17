import numpy as np 

n, m, p = map(int, input().split())

arr_1 = np.array([input().strip().split() for _ in range(n)], int)
arr_2 = np.array([input().strip().split() for _ in range(m)], int)

print (np.concatenate((arr_1, arr_2), axis = 0))