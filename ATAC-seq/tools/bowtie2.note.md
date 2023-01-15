## [懒人文档](https://wenku.baidu.com/view/928364ae84868762cbaed524.html)

## 介绍
Bowtie2 是将测序reads与长参考序列比对工具。适用于将长度大约为50到100或1000字符的reads与相对较长的基因组（如哺乳动物）进行比对。Bowtie2使用FM索引（基于Burrows-Wheeler Transform 或 BWT）对基因组进行索引，以此来保持其占用较小内存。对于人类基因组来说，内存占用在3.2G左右。Bowtie2 支持间隔，局部和双端对齐模式。可以同时使用多个处理器来极大的提升比对速度。


如果目的是对齐两个非常大的序列（例如两个基因组），请考虑使用MUMmer。如果目的是与相对较短的参考序列（如细菌基因组）非常灵敏的比对，可以使用Bowtie 2完成，但您可能需要考虑使用NUCmer，BLAT或BLAST等工具。当参考基因组很长时，这些工具可能会非常缓慢，但当参考基因组很短时通常就足够了。




* 对参考序列构建index

`$ bowtie2-build genome.fasta index`

* 尝试使用前1000个reads进行比对
    `$ bowtie2 -u 10000 -p 8 -x index -1 reads1.fq -2 read2.fq -S out.sam`

* 使用8个线程进行比对 

    `$ bowtie2 -p 8 -x index -1 read1.fq -2 reads2.fq -S out.sam` 

* 比对的sam结果中添加了read group信息


* 单末端
    `bowtie2 -p 10 -x genome_index -U input.fq | samtools sort -O bam -@ 10 -o - > output.bam`


* 双末端 
    `bowtie2 -p 10 -x genome_index -1 input_1.fq -2 input_2.fq | samtools sort -O bam -@ 10 -o - > output.bam`


> 注：genome_index指的是用于bowtie2索引文件，而不是参考基因组本身，genome_index需要指定路径及其共用文件名，例如:我的放在 /data/bowtie/目录下，但需要输入的参数为/data/bowtie/mm10.最后一个mm10指的是共用文件名。


### 参数

	1. -x :参考基因组索引的基名，基名是索引文件的名称，但不包含最终的.1.bt2  / .rev.1.bt2 等。bowtie2在当前目录中首先查找指定的索引，然后在BOWTIE2_INDEXES环境变量中制定的目录中查找。
	2. -1 用逗号分隔的包含read1的文件列表。如: -1 flyA_1.fq,flyB_1.fq。使用此选项指定的序列必须与文件中的文件和读取的文件一致。
	3. -2 用逗号分割的包含read2的文件列表。如：-2 flyA_2.fq,flyB_2.fq。
	4. -U  逗号分割的包含未配对读取文件列表要对齐，例如 lan1.fq,lane2.fq,lane3.fq,lane4.fq。读书可能是不同长度的混合。
	5. -S 将SAM对齐文件写入，默认情况下，对其被写入“标准输出”或”标准输出“文件句柄(控制台)。 

	6. 构建索引

		bowtie2-build mm10.fa mm10
