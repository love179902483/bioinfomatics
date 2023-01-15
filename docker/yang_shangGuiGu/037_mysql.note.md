
# 安装mysql镜像
> docker pull mysql:5.7.37

# 启动mysql
> docker run -p 3306:3306 --name=mysql_01 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.37
> 若本机有mysql需要注意3306端口是否被占用 ps -ef|grep mysql

# 以上命令启动有问题
> 没有挂载容器数据卷也就是没有用-v命令，所以如果容器结束，则数据丢失。


# 挂载容器数据卷
> docker run -d -p 3306:3306 --privileged=true -v /home/qy/workspace/docker_test/mysql_volumn/log:/var/log/mysql -v /home/qy/workspace/docker_test/mysql_volumn/data:/var/log/mysql -v /home/qy/workspace/docker_test/mysql_volumn/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 --name mysql mysql:5.7.37

# 解决mysql中文乱码问题
> /home/qy/workspace/docker_test/mysql_volumn/conf/ 下 新建my.cnf并输出 
```
[client]
default_character_set=utf8
[mysqld]
collation_server=utf8_general_ci
character_set_server=utf8
```
> 之后重新启动mysql容器


# 进入mysql
> mysql -uroot -p
> 查看字符集
> SHOW VARIABLES LIKE 'character%'
> create database db01;
> create table t1(id int,name varchar(20));
> insert t1 values(1, 'z3');
> insert t1 values(2, '中文2');

# 在使用docker版本的mysql中，建议先将字符集修改之后重启mysql之后进行操作


