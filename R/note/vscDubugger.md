### 使用R-debugger的时候老是报错，说需要vscDebugger经过一系列寻找找到一个比较靠谱的解答


在提醒需要vscDebugger之后，在terminal中会出现一行安装方式`ctrl + p` 之后输入` r.debugger.updateRPackage ` 即可

其中去少了`svSocket`依赖，所以还需要安装
> install.packages("svSocket")
