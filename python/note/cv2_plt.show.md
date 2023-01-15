## 关于opencv读取图片和展示图片，以及matplot展示图片


* 开始之前，我们先对imread()这个函数做个了解
	
	cv::imread(const string& filename, int flag=MREAD_COLOR);

	Parameters
		* filename: 需要加载的文件
		* flags: 指加载图片的标识，指定图片类型

	Note:
		
		imread()函数读取图片根据文件内容来读取的，而不是根据文件扩展名。
		
		imread的flags有以下几种:

		```
			IMREAD_UNCHANGED            = -1, //返回包含alpha通道的加载图像
			IMREAD_GRAYSCALE            = 0,  //返回一个灰度图像
			IMREAD_COLOR                = 1,  //返回一个BGR通道的图像
			IMREAD_ANYDEPTH             = 2,  //当输入具有相应的深度时返回16位/ 32位图像，否则将其转换为8位。.
			IMREAD_ANYCOLOR             = 4,  //则以任何可能的颜色格式读取图像。
			IMREAD_LOAD_GDAL            = 8,  //使用GDAL的驱动加载图像。
			IMREAD_REDUCED_GRAYSCALE_2  = 16, //将图像转换为单通道灰度图像，图像大小减少1/2。
			IMREAD_REDUCED_COLOR_2      = 17, //转换图像的3通道BGR彩色图像和图像的大小减少1/2。
			IMREAD_REDUCED_GRAYSCALE_4  = 32, //将图像转换为单通道灰度图像，图像大小减少1/4。
			IMREAD_REDUCED_COLOR_4      = 33, //转换图像的3通道BGR彩色图像和图像的大小减少1/4。
			IMREAD_REDUCED_GRAYSCALE_8  = 64, //将图像转换为单通道灰度图像，图像大小减少1/8。
			IMREAD_REDUCED_COLOR_8      = 65, //转换图像的3通道BGR色彩图像和图像大小减少1/8。
			IMREAD_IGNORE_ORIENTATION   = 128 //不旋转图像根据EXIF的定位标志。
		```


* 由于cv2.read()读取的图片是bgr的，而matplot需要展示的图片却是rgb的，所以要在matplot中展示正常的图片，我们需要调换cv2.read()读取到的图拍你通道顺序。
	1.	cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	2.	img = img[::(2,1,0)]
	3.	
		```
			def change_chennel(img):
				b,g,r=img.split(img)
				channel_list = [r,g,b]
				new_image = cv2.merge(channel_list)
				return new_image
		```




* 图像转为灰度图
	1. cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
