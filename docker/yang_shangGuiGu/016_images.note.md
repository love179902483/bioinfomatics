
# docker iamges 

* -a:列出所有镜像 
* -q:只显示镜像ID

# docker search <image name>
> --limit N:只列出N个镜像，默认25
# docker pull <image name>[:TAG]
> 不写[:TAG]默认使用:latest 
# docker system df
> 查看镜像/容器/数据卷所占用的空间
# docker rmi <ID>
# docker image prune
> 删除虚悬镜像
> 虚悬镜像:也就是repository 和 tag都是 none的镜像
# docker rmi -f $(docker images -qa) 
> 删除所有镜像--慎重,当然需要注意如果是ubuntu需要使用sudo，像这样`sudo docker rmi -f $(sudo docker images -q)`



