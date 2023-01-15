### python中获取绝对路径

	* os.path.dirname
		``` python

			import os
			path1 = os.path.abspath(__file__)
			# 获取当前文件的绝对路径
			print(path) 


			path2 = os.path.dirname(os.path.abspath(__file__))
			# 当前文件的上一层目录的绝对路径
			print(path2)


			path3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			# 获取当前文件上上一层目录的绝对路径
			print(path3)


		```
