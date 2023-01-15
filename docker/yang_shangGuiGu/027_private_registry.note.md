# 创建一个本地的私人dockerhub供自己使用

* 下载镜像 registry
> `docker pull registry`

* 运行私有的registry,相当与本地有一个私有的DockerHub
> `docker run -d --name=my_docker_registry -p 5000:5000 -v /root/docker_registry/:/tmp/registry --privileged=true registry`

* 使用crul验证私有docker服务中有什么镜像
> `curl -XGET http://124.222.24.154:5000/v2/_catalog`

* 将新镜像修改符合服务器规范的Tag
> `docker tag [source_image:Tag] target_ip:target_port/[target_image:Tag]`

* 修改配置文件使之支持http
```
vim /etc/docker/daemon.json

{

    "registry-mirrors": ["https://edpy04wr.mirror.aliyuncs.com"],
    "insecure-registries": ["124.222.24.154:5000"]

}
```
重新启动deamon-reload和docker
> systemctl daemon-reload
> systemctl restart docker

* push推送到服务器
> `docker push target_port/[target_image:Tag]`

* 测试是否上传成功
> docker pull 124.222.24.154:5000/first_private_image:v01
