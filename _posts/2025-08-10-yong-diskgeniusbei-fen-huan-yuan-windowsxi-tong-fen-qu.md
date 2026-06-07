---
layout: post
title: "用DiskGenius备份还原windows系统分区"
date: 2025-08-10
categories: 默认分类
tags: []
---

## 痛点

现在的电脑配置安装windows11系统虽然也是10多分钟可以完成，加上装软常用软件，至少也要半小时，有没有更好的方法呢？

想到用ghost，之前试过会还原的时候出错，还原的时间也并不算快。so，试一试DiskGenius

## 点备份分区

进PE系统，点备份分区，如图示，我这里使用最大压缩，休眠文件就不用备份。备份文件不到11G，拷到U盘备用。

![](/assets/images/ya0/image-krpd.png)

![](/assets/images/ya0/image-xdrd.png)

## 还原分区

在需要还原的主机，启动PE，打开DiskGenius-工具-从镜像文件还原分区，

![](/assets/images/ya0/image-bpaj.png)

## ![](/assets/images/ya0/image-yctl.png)  
还原完成

拔掉U盘，重启系统，还原过程只用了不到4分钟。

![](/assets/images/ya0/image-jqbp.png)

* * *

[ ](javascript:handleLike\('ce7252c5-9803-4108-aa0a-000e9cd9843b'\))

#### Recommended

2026-02-25 [自己动手做一个私人导航主页](/archives/Make%20your%20own%20private%20navigation%20page)

2026-02-25 [Markdown做数据表格批理在每行前插入“|”](/archives/markdown-of-%7C)

2026-02-10 [告别手写抄！这个电子天平小工具，让我每天准点下班](/archives/ElectronicBalance)

Prev Post [windows快速导出导入打印机](/archives/windowskuai-su-dao-chu-dao-ru-da-yin-ji)

Next Post [苹果mac mini主机安装windows10/11](/archives/macos-to-windows)

* * *
