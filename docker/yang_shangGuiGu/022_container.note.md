
# 将数据从容器内拷贝到主机上
> docker cp [container ID]:[container path] [target path]

# 导入和导出内容
## export 导出容器的内容留做一个tar归档文件
> docker export [container ID] > name.tar
## import从tar包中内容创建一个新的文件系统作为导入的镜像
> cat name.tar | docker import - container_name:images_tag



