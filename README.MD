# 图片处理工具

## 环境配置

### 1. 新建虚拟环境

这里我使用的是 conda

```shell
 conda create -n photo_bot python=3.8
 conda activate photo_bot 
```

### 2. 安装依赖

相关依赖都维护在了 requirement.txt 文件，使用下面的命令安装即可

```sheell 
pip install -r requirements.txt
```

### 3.打包命令

```shell
 pyinstaller -F -w -i fav.ico photo_bot.spec
```

## 工具列表

### 1. 相框工具

读取图片的 Exif 参数，生成如下样式的图片
![img](./assert/晚霞.png)

使用方法:
打包后可以看到 dict/photo_bot 的可执行文件，双击执行可见如下的命令行交互界面，安装提示输入图片所在文件夹以及处理后的保存路径

```shell
generate white picture frame automatically
Please enter the folder location of your photo :
/Users/admin/Downloads/test_image
Please enter a file path to save the output photo :
/Users/admin/Downloads/out_image
```

## 参考文献

参考文档：

- [piexif 参考文档](https://readthedocs.org/projects/piexif/downloads/pdf/latest/)