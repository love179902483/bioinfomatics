## 配置磁盘自动挂载

1. 查看Linux硬盘信息
	> sudo fdisk -l 

2. 格式化硬盘
	> sudo mkfs.ext4/dev/sdb1
3. 创建/data目录 (/data目录为硬盘自动挂载的地方)
	> sudo mkdir/data
4. 挂载分区
	> sudo mount /dev/sdb1 /data
5. 查看磁盘分区的UUID
	> sudo blkid


	```
	/dev/sda1: UUID="8048997a-16c9-447b-a209-82e4d380326e" TYPE="ext4"
	/dev/sda5: UUID="0c5f073a-ad3f-414f-85c2-4af83f6a437f" TYPE="swap"
	/dev/sdb1: UUID="11263962-9715-473f-9421-0b604e895aaa" TYPE="ext4"
	/dev/sr0: LABEL="Join Me" TYPE="iso9660"

	```

6. 配置自动开机挂载

	* 因为mount命令会在重启服务器之后失效，所以要将分区信息写到/etc/fastb文件中让它永久挂载
	
	1. sudo vim /etc/fstab
	2. 加入 
	> UUID=11263962-9715-473f-9421-0b604e895aaa /data ext4 defaults 0 1

	3. 以下为具体说明:
	```
	
	pec> <fs file> <fs vfstype> <fs mntops> <fs freq> <fs passno>
	具体说明，以挂载/dev/sdb1为例：
	<fs spec>：分区定位，可以给UUID或LABEL，例如：UUID=6E9ADAC29ADA85CD或LABEL=software
	<fs file>：具体挂载点的位置，例如：/data
	<fs vfstype>：挂载磁盘类型，linux分区一般为ext4，windows分区一般为ntfs
	<fs mntops>：挂载参数，一般为defaults
	<fs freq>：磁盘检查，默认为0
	<fs passno>：磁盘检查，默认为0，不需要检查
	
	```

	4. 重启系统 
		> sudo mount -a

	验证配置是否正确，如果不正确可能会无法启动

	5. 真实例子
		> UUID=42168DE83BC5EDAD /media/jim/Files2 ntfs defaults 0 1
	说明： /media/jim/Files2 为当前挂载位置，不是/dev/sda1
	
	6. df -T
		> df命令用于显示磁盘分区上可使用的磁盘空间，-T表示显示文件类型
	7. file -s /dev/sda3 
		> 查看已经挂载的文件类型
	8. lsblk -f 也可以查看未挂载文件系统类型
	9. parted -l 可以查看未挂载的文件系统类型，以及哪些分区尚未格式化。
