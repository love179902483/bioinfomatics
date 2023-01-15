# 在大部分场景下，我们希望docker的服务是在后台运行的，我们可以通过-d指定容器的后台运行模式。
## 启动守护是容器(后台服务器)
> docker run -d [container name]


# 查看容器日志
> docker logs [container ID]

# 查看容器内运行进程
> docker top [container ID]

# 查看容器内部细节
> docker inspect [container ID]

# 再次进入已经退出的容器内部
> docker exec -it [container ID] /bin/bash
> docker atatch [container ID]
**attach 直接进入容器启动命令终端，不会启动新的进程用exit退出，会导致容器停止**
**exec是在容器中打开新的终端，并且可以启动新的进程，用exit退出，不会导致容器停止**
**推荐使用exec**

# 总结
> 一般用-d后台启动程序，再用exec进入对应容器实例
