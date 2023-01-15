
# docker run [OPTIONS] image [COMMAND][ARG...]
> OPTINOS说明:有些是一个减号，有些是两个减号

* --name="容器新名称" 为容器指定一个名称
* -d: 后台运行容器并返回容器ID，也就是启动守护式容器（后台运行）
* -i: 以交互式模式运行容器，常常与-t同时使用
* -t: 为容器重新分配一个伪输入终端，通常与-i同时使用;也就是启动交互式容器，前台有伪终端，等待交互。
* -P: 随机端口映射，大写P
* -p: 指定端口映射，消协p


# docker ps [OPTIONS]
> 列出当前所有正在运行的容器
> OPTIONS说明
* -a: 列出所有正在运行的容器+历史上晕新过的
* -l: 显示最近创建的容器。
* -n: 显示最近那个创建的容器。
* -q: 静默模式，只显示容器编号。


# 容器退出
* exit: run进去容器，exit退出，容器会停止
* ctrl + p + q: run进去的容器，ctrl + p + q推出，容器不停止.

# 重启容器
> docker restart [ID]

# 停止容器
> docker stop [ID]

# 强制停止容器
> docker kill [ID]

# 删除已经停止的容器
> docker rm [ID]

# 删除未停止的容器
> docker rm -f [ID]

# 删除全部容器
> docker rm -f $(docker ps -a -q)



