---
layout: post
title: "苹果mac mini主机安装windows10/11"
date: 2025-07-30
categories: 默认分类
tags: []
---

对于一些已被淘汰的x86架构老机器，若想将Intel i5处理器的系统更换为Windows 10或Windows 11，通过Mac系统里的“启动转换助理”安装是比较便捷的方式，不过此处暂不展开介绍。要是机器配置较低，比如是4G内存搭配128G硬盘，或是8G内存搭配256G硬盘的情况，我打算直接删除原有的Mac OS系统，将整个硬盘划分为一个C盘来进行安装，以实现100%的磁盘利用率。后续若想重新安装Mac OS，再另行制作Mac OS安装盘即可。

以下是我的操作方法步骤：

## 一、做启动盘

找个空白U盘，装ventoy，找一个EasyU_v3.7.iso 丢进U盘里，然后开机长按`Option`键（没有则是 `Alt`键）会出现下图

![](/assets/images/ya0/image-soiw.png)

![](/assets/images/ya0/image-udyw.png)

![](/assets/images/ya0/image-gcpy.png)

![](/assets/images/ya0/image-aoda.png)

![](/assets/images/ya0/image-szej.png)

## 二、用DiskGenius分区

![](/assets/images/ya0/image-higl.png)

## 三、装windows系统

我这里用，Easylmage X2 还原镜像，实际我是选了windows11-LTSC

![](/assets/images/ya0/image-bxfb.png)

## 四、进windows系统

恢复完，拔开U盘，首次配置进入系统，装好了，完美。

![](/assets/images/ya0/image-qmby.png)

* * *

[ ](javascript:handleLike\('f7634077-b271-4fc2-a24f-327aa7e2aead'\))

#### Recommended

2025-01-15 [win11跳过联网激活步骤](/archives/win11tiao-guo-lian-wang-ji-huo-bu-zou)

2024-09-10 [Windows、macOS、linux、iOS和Android系统，查看本机MAC地址及IP地址的方法](/archives/Mac-IP)

2024-09-06 [ROG STRIX Z790-A GAMING WIFI S 吹雪配i9-14900KF装显卡驱动与cuda解压出错的问题](/archives/cuda)

Prev Post [用DiskGenius备份还原windows系统分区](/archives/yong-diskgeniusbei-fen-huan-yuan-windowsxi-tong-fen-qu)

Next Post [mac OS 把Command/win键换成 ctrl键](/archives/macOS-Command-win-to-ctrl)

* * *
