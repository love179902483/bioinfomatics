
## samtools 使用与安装

由于二代测序中普遍采取短读长(50~140)的测序策略，在后续分析流程中需要使用比对软件将reads片段匹配到参考基因组中，从而产生比对/匹配文件，进而用于后续流程的分析。

samtools是用来处理 *sam/bam* (sam的二进制格式，用于压缩空间）格式的比对文件工具，它能够输入和输出sam格式文件，对其进行排序、合并、建立索引等处理。samtools与2009年由Li Heng发表在期刊BIOINFORMATICS上，被广泛应用与二代测序分析流程中。



## function & command | 功能与命令

1. faidx: index/extract FASTA

本命令对参考基因组的fasta文件建立索引文件，生成的文件以.fai后缀结尾。

`$ samtools faidx ref.fasta`

2. sort: sort alignment file

本命令对bam文件中的序列进行排序，默认是按照序列在fasta文件中的顺序(即header)和序列从左往右的位点排序。

`$ samtools sort [-T out.prefix] [-@ threads] [-m maxMem] [-o out.sorted.bam][in.bam]`

* -T prefix: 把临时文件写到prefix.bam里面。这个参数是必须的
* -@ int: 设置排序和压缩的线程数，默认是单线程。
* -m int: 设置每个线程的最大内存，以bytes为单位设定或者添加 K，M，G后缀。
* -o file: 将最后拍好序的数据输入到file中，而不是标准输出。

```
$ samtools sort abc.bam abc.sort
$ samtools view abc.sort.sort.bam | less S
```

3. merge: merge sorted alignments

本命令将多个排好序的bam比对文件进行合并，产生一个拍好序的bam输出文件(合并后的文件不需要进行sort),这个文件包含了所有的输入记录，并且保留了他们原来的顺序。

`$ samtools merge [out.bam] [in1.bam] [in2.bam] [in3.bam]`

4. index: index alignment

本命令对bam文件建立索引并产生.bai文件，用于快速的随机处理。很多后续分析过程需要bai文件的存在，特别是显示序列比对情况下，比如samtool的tview命令。

`samtools index aln.sorted.bam`

5. view: sam <-> bam <-> cram conversion

* 本命令将sam文件转化为bam文件;然后对bam文件进行各种操作，比如数据的排序和提取(这些操作是对bam文件进行的，不能对sam文件进行该操作);最后将排序或提取得到的数据输出为bam或者sam格式。
* bam文件优点:bam文件为二进制，占用磁盘空间比sam文件小,利用bam二进制文件的运算速度快。


```
$ samtools view -b abc.sam > abc.bam
$ samtools view -b abc.sam -o abc.bam
$ samtools view -bS abc.sam > abc.bam
$ samtools view -b -S abc.sam -0 abc.bam
```

```
# 提取比对到参考系上的比对结果
$ samtools view -bF 4 abc.bam > abc.F.bam

# 提取paired reads 中两条reads都比对到参考序列上的比对结果,只需要将4+8的值12作为过滤参数即可
$ samtools view -bF 12 abc.bam > abc.F12.bam

# 提取没有比对到参考序列上的比对结果
$ samtools view -bf 4 abc.bam > abc.f.bam

# 提取bam文件中比对到caffold1上的比对结果,并保存到sam文件格式中
$ samtools view abc.bam scaffold1 > scaffold1.sam

# 提取scaffold1上能比对到30k到100k区域的比对结果
$ samtools view abc.bam scaffold1:30000-100000 > scaffold1_30k-100k.sam

# 根据fasta文件，将header加入到sam或bam文件中
$ samtools view -T genome.fasta -h scaffold1.sam > scaffold1.h.sam
```


## 什么叫随机访问
简单来说就是访问染色体任何一个位置的比对情况，速度差不多，而不受染色体先后顺序的影响，比如按照顺序访问chr2数据，就必须先读chr1，chr2的数据；而一点我们对BAM文件进行了sort，同时建立了BAM文件的index，那么就可以直接访问chr3的数据。

## BAM文件排序以及建立Index?
使用samtools sort就好！注意，samtools sort是可以按照reads的名称或者reads的mapping结果进行排序的，我们这里要注意，需要按照mapping结果进行排序，也就是染色体5'端的reads在前，靠3'端的reads在后。

在sort完成后，需要使用samtools index 进行建立index, BAM index的名字为BAM文件后加.bai

```
# 对SAM文件转为BAM文件
samtools view -hb ./test.sam > test.bam

# 对BAM文件按照mapping结果进行排序
samtools sort -O BAM -T test_sort.bam.tmp -o test_sort.bam 

# 对BAM文件建立Index
samtools index test_sort.bam test_sort.bam.bai
```

## 对samtools tview的使用

```
# samtools tview 用法
samtools tview test_sort.bam ref.fa

```
这里可以按 ？ 呼出帮助菜单

里面功能主要是方便我们快速定位，如：按"g"进行快速定位，如：我们定位到chr1:12500



## 去除线粒体reads

`samtools view -h -f 2 -q 30 Control.sambamba.rmdup.bam |grep -v chrM |samtools sort -O bam -@ 5 -o -> Control.last.bam `
