


#### fibroblast n.纤维细胞
#### myeloid    adj.骨髓的
#### endothelial adj.内皮的 n. 内皮细胞
#### lymphocyte  n. 淋巴细胞
#### erythrocytes n. 红细胞
#### dendritic adj. 树突状
#### dendritic cell 树突状细胞

> Visium 空间转录组是把切片在芯片上展开，在空间上用条形码来保留切片上每个小店的空间位置信息


> 几千个spts通过聚类被划分为几个或者十几个，二十几个cluster(簇),方便人脑识别，也方便接下来进行分析

* PCA(Principal Component Analysis)



* Seurat软件(Graph Base Louvain Cluster) 可以用这个方法进行聚类 

* t-SNE 降维展示(t-distributed stochastic neighbor embedding)

* UMAP图(Uniform Manifold Approximation and Projection)

    > UMAP除了可以把spot以聚类的方式表现出来外，还可以表现出细胞分化的轨迹,如果两个簇的细胞是从同一个来源分化出来的，那么UMAP就会把他们放到相邻的位置,有利于发现细胞分化树的信息。


    > 但是t-SNE出现的比较早，有很多人习惯用t-SNE,我们就在我们报告中保留了t-SNE和UMAP两种图

* nFeature_Spatial图
    1. 首先它是基于t-SNE图的，用来表示一个spot钟有多少个基因的表达被检测到。
    2. 表达的基因越多，则颜色越红。
    3. 一般而言，一个细胞中能表达的基因数量越多，往往表示这个细胞的分化程度越低。
    4. 一个细胞中能表达的基因数量越少，则这个细胞的分化程度越高。
    5. 也就是说红色的部分分化程度低而灰色的spot可能其中细胞分化程度高。但这不是一定的，因为每个spot中有多少个细胞是不确定的。

* nCount_Spatial

* Loupe Brower 可以将以上这些归纳成簇的spot还原到切片的空间位置上 

* spot群相关性热图
* 群特异表达基因的热图
    1. 横轴是按簇被组织起来的spot
    2. 每一条纵列，就是一个spot
    3. 每一块纵向的块，就是一个簇
    4. 纵轴商，是一个一个的基因 
    5. 黄色表示高表达，紫色表示底表达


* 基因UMI？？

* GO数据库(gene ontology): Go数据库是按照三个大方向对基因进行描述的。
    1. 细胞组件(Cellular Component, CC)
    2. 分子功能(Molecular Function, MF)
    3. 生物过程(Biological Process, BP)

* 显著富集散点图
* 显著富集Go节点与候选基因网络图

* KEGG(kyoto Encyclopedia of Genes and Genomes) : 京都基因与基因组百科全书

* STIRNG数据库