## `这个文件是对白冰老师给的文档的阅读笔记。`

## Generating FASTQs with cellranger-atac mkfastq


### Overview

  The cellranger-atac workflow starts by demultiplexing the Illumina® sequencer's base call files (BCLs) for each flowcell directory into FASTQ files. 10x recommends using `cellranger-atac` mkfastq, a pipeline that wraps bcl2fastq from Illumina® and provides a number of convenient features in addition to the features of bcl2fastq:


> + demultiplex 解复用
> + wrap 包裹


* Translates 10x sample index set names into the corresponding list of four sample index oligonucleotides. For example, well A1 can be specified in the samplesheet as SI-NA-A1, and `cellranger-atac mkfastq` will recognize the four oligos AAACGGCG, CCTACCAT, GGCGTTTC, and TTGTAAGA and merge the resulting FASTQ files.

    > + samplesheet 样本表
    > + oligos 寡核苷酸 (oligonucleotide)

* Supports a simplified CSV samplesheet format to handle 10x use cases.
* Generates sequencing and 10x-specific quality control metrics, including barcode quality, accuracy, and diversity.

* Supports most `bcl2fastq` arguments, such as `--use-bases-mask`.

### Example Workflows

  In this example, we have two 10x libraries (each processed through a separate Chromium chip channel) that are multiplexed on a single flowcell. Note that after running `cellranger-atac mkfastq`, we run a separate instance of the pipeline on each library:

> + chromium chip channel 铬芯片通道


![picture1](https://support.10xgenomics.com/img/cellranger-atac-workflows/mkfastq_1.png)


In this example, we have one 10x library sequenced on two flowcells. Note that after running `cellranger-atac mkfastq`, we run a single instance of the pipeline on all the FASTQ files generated:

![picture2](https://support.10xgenomics.com/img/cellranger-atac-workflows/mkfastq_2.png)

## Arguments and Options
