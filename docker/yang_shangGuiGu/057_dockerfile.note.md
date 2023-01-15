
# dockerfile学写
* 编写Dockerfile文件
* docker build 
* docker run


## 基础知识
* 每条保留字命令都必须为大写字母，后面至少跟一个参数
* 指令从上到上，顺序执行
* #表示注释
* 每条指令都会创建一个新的镜像层并对镜像进行提交

> Docker 定义了进程需要的一切东西。Docker设计的内容包括执行代码或是文件、环境变量、依赖包、运行时环境、动态链接库、操作系统的发行版、服务器进程和内核进程等等;
> Dockerfile定义一个文件之后，docker build会产生一个Docker镜像，当运行Docker镜像时候会真正开始提供服务。
> Docker容器，容器是直接提供服务

## DOckerfile保留字

* FROM 
> 基础镜像，当前新镜像是基于哪个镜像的，制定一个已经存在的镜像作为木板，第一条必须是FROM

* MAINTAINER
> 镜像维护者的姓名和邮箱地址

* RUN
> 容器构建时候需要运行的命令，
> 两种格式 shell格式/exe格式，eg: RUN ["./test.php", "dev", "offline"] 等价于 `RUN ./test.php dev offline`
> RUN是在docker build时候运行的


* EXPOSE
> 当前容器对外暴露出的端口

* WORKDIR
> 指定在创建容器之后，终端默认登录进来工作的目录。

* USER
> 指定镜像以什么样的用户去执行，如果都不指定，默认为root

* ENV
> 用来在构建镜像过程当中设置环境变量
> eg: ENV MY_PATH /user/mytest 这个环境变量在后续的任何RUN指令中使用，这里如同在命令前定一个环境变量前缀一样，也可以在其他指令中直接使用这些环境变量。

* VOLUME
> 容器数据卷，用于数据保存和持久化 

* ADD
> 将宿主机目录i啊的文件拷贝到镜像，且会自动处理URL和解压.tar压缩包

* COPY
> 类似ADD，拷贝文件和目录到镜像中，将从构建上下文目录中<源路径>的文件/目录 复制到新一层镜像内的<目标路径>位置

* CMD
> 指定**容器**启动后要做的事情, 

> CMD指令的格式和RUN相似，也是两种格式
> * shell格式 cmd <命令>
> * exec格式 cmd ["可执行文件", "参数", "参数2",...]
> * 参数列表格式 cmd ["参数", "参数2"], 在指定了ENTERYPOINT 指令后，用CMD制定具体参数。

> 注: Dockerfile中可以有多个CMD指令，但最后只有一个生效，CMD会被docker run 之后的参数替换
> CMD是在docker run时候运行; RUN是在docker build时运行

* ENTRYPOINT
> 类似CMD命令，但是ENTRYPOINT不会被docker run后面的命令覆盖，而且这些命令行参数会被大概你做参数送给ENTRYPOINT指令指定的程序
> eg: 
```

FROM nginx

ENTRYPOINT ["nginx", "-c"] # 定参
CMD ["etc/nginx/nginx.conf"] # 变参

```
执行 `docker run nginx:test`
衍生出的实际命令是 `nginx -c /etc/nginx/nginx.conf`

执行 `docker run nginx:test /etc/nginx/new.conf`
衍生出的实际命令是 `nginx -c /etc/nginx/new.conf`





