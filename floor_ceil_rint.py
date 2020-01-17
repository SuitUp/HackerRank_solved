import numpy as np 

np.set_printoptions(sign=' ')


if __name__ == '__main__':

    u_input = list(input().split())
    arr = np.array(u_input, float)

    print(np.floor(arr), np.ceil(arr), np.rint(arr), sep='\n')