### 1.查看R解释其版本及包的安装路径

1.1 .sessionInfo()查看R解释器版本以及运行平台信息
> 'sessionInfo()'

1.2 .libPath() 查看安装包路径
> '.libPaths()'

### 2. 查看可以安装的包

> 'p <- available.packages()'

> 'dim(p)'

显示：
> [1] 17582 17

### 3.查看已经安装的包

> installed.packages()

> 我们也可以使用grep(packageName, installed.packages()[,1]) 来查找看是否安装了某个包

### 4. R包的安装方式

	* 从CRAN 安装
		> install.packages('packageName')
		
		这个函数会从你设置的CRAN镜像中下载指定的二进制代码，并且安装到.libPath()指示的地方，我们也可以在函数中通过设置lib这个参数来指定安装到哪个目录。
	* 从github安装
		> library(devtools) 

		> install_github('hadley/dplyr')

		使用devtools包中的函数install_github()来安装，需要制定仓库名称例子中使用的'hadley/',这点通常比较困难，人们很难记住。为此有人开发了另一个包 githubinstall,也是专门用来从github安装R包的，用法类似于install.packages(),只要提供名字即可
		> library(githubinstall)

		> install_github('dplyr')

	* 从Bioconductor安装
		历史办法:

		> source("https://bioconductor.org/bioclite.R")

		>biocLIte('DavidWebService')

		先用source加载bioconductor仓库，然后通过biocLite()函数安装指定包

		Bioconductor已经更新了包管理工具，新的安装方法如下

		'''
			if(!requireNamespace("BiocManager", quietly = TRUE))
				install.packages("BiocManager")

			BiocManager::install("DESeq2")

		'''
