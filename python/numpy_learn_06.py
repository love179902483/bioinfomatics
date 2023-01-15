
import numpy as np

a = np.array([(1,2,3), (4,5,6)])
b = np.array([(1,8,3), (4,5,6)])
c = np.array([(1,8,3), (4,5,6)])

print(a==b)

print(a<3)


print(np.array_equal(a,b))

print(np.array_equal(b,c))




