import numpy as np 

if __name__ == "__main__":

    # Keeping 'z' optional here.
    x, y, *z = tuple(map(int, input().split()))
    
    shape = (x, y, *z)
    print(np.zeros(shape, dtype=np.int))
    print(np.ones(shape, dtype=np.int))