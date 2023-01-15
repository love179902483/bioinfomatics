

import numpy as np


original_array = np.array([1,2,3])
print(original_array)


np.save('my_array', original_array)


np.savetxt('/home/qy/workspace/bioinformatics/python/my_array.txt', original_array, fmt='%d')


array_from_npy = np.loadtxt('./my_array.txt')
print(array_from_npy)


