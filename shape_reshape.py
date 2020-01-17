import numpy as np 

integers = map(int, input().split())
#int_list = list(integers)
#if len(list(integers)) == 9:
i_array = np.array(list(integers))
reshape_array = np.reshape(i_array, (3,3))

print (reshape_array)
