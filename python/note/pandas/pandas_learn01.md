### 记录一些panda的常用命令、操作

*   pandas 读取csv
	``` python
	df = pd.read_csv('student.csv', sep=':')

	```

*	pandas 指定文件的一行作为标题，标题指的是列标签。通常指的是一行，但有时候，如果文件顶部有额外的信息，我们希望指定另一行作为标题。可以这样操作：
	``` python

	df = pd.read_csv('student.csv', header=2)
	df.head()
	```


	* 这里我们使用第二行作为标题，上面的所有数据都被删除。`read_csv`使用head=0,使用第一行作为标签。如果文件不包含标签，可以使用`header=None`防止数据第一行被误当作标签列。

	* 我们可以使用以下方式来指定标签

	``` python
	labels = ['id', 'name', 'attendance', 'hw', 'project1']
	df = pd.read_csv('student_scores.csv', names = labels)
	df.head()

	```

*	pandas 读取前几行数据 
	*	`data1.head(10)`
	*	`data = pd.read_csv('data.csv', nrows = 5)

* 
	*	`fruit_tree.shape` : 查看数据的形状，返回(行数、列数)
	*	`fruit_tree.columns` : 查看列名列表
	*	`fruit_tree.index`	: 查看列索引
	*	`fruit_tree.dtypes`	: 查看每列数据类型


*	`pandas` 中 `loc`的用法	

	> `loc`的用法类似与切片。并且`loc`中的数字是前闭后闭，而不像`iloc`是前毕后开。`loc`可以使用列名称来获取整列数据。
	*	`fruit_tree.loc[:, 1]` : 获取图标中第二列的所有元素

	``` python
	>>> fruit_tree.loc[:, 1]
	0    调查日期
	1     NaN
	2    1985
	Name: 1, dtype: object
```
	*	`fruit_tree.loc[0, :]` : 获取第一行的所有元素
	``` python
	>>> fruit_tree.loc[0:1,]

	```

*	`pandas` 中 `iloc`的用法

	> `iloc` 的用法基本和`loc`的用法一样，但是，`loc`中是前闭后开的，并且`iloc`不可以使用列名称来获取整列数据。




