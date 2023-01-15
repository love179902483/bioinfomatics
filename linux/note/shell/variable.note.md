## 变量使用

使用一个定义过的变量，只要在变量名前面加美元符号即可：

```
your_name="test"
echo $your_name
echo ${your_name}
```

变量名称外面的花括号是可选的，加不加都行，加话括号是为了帮助解释其识别变量的边界，如：

```
for skill in Ada Coffe Action Java; do
	echo "I am good at ${skill}Script"
done

```

## 只读变量

使用readonly命令可以将变量定义为只读变量，只读变量值不能改变。

```
test_readonly="goole.com"
readonly test_readonly
test_readonly="runoob.com"
```

运行脚本将会报错

```
/bin/sh: This variable is read only
```

## 删除变量

使用unset命令可以删除变量:

`unset variable_name`

变量删除后不能再次使用。unset命令不能删除只读变量。

```
test_unset="test variable"
unset test_unset
echo $test_unset
```

## shell 字符串
字符串是shell变成中最常用的数据类型

### *单引号*

` str='this is a string'`

*注意*
* 单引号中任何字符串都会原样输出，但因好字符串中的变量是无效的;
* 单引号字符串不能出现单独一个引号(对但因好使用转移字符后也不可以),但可成对出现，作为字符串拼接使用。


### *双引号*

```
your_name='runoob'
str="hello, i know you are \"$your_name\" \n"
echo -e $str
```

*优点*
* 双引号可以有变量
* 爽引号可以出现转意字符


## 字符串拼接

```
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name"!"

greeting_1="hello, ${your_name}!"

echo $greeting $greeting_1

# 使用单引号拼接
greeting_2='hello, '$your_name'!'
greeting_3='hello, ${your_name}!'

echo $greeting_2 $greeting_3
```

结果：
```
hello, runoob! hello, runoob!
hello, runoob! hello, ${your_name}!
```

## 获取字符串长度

```
string="abcd"
echo ${#string} #输出4
```


## 提取字符串
以下是从字符串第二个开始截取到第四个

```
string="runoob is great site"
echo ${string:1:4} # 输出 unoo
```


## 查找字符串

查找字符i或者o的位置(哪个字符先出现就计算哪个)


```
string="runoob is greate site"
echo `expr index "$string" io` # 输出4
```

## shell 数组

bash 支持一维数组(不支持多维数组),并且没有限定数组大小。

### 定义数组

```
数组名=(值1 值2  ... 值n)
```

例如:
```
array_name=(vale0 value1 value2 )

```
还可以单独定义数组各分量

```
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
array_name[3]=value3
```
### 读取数组

读取数组一般格式

```
${数组名[下标]}
```

例如：

```
valuen=${array_name[n]}

```

使用`@`符号可以获取数组中所有元素:

```
echo ${array_name[@]}
```

### 获取数组元素的个数

```
length=${#array_name[@]}

or

length=${#array_name[*]}

or

length=${#array_name[n]}
```

