## NGS接头是如何添加上的，以及如何去接头

我见过的相当一部分人，做质控时，一般也就就是跑个实验室或者公司的祖传代码，但对于软件所做的操作不求甚解，归根结底，是因为对测序流程中，接头是怎么加上去的不太了解。


现在我们接触的大多数二代测序数据，都是来自于illumina测序平台。这其中，大多数illumina文库的构建，是通过将接头连接到fragment DNA/cDNA的两端（但是Nextera方法除外，因为技术相对不常见，这里不深入展开）。 下图是一张很经典的加接头的示意图。

![示意图](https://pic4.zhimg.com/80/v2-aa6a01141ff7744bdc4156e035143a93_720w.jpg)


### 大体分为以下几个步骤。

* 用酶或者激光或者超神波将DNA或者RNA发转得到的双链cDNA打断成小片段。
* 打断是随机打断的，有可能末端不平整，还需要酶补平。
* 补平之后需要在3'端加上A碱基。
* 加上A之后，再加上adapter



这时候我们大概有点B数，但是依然不知道adapter具体是怎么加上去的，也并不知道接头中，read1、sequncing primer、index、read2 sequencing primer，以及index sequencing primer到底在接头的什么地方。

我们看看下面这张
![示意图](https://pic2.zhimg.com/80/v2-98290b3ba946d70dcf3f2d1638ae9cf1_720w.jpg)


看上面的两张图，好像是在fragment DNA 两端直接加上了一个Y字型的引物，他们被人称为Full Y-adapter或者forked adapter。

illumina官网有一下一点点介绍

![示例图](https://pic1.zhimg.com/80/v2-601e1d974a52a97600cfb3229d66e0ec_720w.jpg)

从图中我们看到，在'接头'添加之前，街头上好像已经有另一个叉形的接头了，难道Y型接头不是直接添加到DNA fragment上的吗？


其实这是两种不同的indexing strategy导致的差异，而这两种strategy的示意图，如下
![示意图](https://pic3.zhimg.com/80/v2-815463cd17ad105115f6c8440c43ea66_720w.jpg)

*左边的是直接在fragment DNA的两端直接加上full Y-adapter*, adapter中已经包括了和P5/P7 oligo互补的序列, index, 以及Read1/Read2的测序引物。

*一句话总结，这两种不同的indexing strategy的差别在于引入index序列的时机和方式不一样。*

其实右边的图并不是画的特别形象，具体的的可以参看下面这张图
![示意图](https://pic1.zhimg.com/80/v2-0abfd5500a3559cb71003b6ca4322b50_720w.jpg)



在这里我们能够清楚地看到，这种接头添加过程中，fragment DNA两端是先连上PE adapter, 然后再通过PCR引入的region complementary to P5/P7 sequence, index, and sequencing biding sites.


## 去接头代码
`cutadapt --times 1 -e 0.1 -O 3  -m 30 -q 25,25 -u 8 -a AGATCGGAAGAGC -A AGATCGGAAGAGC  -o trimmed.1.fastq.gz -p trimmed.2.fastq.gz  reads.1.fastq.gz reads.2.fastq.gz
`


<video id="video" controls="" preload="none" poster="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.jpg">
<source id="mp4" src="https://video.zhihu.com/video/964658526447198208?autoplay=false&useMSE=">
</video>

