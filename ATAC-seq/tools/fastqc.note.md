## fastqc 对原始测序reads质量控制

## 解读输出文件

打开html网页可以看到没一个图片的内容也可以打开zip压缩包，看具体每张图片

1. basic statistics

	![basic](https://upload-images.jianshu.io/upload_images/5256706-e98a6ab50dc85692.png?imageMogr2/auto-orient/strip|imageView2/2/w/843/format/webp)

	* filename: 指的是进行质量控制的文件名
	* encoding: 指测序平台版本和相应的编码版本号
	* sequence length: 指测序长度
	* %GC 是我们需要重点关注的一个指标，这个值表示的是整体序列中的GC含量，这个数值一般是物种特意的，比如人类细胞就是42%左右。
	*
	*
2. per base sequence quality 

	![quality](https://upload-images.jianshu.io/upload_images/5256706-abc4a2ad83739c74.png?imageMogr2/auto-orient/strip|imageView2/2/w/874/format/webp)

	* 横轴是测序序列第1个到第151个碱基，纵轴是质量得分，Q = -10*log10(error P) 即20表示0.01的错误率，30表示0.001错误率
	* 红线表示中值
	* 蓝色的线是各个位置的平均值连线
	* 注：
		1. warning 警报，如果任何碱基质量低于10,或者任何中位数低于25
		2. failure 报错，表示任何剪辑质量低于5,或者任何中位数低于20

3. per sequence quality scores

	![scores](https://upload-images.jianshu.io/upload_images/5256706-0d45fa507a5c1bd5.png?imageMogr2/auto-orient/strip|imageView2/2/w/858/format/webp)
	* 序列长度为151bp，每个位置的Q值的平均值就是这条reads的质量值。
	* *横轴是0-40,表示Q值*

	* *纵轴是每个值对应的reads数目*
	* 这个样本数据，测序结果主要集中在30 - 40,说明测序质量很好!

4. per base sequence content (碱基分布)

![content](https://upload-images.jianshu.io/upload_images/5256706-22f36cb8f38b9f32.png?imageMogr2/auto-orient/strip|imageView2/2/w/873/format/webp)


	* 横轴是1 - 151bp;纵轴是百分比;
	* 图中4条线代表A T C G,在每个位置平均含量
	* 理论上说，A与T是相等，G与C相等，但一般测序的时候，刚开始测序状态不稳定，很可能出现图上开头的情况。

5. per sequence GC content (序列平均GC含量分布图)

![GC](https://upload-images.jianshu.io/upload_images/5256706-c50274b9d014eb60.png?imageMogr2/auto-orient/strip|imageView2/2/w/857/format/webp)

	* 横轴是0 - 100%
	* 纵轴是每条序列GC含量对应的数量
	* *蓝色的线是程序根据经验分布给出的理论值，红色是真实值，两个应该比较接近才比较好*

6. per base N content (N统计含量)

![N content](https://upload-images.jianshu.io/upload_images/5256706-24e014b04ced7c8e.png?imageMogr2/auto-orient/strip|imageView2/2/w/877/format/webp)

	* 当测序一起不能分辨某条reads的某个位置是ATCG哪个碱基的时候，就会产生“N”，对所有reads的每个位置统计N的比率。
	* warning 警报，任意位置的N比率超过5%
	* failure 报错，如果任意位置N比率超过20%

7. sequence length distribution

![distribution](https://upload-images.jianshu.io/upload_images/5256706-3045d247b86d7664.png?imageMogr2/auto-orient/strip|imageView2/2/w/868/format/webp)

	* 每次测序一起测出来的长度理论上应该完全相等，但总会有一些误差
	* 例如： 途中151bp是主要的，但是有少量的150和152bp的长度
	* 当测序长度不同的时候，如果很严重，则表明测序仪器在此测序不成功。


8. sequence Duplication levels (重复序列)

![duplication](https://upload-images.jianshu.io/upload_images/5256706-40683823d5620ade.png?imageMogr2/auto-orient/strip|imageView2/2/w/861/format/webp)

	 
	* 统计序列完全一样的reads频率。横坐标是duplication的次数，总坐标是duplicated reads的数目。
	

9. kmer content

![kmer](https://pic4.zhimg.com/80/d36385723bfbe857c1d0516c622fc05f_720w.png)

	* 这个图统计的是，在序列中某些特征的短序列重复出现的次数
	* 我们可以看到1-8bp的时候图例中的几种短序列都出现了非常多的次数，一般来说，出现这种情况，要么是adapter没有去除干净，而又没有使用-a参数；要么就是序列本身可能重复度比较高，如建库PCR的时候出现了bias
	* 对于这种情况，我的办法是可以cut掉前面的一些长度，可以试着cut 5~8bp

