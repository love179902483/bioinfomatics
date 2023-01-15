* illumina 刚下机的数据未bcl格式文件,但下游分析一般都要fastq格式文件，所以在进行下游分析之前，需要将bcl格式的文件根据每个样本之前田间的Index分出，并转为fastq文件。

## fastq
  * 通常我们可以将测序数据分为**双端测序**和**单端测序**双端测序的数据含有两个fastq格式的文件，单端测序的数据只含有一个fastq格式的文件
  * fastq是基于文本的，保存生物序列(通常为核酸序列)和其测序质量信息的标准格式。其序列以及质量信息都是使用一个ASCII字符标识，目的是将fasta序列与质量数据放到一起，目前已成为高通量测序结果的实施标准。
  * fastq一般有4行：
    1. 第一行：必须以"@"开头，后面跟着唯一的序列ID标识符，然后跟着可选的序列描述内容，标识符与描述内容用空格分开。
    ![例如](https://img-blog.csdnimg.cn/20190413174056863.png)
    2. 第二行：序列字符(核酸为[AGCTN]+，蛋白未氨基酸字符);
        * 核苷酸序列信息，我们一般使用下面的对应表

        * ![对应表](https://img-blog.csdnimg.cn/20190413172954362.png)

    3. 第三行：必须以"+"开头，后面跟着可选的ID标识符和可选的描述内容，如果"+"后面有内容，该内容必须与第一行"@"后面内容相同。
    4. 第四行：碱基质量字符，每个字符对应第二行相应位置碱基或者氨基酸的质量(phred值越大说明测序质量越好)。该字符可以按照一定规则转换为碱基质量得分，碱基质量得分可以反映该碱基的错误率。这一行的字符数与第二行中的字符数必须相同。

    ```
        @HWI-ST1223:80:D1FMTACXX:2:1101:1243:2213 1:N:0:AGTCAA
        TCTGTGTAGCCNTGGCTGTCCTGGAACTCACTTTGTAGACCAGGCTGGCATGCACCACCACNNNCGGCTCATTTGTCTTTNNTTTTTGTTTTGTTCTGTA
        +
        BCCFFFFFFHH#4AFHIJJJJJJJJJJJJJJJJJIJIJJJJJGHIJJJJJJJJJJJJJIIJ###--5ABECFFDDEEEEE##,5=@B8?CDD<AD>C:@>
        @HWI-ST1223:80:D1FMTACXX:2:1101:1452:2138 1:N:0:AGTCAA
        NTCTAGGAGGTCTAGAAAGCCCAGGCCACCGGTACAAACATCAAGGGTGTTACGGATGTGCCGCTCTGAACCTCCAGGACGACTTTGATTTCAACTACAA
        +
        #4=DFFEFHHHHHJJJJJIJJJJHIIJGJJJJ@GIIJJJJJJIJJJJFGHIIIJJHHHDFFFFDDDDDDDDDDDDCDDDDDDDDDDDCCCEDEDDDDDDD 
    ```
  * 每个碱基的质量值与错误率之间的关系:

    > 其中P代表该碱基被测序错误的概率，如果该碱基测序出错的概率为0.001，则Q应该为30,那么30+33=63,那么63对应ASCII码为"?",则在第四行中碱基对应的质量代表值为"?"

    ```
        print(ord("?))
    ```

    ```
       63 
    ```
  * FASTQ质量值的计算方法

    p值：测序错误概率 error probility;测序仪根据荧光信号强弱会给出一个参考值。

    `Q = -10*log10(P)`

    `Phred = Q+33/64(illumina: + 33)`

    Phred对应的ASCII字符对应到这个碱基

    * *个版本不同Phred对应的ASCII的值*
    > 在计算Q值和加上33/64的时候，不同测序仪，产生的数据不同，大概如下所示:

      * Solexa标准

      ![Solexa标准](https://img-blog.csdnimg.cn/20190413174440145.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY0OTMzMQ==,size_16,color_FFFFFF,t_70)

      * Illumina标准

      ![illumina标准](https://img-blog.csdnimg.cn/20190413174440145.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY0OTMzMQ==,size_16,color_FFFFFF,t_70)

        * 不同测序仪的不同Phred值对应的ASCII表

      ![ASCII表](https://img-blog.csdnimg.cn/20190413174629820.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY0OTMzMQ==,size_16,color_FFFFFF,t_70)
## FASTA

> fasta格式也成为pearson格式，是一种基于文本用于表示核苷酸序列或者氨基酸序列的格式。在这种格式中碱基对或氨基酸用单个字母来编码，且允许在序列前添加序列名称及注释。

* fasta格式首字母以大于号 ">" 开头，接着是序列的标识符；换行后是序列的描述信息。文件每行的字母一般不应该超过80个字符。序列中允许存在空格，换行，空行，知道下一个大于号或者文件结束，表示该序列结束。
```
>gi|46575915|ref|NM_008261.2| Mus musculus hepatic nuclear factor 4, alpha (Hnf4a), mRNA
GGGACCTGGGAGGAGGCAGGAGGAGGGCGGGGACGGGGGGGGCTGGGGCTCAGCCCAGGGGCTTGGGTGG
CATCCTGGGCCGGGCAGGACAGGGGGCTAAGGCGTGGGTAGGGGAGAATGCGACTCTCTAAAACCCTTGC
CGGCATGGATATGGCCGACTACAGCGCTGCCCTGGACCCAGCCTACACCACCCTGGAGTTTGAAAATGTG
CAGGTGTTGACCATGGGCAATGACACGTCCCCATCTGAAGGTGCCAACCTCAATTCATCCAACAGCCTGG
GCGTCAGTGCCCTGTGCGCCATCTGTGGCGACCGGGCCACCGGCAAACACTACGGAGCCTCGAGCTGTGA
CGGCTGCAAGGGGTTCTTCAGGAGGAGCGTGAGGAAGAACCACATGT
```

* 使用人类训红蛋白a亚基对应的mRNA序列，这个序列是从NCBI RefSeq数据库下载的

```
    >gi|13650073|gb|AF349571.1| Homo sapiens hemoglobin alpha-1 globin chain (HBA1) mRNA, complete cds
    CCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGACGACAAGACCAACGTCAAGGCCGCCTGG
    GGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCA
    CCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAA
    GGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGC
    GACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGA
    CCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTC
    TGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTTG

```
从第一行来看：
![解释](https://img-blog.csdnimg.cn/20190413172512249.png)



![cds区域](https://img-blog.csdnimg.cn/20190413172623832.png)


> gi号具有唯一性
 
