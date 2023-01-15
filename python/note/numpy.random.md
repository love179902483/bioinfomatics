### 关于 numpy.random 的解释

1.	`numpy.random.randn(d0,d1...,dn)`

	* 输入: d0, d1, d2 ... , dn: int 可选
	* 返回: A(m0, m1,....)   shaped 大小服从标准正太分布（均值为0,方差为1），若无输入值，则返回单个副点数
	* 例子:
		``` python
		>>> np.random.rand()
		-0.032520361570606976
		```

		``` python
		>>> np.random.randn(2,3)
		[[ 0.13837459 -1.26560502  0.80081652]
		 [ 2.0976841   0.76788921  0.36561914]]]]]

		```


		``` python
		>>> np.random.randn(10)
		[-1.28265282 -0.39586468  0.73049524 -0.68110914 -0.5710301   1.54866597 -2.07624983 -0.01206551  0.05431064  0.33837575]]

		```



2.	`numpy.random.rand(d0, d1, d2....dn)
	
	
	* 输入: d0, d1, d2 ... , dn: int 可选

	* 返回: A(m0, m1,....)   shaped 生成[0,1]之间的数据，包含0，不包含1,若不输入值则返回单个浮点数
	* 例子：
		``` python
		>>> np.random.rand()
		0.1007475660661592
		```

		``` python
		>>> np.random.rand(2,3)
		[[0.77525927 0.76097541 0.94287393]
		 [0.00513291 0.36386181 0.17260013]]

		```

		``` python
		>>> np.random.rand(10)
		[0.53648326 0.00069066 0.41612969 0.47222329 0.65190819 0.12212541 0.41958638 0.01207235 0.50476385 0.05975568]]

		```

3. `numpy.random.randint(start, stop, size,dtype)

	* 输入 
		1.	low:int 生成的数值最低要大于等于low。(high = None时候，生成的数值要在[0, low) 区间内)
		2.	high:int (可选) 如果使用这个值，则生成的数值在[low, high)区间。 
		3.	size: int or tuple of ints(可选) 输出随机数的尺寸，比如size=(m*n*k)则暑促同规模即m*n*k个随机数。默认是None,仅仅返回满足要求的单一随机数
		4.	dtype: dtype(可选): 想要输出的格式。如 int64、int等等。
	* 输出
		* 返回一个随机数或者随机数组

	* 例子：
		``` python
		>>> np.random.randint(2, 9)
		7

		>>> np.random.randint(2, 9, 5)
		[2 7 7 6 8]

		>>> np.random.randint(2, 9, (2,3))
		[[5 8 8]
		 [5 5 3]]
		```
4.	`numpy.random.uniform(low, high, size)

	* 输入
		1.	low: 下界， float类型，默认为0
		2.	high: 上界，float类型，默认为1
		3.	size: 输出样本数量，为Int或者tuple类型，例如，size=(m, n, k) 则输出为 m*n*k个样本，缺省时候输出为1个值
	
	* 输出
		ndarray类型，形状和参数与size描述一致

	* 例子
		
		``` python

		>>> uniform01 = np.random.uniform()
		0.8047912334485202
		>>> uniform02 = np.random.uniform(2,)
		0.8047912334485202
		>>> uniform03 = np.random.uniform(4, 7)
		0.8047912334485202
		>>> uniform04 = np.random.uniform(4, 7, 5)
		[[4.98585722 5.52512449 5.64154774 5.27595603 4.68157352]]
		>>> uniform05 = np.random.uniform(4, 7, (2, 3))
		[[4.19056633 5.28216959 6.20050327]
		 [4.70597796 5.80593484 6.48959252]]

		```

5.	`numpy.random.random(int or (tuple))`

	*输入
		1.	int: 当输入一个整形的时候表示需要长度为n的随机以为数组
		2.	tuple: size=(m, n, k) 输出为m*n*k个样本，缺省的时候输出为1个值


	*输出
		ndarray类型，形状和参数与size一致


	*例子

		``` python
		>>> random01 = np.random.random()
		0.14031816893648563
		>>> random02 = np.random.random(2)
		[0.50448265 0.26176483]
		>>> random03 = np.random.random((2,))
		[0.91957931 0.3420875 ]
		>>> random04 = np.random.random((2, 4))
		[[0.51361155 0.92366089]
		 [0.5340939  0.43286549]
		 [0.69157584 0.82739554]
		 [0.1661872  0.7096469 ]]
		```
	> `numpy.random.random` 与 `numpy.random.rand()`两个函数功能完全一样，numpy为什么这么做是有历史原因的。可能是为了matlab用户更容易学习python + numpy的组合


6.	`numpy.random.choice(a, size=None, replace=True, p=None)` 

	*输入
		1.	a 从a(只要是ndarray都可以，但是必须是一维的)中随机抽取数字，并且组成制定大小(size)的数组
		2.	replace  True表示抽取后放回，也就是可以抽取到相同的数字，False表示不妨会的抽取，表示不可以获取相同的数字
		3.	数组p, 与数组a想对应，比欧式取数组a中每个元素的概率，默认为选取每个元素概率相同
	
	*例子

		``` python
		>>> source_A = [1, 2, 3, 4, 5]
		>>> source_B = ("test01", "test02", "test03", "test04", "test05")
		>>> choice01 = np.random.choice(5)
		3
		>>> choice02 = np.random.choice(5, 3)
		[0 2 4]
		>>> choice03 = np.random.choice(a=5, size=6, replace=True, p=None)
		[0 0 3 3 4 4]
		>>> choice04 = np.random.choice(source_A, size=10)
		[3 1 2 4 2 1 1 1 1 1]
		>>> choice05 = np.random.choice(source_B, size=8)
		['test03' 'test04' 'test04' 'test04' 'test01' 'test02' 'test03' 'test02']
		```


7. `numpy.random.shuffle(array)`

	*输入 
		array 需要是array 的数据不可以是tuple
	*输出
		函数是将原`array`打乱了顺序，而不会有返回值

	*例子
		``` python
		shuffle_A = ["M1","M2","M3","M4","M5","M6"]
		shuffle_B = [1, 2,3,4,5]
		>>> np.random.shuffle(shuffle_A)
		['M6', 'M4', 'M5', 'M1', 'M2', 'M3']
		>>> np.random.shuffle(shuffle_B)))]""""""""""""]
		[3, 5, 2, 4, 1]
		```


8. `numpy.random.seed()`
	> 简单来说若每次设置相同`seed()`那么每次获取到的随机数都是一样的，若不设置`seed()`则每次随机数都不一样
	
	*例子
		``` python
		>>> np.random.seed(10)
		>>> test_seed01 = np.random.randint(10, 100, (2, 4))
		[[19 25 74 38]
		 [99 39 18 83]]

		>>> test_seed02 = np.random.randint(10, 100, (2, 4))
		[[10 50 46 26]
		 [21 64 98 72]]

		>>> np.random.seed(10)
		>>> test_seed03 = np.random.randint(10, 100, (2, 4))))))))))
		[[19 25 74 38]
		 [99 39 18 83]]

		```


