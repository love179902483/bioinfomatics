### numpy中的where()函数


#### numpy.where()分为两种调用方式


	* 三个参数 np.where(cond, x ,y)  满足 cond时候输出 x，不满足的时候输出y

	* 一个参数 np.where(array)  输出array中为"真"的坐标(也可以理解为非0)




	``` python

	>>> a = np.reshape(np.arange(0, 20), (4, 5))
	print(a)
	[[ 0  1  2  3  4]
	 [ 5  6  7  8  9]
	 [10 11 12 13 14]
	 [15 16 17 18 19]]
	>>> b = np.where(a > 5)
	print(b)
	array([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]),
	array([1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
	```
