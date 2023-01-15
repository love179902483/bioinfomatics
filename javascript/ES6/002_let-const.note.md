# let 命令


## **基本用法**
ES6新增了`let`命令，用来声明变量。用法类似于var，但是声明的变量只能在`let`命令所在代码快中生效 
```javascript
    {
        let a = 10;
        var b = 1;
    }
    a // ReferenceError a is not defined.
    b // 1
```
以上代码在使用`let`与`var`声明变量之后，在代码块作用域外使用其中`let`声明的调用时候出错而`var`声明调用后的则正确，说明在代码快之外`let`声明的变量已经不生效了。
也是因为这个特性，`js`中`for`循环很适合用`let`命令。

```javascript
for(let i = 0; i < 10; i++ ){
    //...
}
console.log(i)
// ReferenceError i is not defined

for(var k = 0; k < 10; k++){
    // ...
}
console.log(k);
// 10
```
由于`let`作用域的原因`for`循环之外没有`k`的定义故结果为`undefined`而`var`在全局定义所以结果是`10`。		

```javascript
var a =	[]
for(let i = 0; i < 10; i++){
    a[i] = function(){
        console.log(i);
    }	
}
a[5]();
// 10
```  

由于`var`属于全局作用域故结果输出为`10`。

```javascript
var a = []
for(let i = 0; i < 10; i++ ){

    a[i] = function(){
        console.log(i);
    }
}
a[5]();
// 5
```  

以上代码中，变量`i`是`let`声明 的，当前的`i`只有在本轮有效，所以每次循环`i`都是不一样的的新变量，所以最后输出为5。那么若每次循环的变量`i`都会重新声明，那么它是如何记忆上一轮的值？这是因为`javascript`引擎会记住上一轮的值，初始化本轮的值`i`时候，就在上一轮的基础上进行计算。  

```javascript
for (let i = 0; i < 10; i++){

    let i = "abc";
    console.log(i);
}

// abc
// abc
// abc

```
`for`循环有一个特别之处就是，在设置循环变量那一部分是父作用域，而循环体外则是单独的子作用域。

## **`let`不存在变量提升**
`var`命令会发生变量提升的现象，即变量在声明之前就可以使用，值为`undefined`。这多多少少有些奇怪。所以为了纠正这一现象，`let`命令改变了语法行为，变量需要在声明子后才能使用，否则报错。
```javascript
//var
console.log(test01);
// undefined
var test01 = 2;

//let 
console.log(test02);
// ReferenceError
let test02;

```
## **暂时性死区(temporal dead zone , TDZ)** 
```javascript
var a = 10;
var b = 20;
if(true){

    console.log(b);
    console.log(a);
    let a = 300;
}
// 20 
// ReferenceError

if(true){
    // TDZ 开始 
    tmp = 'abc';    // ReferenceError 
    console.log(tmp);// ReferenceError

    let tmp; // TDZ 结束
    console.log(tmp);//undefined

    tmp = 123;
    console.log(tmp);// 123
}

```
只要块及作用域内的变量被`let`定义，那么这个变量就绑定了这个区域，不再受外部影响。上面的变量`a`,`b`在全局作用与中使用`var`定义，但是在以下块及作用域中，`a`被`let`定义，所以变量`a`就绑定在了下面的作用域中，不受其他作用域影响。故相当与在单独的块及作用与中变量`a`未声明就使用，所以会报错。
`ES6`明确规定，如果区块中存在`let`与`const`命令，这个块及作用域所声明的变量从一开始就形成了一个封闭的区域，凡是在声明之前使用这个变量，就会报错。
总之，在代码块中，使用`let`生命的变量之前，该变量都是不可用的。语法上叫**暂时性死区**

所以，目前`typeof`不再是一个百分百安全的操作，例如：

```javascript
typeof x;// ReferenceError
let x;

typeof y;// undefined
```
所以在使用`let`之前`typeof`操作是百分百安全的。
另外还要注意以下两种情况，例如：

1. 第一种 

```javascript
function bar(x = y, y = 2){
    return [x, y];
}
bar(); 
//  ReferenceError 

function bar2(x = 2, y = x){
    return [x, y];
}
bar2();
// [2, 2]
```  

---

2. 第二种

```javascript
// 不报错
var x = x;

// 报错
let x = x; 
```  

总之，暂时性死区的本质就是，只要一进入当前作用域，所要使用的变量就已经存在了，但是不可获取，只有等到声明变量的那一行代码出现，才可以获取和使用该变量。  

## **不允许重复声明** 
`let` 不允许在相同作用与内，重复声明一个变量。 
 
```javascript
// 报错 
function func1(){
    let a = 10;
    let a = 1;
}
func1();
// 报错

function func2(arg){
    let arg;
}
func2();
```  

## **`var`块及作用域**
为什么需要块及作用域?
`ES5`只有全局作用域与函数作用域，没有块及作用域，所以带来了很多不合理的场景。
1.  第一种

```javascript
var tmp = new Date();
function f(){

    console.log(tmp);
    if(false){

    
    }
}
```
2.  用来计数的循环变量泄露为全局变量。

```javascript
var s = 'hellow';
for(var i = 0; i < s.length; i++){

    console.log(s[i]);
}

console.log(i);
// 5
```
以上代码中按理说在最后一行的`console.log(i)`应该报错，但是可以看出，在`for`中的`i`并没有在循环结束后消失，而是泄露成了全局变量。


## **`ES6`的快级作用域** 

`let`实际上为`javascript`新增了快级作用域。

```javascript
function f1(){
    let n = 5;
    if(true){
        let n = 5;
    }
    console.log(n);
    //5
}

```
以上函数有连个代码快，都声明了变量`n`,运行后输出5,这表明内层代码快不影响外层代码块。如果两次都使用`var`定义变量`n`则最后输出为`10`

ES6允许作用域 的任意嵌套

```javascript
{
    {
    {
    {
        {
            let insane = "hello world";
        }
        console.log(insane);
        // referenceError
        }

    }
    }
}

```
如上，没一层都是一个单独的作用与。前一层的作用与无法读取上一层的作用域。
实际上块级作用域的出现使得广泛应用的匿名立即执行函数表达式不再必要了。
```javascript
(function(){
    var tmp = ...;
    ...
}())

//块级作用域写法
{
    let tmp = ...;
    ...
}

```
---

## **函数作用域与函数声明**

[这一篇帖子写的不错](https://juejin.cn/post/6844903971925000205)

---


# `const`命令

## 特点
1.  `const` 声明的是一个只读的常量。
2.  声明的时候必须初始化，不能留到以后赋值。
    ```javascript
    const fool;
    // SyntaxError: Missing initializer in const declaration
    ```
3.  `const`作用域与`let`命令相同，也就是说只能在块及作用域内有效。  
4.  `const`命令声明的变量也是不提升的，存在暂时性死区，有就是只能在声明后使用。
5.  `const` `let`不可重复声明。

## 本质
`const`实际上保证的不是变量值的改动，而是变量指向的那个内存地址所保存的数据不改动。对于简单的数据类型(数值、字符串、布尔值)，值就保存在变量指向的那个内存地址，因此等同于常量。但是对于复合型数据类型主要是"对象和数组"，变量指向的内存地址，保存的只是一个指向实际数据的指针，`const`只能保证这个指针是固定的，但是指向数据结构是不是改变了，就不能控制了，**因此将一个对象声明为常量需要小心**
```javascript
const foo = {};

// 为foo添加一个属性，可以成功
foo.prop = 123;

//为foo指向一个新对象，就会报错

foo = {};
// typeError: "foo" is read-only


const a = [];
a.push('hello');
a.length = 0;
//可执行
a = ['Dave']
//报错
```
若真的想冻结对象，应该使用`Object.freeze`方法
`Object.freeze`只能冻结外层对象，  
```javascript
const objectExample = {
    prop1: 20,
    prop2: "test"
};

// 默认情况下我们仍可以修改对象属性
objectExample.prop1 = 200;
console.log(objectExample.prop1)


//冻结对象
Object.freeze(objectExample);
objectExample.prop2 = "Alice";
console.log(objectExample);
// {prop1: 200, prop2:"test"}
```
想要全部冻结需要递归。
```javascript
const theObjext = {
    x: 1,
    z: 2,
    y: {
        a: 'test1',
        b: 'test2'
    }

}



const deepFreeze = (obj)=>{
    
    const propNames = Object.getOwnPropertyNames(obj);

    for(const name of proNames){
        const value = obj[name];

        if(value && typeof value === "object"){
            deepFreeze(value);
        }
    }

    return Object.freeze(obj);
}


deepFreeze(theObject);
theObject.y.a = 100;
console.log(theObject.y.a);
// test1

```


# 声明变量的六种方式
`ES5`中只有两种方式，`var`与`function`。在`ES6`中，添加了`let`和`const`，还有之后的`import`和`class`。所以`ES6`中变量声明一共有6种方式。

# 顶层对象的属性
顶层对象，在浏览器中是`window`对象，在`Node`里面是`global`对象。`ES5`之前顶层对象的属性与全局变量是等价的。

```javascript
window.a = 1;
a
//1

a = 2;
window.a
//2

```
上诉代码，顶层对象的属性值与全局变量的赋值是同一件事情。
顶层对象的属性与全局变量挂钩，被认为是`javascript`语言最大设计败笔之一。`ES6`为了改变这一点，并且为为了兼容性，`var`与`function`命令声明的全局变量一就是顶层对象属性，同时，另一方面也规定，`let`命令、`const`命令、`class`命令声明的全局变量，不属于顶层对象属性。也就是说从`ES6`开始全局变量逐步与顶层对象属性脱勾。

```javascript
var a = 1;
window.a
//a

let b = 1;
window.b
//undefined
```

同时顶层对象在各种实现里面是不统一的。
* 浏览器里面，顶层对象是`window`，但是`Node`与`Web Worker`没有`window`
* 浏览器和`Web Worker`里面，`self`也指向顶层对象，但是`Node`没有`self`
* `Node`里面，顶层对象是`global`，但是其他环境都不支持。




