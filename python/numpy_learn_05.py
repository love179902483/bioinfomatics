
import numpy as np

# np.info(np.ndarray.dtype)


a = np.array([1,2,3])
b = np.array([2,4,5])

ab = np.add(a,b)

print("a is ", a)
print("b is ", b)
print(ab)

bc = np.subtract(a,b)

print("substract result",bc)

cd = np.multiply(a,b)

print("multiply result", cd)

ef = np.divide(a,b)

print("divide result", ef)


aq = np.sqrt(a)

print("sqrt a is ", aq.astype(float))


asin = np.sin(a)

print("asin as is",asin)


alog = np.log(a)

print("alog is ", alog)





