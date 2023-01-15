## shell流程控制

### if else

语法格式

```
if condition
then
	command1
	command2
	command3
fi
```

写成一行
`if [$(ps -ef |grep -c "shh") -gt 1]; then echo "true"; fi`


### if else-if else

```
if condition1
then
	command1

elif condition2

then
	command2
else 
	command3
fi


判断两个变量是否相等
```
a=10
b=20
if [$a=$b]
then
	echo "a == b"
elif [$a -gt $b]
	echo "a > b"
then
	echo "a < b"
else
	echo "a < b"
fi
```

例：
```
num1=$[2*3]
mum2=$[1+5]
if test $[num1] -eq $[num2]
then 
	echo '=='
else
	echo '!='
fi
```




