## 查看linux服务器的cpu核心个数

1. 查看逻辑CPU个数:

```
#cat /proc/cpuinfo |grep "processor"|sort -u|wc -l
```

2. 查看物理CPU的个数:
> 物理CPU就是计算机上实际配置的CPU个数。在linux上可以打开cat /proc/cpuinfo 来查看，其中的physical id就是每个物理CPU的ID，你能找到几个physical id就代表你的计算机实际有几个CPU。

```
#grep "physical id" /proc/cpuinfo|sort -u|wc -l
#grep "physical id" /proc/cpuinfo|sort -u


physical id : 0
physical id : 1
```

3. 查看每个物理CPU内核个数:
```
#grep "cpu cores" /proc/cpuinfo|uniq


cpu cores : 6
```

4. 每个物理CPU上逻辑CPU的个数:
```
#grep "siblings" /proc/cpuinfo|uniq


siblings : 12
```

5. 判断是否开启了超线程：

如果多个逻辑CPU的"physical id"和"core id"均相同，说明开启了超线程
或者换句话说
逻辑CPU个数 > 物理CPU个数 * CPU内核数 开启了超线程
逻辑CPU个数 = 物理CPU个数 * CPU内核数 没有开启超线程


## CPU 个数、内核数、线程数的区别

CPU主频就是CPU运算时的工作频率，在单核时间它是决定CPU性能的重要指标，一般以MHz和GHz位单位，如Phenom II X4 965主频是3.4GHz。说到CPU主频，就不得不提外频和倍频的概念，它们的关系是：主频=外频×倍频。

        虽然提高频率能有效提高CPU性能，但受限于制作工艺等物理因素，早在2004年，提高频率便遇到了瓶颈，于是Intel/AMD只能另辟途径来提升CPU性能，双核、多核CPU应运而生。

        其实增加核心数目就是为了增加线程数，因为操作系统是通过线程来执行任务的，一般情况下它们是1:1对应关系，也就是说四核CPU一般拥有四个线程。但Intel引入超线程技术后，使核心数与线程数形成1:2的关系，如四核Core i7支持八线程(或叫作八个逻辑核心)，大幅提升了其多任务、多线程性能。


* cpu个数是指物理上安装了几个cpu，一般的个人电脑是安装了1个cpu

* cpu内核数是指物理上，一个cpu芯片上集成了几个内核单元，现代cpu都是多核的。

* cpu线程数是指逻辑上处理单元，这个技术是Intel的超线程技术，它让操作系统识别到有多个处理单元。

如下图所示：插槽指cpu个数，内核数量是4个，线程数是4个。我的I5 4590 cpu不支持超线程技术。所以，一个内核就是一个线程

![picture](https://img-blog.csdnimg.cn/20190706101735606.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FnYW5saWFuZw==,size_16,color_FFFFFF,t_70)