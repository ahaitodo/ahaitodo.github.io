---
layout: post
title: "记录一下，linux全盘备份的两个方法"
date: 2024-10-21
categories: 默认分类
tags: []
---

记录一下，linux全盘备份的两个方法。

**第一个方法：使用（猫头）img写盘工具DiskImage**

1、备份

![](/assets/images/ya0/1729532812314.png)

store image 创建镜像，读取源盘，选择保存到另一个物理硬盘路径。备份120G，顺利成功。

2、还原

![](/assets/images/ya0/image-whka.png)

write image 写入镜像，选择目标硬盘，如果目标硬盘有分区，一般要用DG工具提前删除目标硬盘的所有分区。选择之前保存的镜像，点start写入，直至提示成功。

3、遇到的问题

当备份240G的硬盘出现快结束时提示出错，换一个备份硬盘出现同样问题，不确定是不是工具版本不支持，换第二个方法。

![](/assets/images/ya0/1729538617228.png)

**第二个方法：使用DD**

1、备份前工作

首先fdisk-l确认磁盘身份，以下是简化信息。

![](/assets/images/ya0/image-hfgy.png)

可见有两个物理硬盘，确认sda无重要数据后，把sdb备份到sda下边的一个分区。

root@host-231~]# **sudo umount /dev/sda1 -- 卸载分区（如无挂载跳过）**

**sudo mkfs.ext4 /dev/sda1 --** 将 `/dev/sda1` 分区格式化为 ext4 文件系统

![](/assets/images/ya0/image-puuh.png)

**sudo mkdir -p /mnt/sda1 -- 创建挂载点**

**sudo mount /dev/sda1 /mnt/sda1 -- 挂载分区**

**df -Th --查看挂载情况，有sda1了**

![](/assets/images/ya0/image-oyeu.png)

cd /mnt/sda1 --**进入挂载点**

2、备份

**dd if=/dev/sdb bs=4M status=progress | xz -3 -z -T 8 -c > sdb3.img.xz**

![](/assets/images/ya0/image-vpie.png)**\--将**`/dev/sdb`**盘的数据以进度显示的方式压缩为**`sdb3.img.xz`**文件，同时使用8个线程进行压缩以加快处理速度。**

**如果硬盘空间大，不压缩使用** dd if=/dev/sdb bs=4M status=progress > sdb.img

![](/assets/images/ya0/image-uaas.png)

**ls -lh查看备份文件大小，压缩的18G，不压缩的120G**

![](/assets/images/ya0/image-etgp.png)

3、还原：

同样要先确认磁盘身份，确认还源到哪个盘，以还原到sdc为例

sudo umount /dev/sdc1

cd /mnt/sda1 --**进入挂载点 ，如果没有需要创建。**

root@pve:/mnt/sda1#xz -d -k -T 4 -c sdb.img.xz | dd of=/dev/sdc status=progress

* * *

[ ](javascript:handleLike\('161a9d7f-3645-4f5f-b010-edd31cc89c44'\))

Prev Post [win11跳过联网激活步骤](/archives/win11tiao-guo-lian-wang-ji-huo-bu-zou)

Next Post [Windows、macOS、linux、iOS和Android系统，查看本机MAC地址及IP地址的方法](/archives/Mac-IP)

* * *
