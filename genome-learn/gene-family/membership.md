
# 基因家族成员鉴定

## 数据下载

### 系统数据库
1. [phytozome](https://phytozome-next.jgi.doe.gov/)
2. [ensembl](https://plants.ensembl.org/index.html)

## 物种数据库
1. [maizegdb](https://maizegdb.org/)
2. [wheat](https://wheatgenome.org/)


## 基因家族特征分析
1. 基因结构分析
[GSDS](http://gsds.gao-lab.org/)

2. Motif 分析
Motif是一段典型的序列或者一个结构。一般来说，我们称为基序。一般情况下是指构成任何一种特征序列的基本结构。通俗来讲，即是有特征的短序列，一般认为它是拥有生物学功能的保守序列，可能包含特异性的结合位点，或者是涉及某一个特定生物学过程的有共性的序列区段。比如蛋白质的序列特异性结合位点，如核酸酶和转录因子。
[MeMe](https://meme-suite.org/)

![avatar](https://picx.zhimg.com/v2-5415cb079bbec8a89f767ef50de379cb_1440w.jpg?source=172ae18b)

3. 亚细胞定位分析
[SoftBerry](http://linux1.softberry.com/berry.phtml)
ProteinLocation > ProtComp

4. 染色体定位分析
[MG2C](http://mg2c.iask.in/mg2c_v2.1/index.html)


5. 基因复制分析
[MCScan](https://github.com/tanghaibao/jcvi/wiki/MCscan-(Python-version))


## 基因家族进化分析
1. 系统进化树构建
    * 序列集合选择: 
        * 该物种基因家族
        * 属内、科内近源物种基因家族
        * 模式物种基因家族
    * **保守结构域**系统进化树
    * **全场蛋白序列**系统进化树
    * ClustalW 氨基酸序列多重比对
    * MEGA
2. 系统进化树美化
[Itol](https://itol.embl.de/)



## 基因家族表达分析
1. 数据选择
    * 不同组织表达分析： 根、茎、叶、花、果实、籽粒等;
    * 不同特异表达分析： 发育2d、4d、6d、8d;
    * 不同处理表达分析： 干旱、盐、真菌处理前后等;

2. 数据类型-表达量数据
    * 自测转录组数据: 提取基因家族表达量。
    * 公共数据-表达量: NCBI-GEO数据库，提供FPKM(标准化后表达量，可直接使用) 或者 Reads Counts文件(需要转化为FPKM等);
    * 公共数据-表达量: NCBI-SRA数据库，转录组测序的原始数据，需要进行转录组标准分析，得到FPKM文件;
    * 如无需数据，需要设计实验，进行荧光定量分析;

3. 分析结果呈现-聚类热图、柱状图等
    * [HeatMapper](http://heatmapper.ca/)

4. WGCNA基因共表达网络构建

