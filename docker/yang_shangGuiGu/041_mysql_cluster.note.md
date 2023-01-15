# 新建主服务器3307                                                                                                                  
> docker run -d -p 3307:3307 --privileged=true -v /home/qy/workspace/docker_test/mysql_volumn/master/log:/var/log/mysql -v /home/qy/workspace/docker_test/mysql_volumn/master/conf/:/etc/mysql -v /home/qy/workspace/docker_test/mysql_volumn/master/data/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root --name=master_test mysql:5.7.37


# 配置文件                                                                                                                                                                                                                                                            
```
[mysql]

## 设置server_id，统一局域网需要唯一                                                                                                
server_id=101                                                                                                                       
## 指定不需要同步的数据库名称                                                                                                       
binlog-ignore-db=mysql                                                                                                              
## 开启二进制日志功能                                                                                                               
log-bin=mall-mysql-bin                                                                                                              
## 设置二进制日志使用内存大小（事物）                                                                                               
binlog_cache_size=1M                                                                                                                
## 设置使用二进制日志格式(mixed.statement.row)                                                                                      
binlog_format=mixed                                                                                                                
## 二进制日志过期清理时间，默认为0,表示不自动清理                                                                                   
expire_logs_day=7                                                                                                                   
## 跳过主从复制中遇到的所有错误或者指定类型的错误，避免slave端复制终端                                                              
## 如：1062错误是指主键重复，1032错误是因为住从数据库数据不一致                                                                     
slave_skip_errors=1062
```


# 创建数据同步用户
> CREATE USER 'slave'@'%' IDENTIFIED BY '123456';
> GRANT REPLICATION SLAVE,REPLICATION CLIENT ON *.* TO 'slave'@'%';

# 创建从服务器3308
> sudo docker run -d -p 3308:3307 --privileged=true -v /home/qy/workspace/docker_test/mysql_volumn/slave/log:/var/log/mysql -v /home/qy/workspace/docker_test/mysql_volumn/slave/conf/:/etc/mysql -v /home/qy/workspace/docker_test/mysql_volumn/slave/data/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root --name=slave_test mysql:5.7.37

# 新建从主机的my.cnf
```
## 设置server_id，统一局域网需要唯一                                                                                                
server_id=102                                                                                                                       
## 指定不需要同步的数据库名称                                                                                                       
binlog-ignore-db=mysql                                                                                                              
## 开启二进制日志功能                                                                                                               
log-bin=mall-mysql-bin                                                                                                              
## 设置二进制日志使用内存大小（事物）                                                                                               
binlog_cache_size=1M                                                                                                                
## 设置使用二进制日志格式(mixed.statement.row)                                                                                      
binlog_format=mixed                                                                                                                 
## 二进制日志过期清理时间，默认为0,表示不自动清理                                                                                   
expire_logs_day=7                                                                                                                   
## 跳过主从复制中遇到的所有错误或者指定类型的错误，避免slave端复制终端                                                              
## 如：1062错误是指主键重复，1032错误是因为住从数据库数据不一致                                                                     
slave_skip_errors=1062 
## relay_log配置中继日志
relay_log=mall-mysql-relay-bin
## log_slave_updates表示slave将复制事件些进自己的二进制目录
log_slave_updates=1
## slave设置为只读
read_only=1
```
# 重启my.cnf



