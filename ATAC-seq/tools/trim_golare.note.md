## 使用trim_galore对数据进行质量控制-过滤

> cutadapt 软件可以对NGS数据进行质量过滤
> FastQC 软件可以查看NGS数据的质量分布
> trim_galore 将这两个软件封装到一起，使用起来更加方便


* Trim galore，是可以自动检测adapter
* 去除reads 3’端的低质量碱基 # 自动调用cutadapt
* 去除adapter序列 # 自动去除3’端的adapter,可以通过设定--Illumina，--small_rna，--nextera参数来指定对应的adapter类型
* 去除长度太短的序列 #通过设定--length参数，小于设定值被去除
* 其它过滤

## 说明

1. trim galore是对 FastQC和Cutadapt的包装
2. trim_galore适用于所有高通量测序，包括RRBS(Reduced Representation Bisulfite-Seq ), Illumina、Nextera和smallRNA测序平台的双端和单端数据。

3. 主要功能包括两步：

	1. 首先去除低质量碱基，然后去除3' 末端的adapter(如果没有指定具体的adapter，程序会自动检测前1million的序列）
	2. 对比前12-13bp的序列是否符合以下类型的adapter :
		* Illumina: AGATCGGAAGAGC # 如果输入参数 --Illumina,就会默认trimmed前13bp的adapter
		* Small RNA: TGGAATTCTCGG # 同上 如果输入参数 --small_rna,就会默认trimmed前12bp的adapter
		* Nextera: CTGTCTCTTATA # 同上 如果输入参数 --nextera,就会默认trimmed前12bp的adapter


> 对于单端测序数据，基本用法如下
> trim_galore --quality 20 -a AGATCGGAAGAGC --length 20 -o out_dir input.fq
> 其中-a后面可以跟着序列（-a AGATCGGAAGAGC）
> 对于双端测序数据，基本用法如下
> trim_galore --paired --quality 20 -a AGATCGGAAGAGC -a2 AGATCGGAAGAGC --length 20 -o out_dir R1.fq.gz R2.fq.gz

## 参数说明

> --quality/-q<INT>：设定Phred quality score阈值，默认为Phred 20 切除质量得分低于设定值的序列

> --phred33/64：使用ASCII+33/64质量得分作为Phred得分选择-phred33或者-phred64，表示-测序平台使用的Phred quality score。
（需要确认:anger/Illumina 1.9+ encoding为33; Illumina 1.5 encoding为64）
> --adapter/-a ：输入adapter序列。也可以不输入，Trim Galore!会自动寻找可能性最高的平台对应的adapter。自动搜选的平台三个，也直接显式输入这三种平台，即--illumina、--nextera和--small_rna。

> -s/--stringency<INT>：设定可以忍受的前后adapter重叠的碱基数，默认为1（非常苛刻）。可以适度放宽，因为后一个adapter几乎不可能被测序仪读到。

> --length<INT>：设定输出reads长度阈值小于设定值会被抛弃，默认值20bp；即小于20bp的被去除。注意，在pe150下，不要设置太高，可以50或36（默认20）

> --max_length : 设置长度大于此值被丢弃


> -e <ERROR RATE> ：默认0.1


> --paired：对于双端测序结果，一对reads中，如果有一个被剔除，那么另一个会被同样抛弃，而不管是否达到标准。


> --retain_unpaired：对于双端测序结果，一对reads中，如果一个read达到标准，但是对应的另一个要被抛弃，达到标准的read会被单独保存为一个文件。

> --gzip和--dont_gzip：清洗后的数据zip打包或者不打包。


> -o/--output_dir：输入目录 [需要提前建立目录，否则运行会报错]。


> -- trim-n : 移除read一端的reads


> -j :使用线程数, 注意假设已使用Python 3并安装了Pigz，那么内核设置为4，实际使用内核是15，因此，最高设为4.


> --fastqc #当分析结束后，使用默认选项对结果文件进行fastqc分析



