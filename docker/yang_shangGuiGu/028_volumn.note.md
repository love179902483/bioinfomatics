# Docker挂载主机目录访问出现cannot open directory.:Permission denied
> 解决方法，在挂载目录后多加一个--privileged=true参数

# 卷的设计摸底就是数据持久话，完全独立与容器的生存周期，因此Docker不会在容器删除的时候删除其挂挂载的数据卷

> `docker run -it --privileged=true -v [absolute path of source mechine]:[absolute path of container mechine] image_name:tag`

# 特点

* 数据卷可以在容器之间共享和重用数据
* 卷的更改可以直接实时生效
* 数据卷中的更改不会包含在镜像中的更新
* 数据卷的生命周期一直持续到没有容器使用他为止


# 查看已经启动容器所挂载的目录，及其他信息
> docker inspect [container ID]`

# 容器数据卷可读可写
> `docker run -it --privileged=true -v [absolute path of source mechine]:[absolute path of container mechine]:rw image_name:tag`
默认情况是`:rw`的
> 若容器内只读`:ro`


# 容器卷继承
> `docker run -it --privileged=true --volumes-from [parents container] --name [new container name] image:tag`
