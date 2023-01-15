## matplotlib.pyplot.scatter

1.	`scatter`函数
	
	> matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)

	* x,y :array_like, shape(n,) ,形状如(n, 1)的数组
	* s: 点的大小
	* c: 色彩颜色序列，标记颜色
		* RGB 三元素颜色：使用相同的颜色绘制所有标记
		* 由RGB三元数组组成三列矩阵：对每个标记使用不同的颜色，矩阵的每行对应标记指定一种RGB三元颜色。行数必须等于x和y的长度
		* 向量：对每个标记使用不同颜色，并以现行方式将c中的值映射到当前颜色图中的颜色。c的长度必须等于x,y的长度。要更改坐标区域的按色图，使用colormap函数
	
	* marker:可选，默认：'o'，下面有详细解释
	* cmap: 调整见变色或者颜色列表的种类
	* norm: normalize可选，默认为`none`, 数据亮度 0 - 1,float数据
	* vmin, vmax: 标量，可选，默认为`none`，亮度设置，若norm实例已经使用，该参数无效
	* alpha: 标量，可选，默认为`none` ： 0 - 1
	* linewidths: 边框的宽度
	* edgecolor: 标记边框的颜色
