## 1. radian是什么

## 2. 安装radian

	* 安装radian，首先需要安装python3
	* `pip install -U radian`

## 3. radian体验
	
	在终端输入 radian 就可以进入交互界面了,radian界面包含了语法高亮以及语法提示，棒棒的。


## 4. radian特点
	
	* 跨平台，可以在windows, macOS,linux上运行
	* shell模式很好用，点击;进入shell模式，<backspace>键进入R编辑界面
	* 改进的R提示和网状python提示
		* 多行编辑
		* 语法高亮
		* unicode支持


### 5. 推荐设置radian

	终端快速输入`vim ~/.radian_profile`之后：

	```
	options(radian.escape_key_map = list(

		list(key = "-", value = " <- "),
		list(key = "m", value = " %>% ")
	))
	```


### 6. 将radian别名为r


	在`~/.bash_profile`,将r改为radian,R是传统的R console， 加入 `alias r = "radian"` 后保存

	之后在终端键入r,就可以进入radian了。
