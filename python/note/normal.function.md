## 关于python的一般函数的解释

1.	`range(start, stop [, step])` 和 `numpy.arange([start,] stop, [step,] dtype=None)`

	* `range()`
		
		> 这是一个通用的函数来创建包含算数的列表，它最长用于for循环。参数必须是纯整数。如果省略step参数， 则默认为1。若省略start参数，则默认为0。最后一个元素是小于stop值的;如果setp是负数，则最后一个值大于stop的值。step不能是0,否则报错

		```
			>>> range(10)
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
			>>> range(1, 11)
			[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
			>>> range(0, 30, 5)
			[0, 5, 10, 15, 20, 25]
			>>> range(0, 10, 3)
			[0, 3, 6, 9]
			>>> range(0, -10, -1)
			[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
			>>> range(1, 0)
			[]
		```


	* `numpy.arange()`

		> 在给定[start, stop)区间内(不包括stop),返回一个ndarray而不是一个列表

		1.	start: 数字，可选
		
			开始，包括这个值，默认起始值为0

		2.	stop:  数字

			结束，不包括这个值，某些情况下，可以不是整数


		3. step: 步长，可选

			值之间的间隔。默认步长为1。如果指定了step，则还必须给出start。

		4. dtype: 输出数据的类型。如果没有给出dtype，则从其他输入参数判断数据类型

		5. return: 类型 ndarray

			



	* `range()` 与 `numpy.arange()`的比较：
		* `range()`和`numpy.arange()`的返回类型不同，`range()`的返回是range object, 而`numpy.arrage()`返回的ndarray类型。
		* `range()`不支持步长为小数， 而`numpy.arrange()`支持步长step的小数
		* `range()`和`numpy.arange()`都可以用于迭代
		* `range()`和`numpy.arange()`都有三个参数，以地一个参数为起点，第三个参数为步长，截至到第二个参数之前，不包括第二个参数的数据。
		* `range()`可用于迭代，而且`numpy.arange`作用远不止于此，它是一个序列，可悲当作向量使用。


	* `Iterable` 判断一个元素是否是可迭代的元素
	
	``` python
	from collections.abc import Iterable
	print(isinstance('abc', Iterable))

	```
