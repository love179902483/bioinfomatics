# 提交容器副本使之成为一个新的镜像
> docker commit -m="discription info" -a="author" [conainer ID] [created image name]:[tag]

## 从hub上下载的ubuntu镜像是不带vim命令的
> 从hub上下载的ubuntu镜像是不带vim命令的，但是如果在外网联通的情况下安装vim，安装完成后，commit自己的新镜像，启动我们的新镜像并且和原来的对比，发现新的镜像是有vim命令的。

