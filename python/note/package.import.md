### 关于__init__.py的作用 

* __init__.py文件的作用就是将文件夹变为一个python模块，python中的没一个模块包中，都有__init__.py文件。通常__init__.py文件为空，但是我们还可以为它增加其他功能。我们在导入一个包的时候，实际上是导入了它的__init__.py文件。这样我们可以在__init__.py文件中批量导入我们想要导入的包，而不在需要一个一个导入。

	```(python)
		# mt/__init__.py
		# __init__.py
		
		import re
		import cv2
		import os
		import sys


		# mt/a.py
		import mt
		pirnt(mt.re, mt.sys, mt.os)
	```

* 注意这里访问__init__.py文件中的引入文件，需要加上"mt"。 __init__.py中还有一个重要的变量，__all__,它用来将全部的模块导入
	
		```
			# mt/__init__.py
			__all__ = ['os', 'sys', 're', 'cv2']

			# mt/a.py
			from package import *
		```

* __init__.py主要控制包的导入行为，我们要清楚理解__init__.py文件的作用，还需要了解一下import的机制。可以被import引入的有以下几种类型。

		1.	模块文件(.py)
		2.	c或者c++扩展（已经编译为共享库，或者DLL文件)
		3.	包（包含多个模块）
		4.	内建模块（使用c编写并已经链接到python解释器中）

* 当导入模块时候，解释器按照sys.path列表中的目录顺序来查找导入的文件
	```
		>>> import sys
		>>> print(sys.path)

		# linux:
		['',
		'/home/qy01/miniconda3/envs/biosoft/lib/python38.zip',
		'/home/qy01/miniconda3/envs/biosoft/lib/python3.8',
		'/home/qy01/miniconda3/envs/biosoft/lib/python3.8/lib-dynload',			'/home/qy01/miniconda3/envs/biosoft/lib/python3.8/site-packages']
	```
	> 其中list地一个元素空字符串短期表当前目录


* ### `import`自己的包

	*	目录结构如下
		``` python
			sub_ui.py
			main.py
			test/
				test1.py
			model/
				model1.py
		```
	*	同目录下 `main.py`导入到`sub_ui.py`
		``` python
			import sub_ui
			或者
			from sub_ui import *
		```

	*	子目录， `main.py` 导入 `model/model1.py`

		``` python
			# 需要在model/建立 __init__.py空文件，让编译器认为是一个模块。
			import model.model1
			或者
			from model.model1 import *
		```

	*	跨目录，`model1.py` 导入 `test/test1.py`

		``` 需要在test1/下建立__init__.py空文件```

		``` python
			import sys
			sys.path.append("..")
			import test.test1
		```


		```
			import sys
			sys.path.append("..")
			import test.test1 import *
		```
