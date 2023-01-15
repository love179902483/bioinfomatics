## fasterq-dump

当然除了参数问题，还有一个让人诟病的地方就是他只能单个线程，所以速度特别的慢。尽管相对于下游分析要分析好几天而言，这点时间还能能等的。但是能快一点总是好的，所以在2018年的6月份，sra-tools更新了一个新的sra解压工具，fasterq-dump, a faster fastq-dump，它能利用临时文件和多线程加速从SRA文件提取FASTQ。


## 用法

`fasterq-dump --split-3 SRR5318040.sra`

此外还有建立了GitHub Wiki提供使用教程，参见https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump。



重点参数是`-e|threads`, 用于选择使用多少线程进行运行，默认是6个线程。 同时考虑到有些人容易着急，还提供了`-p`选项用于显示当前进度。

我用一个9G大小的SRA文件，分别以fastq-dump和fasterq-dump进行了测试。

```
time fastq-dump --split-3 -O test SRR5318040.sra
# 558.76s user 41.36s system 101% cpu 9:51.82 total
time fasterq-dump --split-3 SRR5318040.sra -e 20 -o SRR5318040
# 582.70s user 121.06s system 1130% cpu 1:02.25 total
```

对于我们而言，我们只要看最后的total部分，也就是实际花了多少时间。fastq-dump花了快10分钟，而fasterq-dump只需要1分钟，快了9倍多。


## 不足
最后还有一点不足之处：输出的fastq的ID目前暂时没有选项可以调整，需要自己写个脚本解决。

![示例](https://upload-images.jianshu.io/upload_images/2013053-1f2f341c7c534cb4.png?imageMogr2/auto-orient/strip|imageView2/2/w/497/format/web)
