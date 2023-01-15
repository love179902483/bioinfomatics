

import numpy as np


a = np.array([2,5,7])
b = np.array([(0,1),(2,3)])

print(a.sum)
print(b.sum)


print("a.min", a.min())
print("b.min", b.min())
print("a.max", a.max())
print("b.max", b.max())

print(b.max(axis=0))
print(b.max(axis=1))


aa = np.array([[1,2,3],[2,3,4],[3,4,6]])

print(aa[0][1])
print(aa[1][0])
