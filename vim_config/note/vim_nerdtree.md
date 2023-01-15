
## Vim产见NERDTree基本配置

1. 在vim启动的时候自动启动NERDTree
	> autocmd VimEnter * NERDTree 

2. 将NERDTree窗口设置在vim窗口右侧(默认为左侧)
	> let NERDTreeWinPos = "right"

3. NERDTree基本操作

	+ o: 开启一个目录或者开启档案，建立的是buffer，可以用来开启书签。并且跳到该窗口
	+ t: 在新的tab打开选种的文件/书签,并跳到新的Tab
	+ T: 在新的Tab中打开选中的文件/书签,但不跳到新的Tab
	+ i: split 一个新窗口打开选中的文件，并跳到新的Tab
	+ s: vsplit一个新窗口打开选中文件，并跳到该窗口
	+ !:执行当前文件
	+ O:递归打开选中节点下所有目录 
 	+ x:合拢选中节点的父目录
	+ X:递归合拢选中节点下所有目录
	+ D:删除当前书签
	+ P:跳到根节点
	+ p:跳到父节点
	+ K:跳到当前目录同级的第一个节点
	+ J:跳到当前目录同级最后一个节点
	+ C:将选中目录或者选中文件的父目录设置为跟节点
	+ u:将当前根节点的父目录设置为根目录，并变成合拢的跟节点
	+ r:递归的刷新选中目录
	+ R:递归刷新跟节点
4. 切换标签页
	+ :tabnew [++opt选项] [+cmd]文件建立制定文件新的tab
	+ :tabc 关闭当前tab
	+ :tabo 关闭所有其他tab
	+ :tabs 查看所有打开的tab
	+ :tabp 前一个tab
	+ :tabn 后一个tab
5. 标准模式下
	+ gT前一个tab
	+ gt后一个tab
