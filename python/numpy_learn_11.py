import numpy as np

x = np.empty([3,2],dtype=int)
print(x)

y = np.zeros([5,3],dtype=float,order='C')
print(y)


xy = np.zeros((2,2), dtype=[('x','i4'),('y','i4')])

print(xy)
print(xy.shape)


aa = np.random.randint(100,200,(3,3))
print(aa)


ai = np.arange(10)
bi = np.arange(10,20)
ci = np.arange(10,20,2)
print(ai)

print(bi)

print(ci)


ab = np.eye(5)
print(ab)



