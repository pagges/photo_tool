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


## 参考文献

参考文档：

- [piexif 参考文档](https://readthedocs.org/projects/piexif/downloads/pdf/latest/)