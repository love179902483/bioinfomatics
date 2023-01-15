# 从晕拉取redis镜像标签目前用6.0.16
# redis一定要指定配置文件
> 默认配置文件修改
```

# 允许redis外部链接 必须注释掉
# bind 127.0.0.1

# 注释掉daemonize 或者daemonize no
# daemonize no

# redis持久化 appendonly yes 可选


```

# 绑定容器数据卷
> docker run -d -p 6379:6379 --name=redis_test --privileged=true -v /home/qy/workspace/docker_test/redis_volumn/redis.conf:/etc/redis/redis.conf -v /home/qy/workspace/docker_test/redis_volumn/data:/data redis:6.0.16 redis-server /etc/redis/redis.conf

# 验证是否.conf绑定成功
