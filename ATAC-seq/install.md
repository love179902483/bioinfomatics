## 安装miniconda3 

1. 镜像下载： 
	* [官网](https://docs.conda.io/en/latest/miniconda.html) 
	* [清华镜像](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/) 

2. 安装镜像
	
	bash 已经安装的镜像

3. 添加环境变量并刷新bash
	source ~/.bashrc
4. 创建环境
	* conda create -n atac python=2 bwa
		* atac: 环境名称 
		* python=2: 环境使用的python版本
		* bwa: 新建环境之后安装的软件
		* -n 指定环境名称
5. 激活环境
	* source activate atac


6. 在激活的环境中安装包

```
bedtools
sra-tools
deeptools
homer
meme
macs2
bowtie
bowtie2
```

7. 下载测试数据

```
2-cell-1 SRR2927015 
2-cell-2 SSR2927016 
2-cell-5 SSR3545580
2-cell-4 SSR2927018
```

8. pcr重复，线栗体染色体
