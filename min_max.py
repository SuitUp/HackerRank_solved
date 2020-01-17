import numpy as np 

if __name__ == '__main__':

    n, m = map(int, input().split())

    arr = np.array([input().split() for _ in range(n)], int)
    arr_min = np.min(arr, axis=1)
    print(np.max(arr_min, axis=0))