import numpy as np 

if __name__ == '__main__':
    n, m = map(int, input().split())

    print(str(np.eye(n, m, k=0)).replace('1', ' 1').replace('0', ' 0'))