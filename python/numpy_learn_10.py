import numpy as np

a = np.arange(24)
print(a.ndim)

b = a.reshape(2,4,3)
print(b.ndim)

ab = np.array([[1,2,3],[4,5,6]])
print(ab.shape)
print(ab)
ac = ab.reshape(3,2)
print(ac)

print(ab)

x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)

y = np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)

x = np.array([1,2,3,4,5])

print(x.flags)

xy = np.array([[1,23,4],[4,5,6]])
xz = xy.reshape(6,)


print(xy)
print(xz)

xz[0]=111111
print(xy)
print(xz)
