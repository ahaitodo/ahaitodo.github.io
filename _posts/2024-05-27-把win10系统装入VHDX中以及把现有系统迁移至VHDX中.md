---
layout: mypost
author: 三九二七
title: "把win10系统装入VHDX中以及把现有系统迁移至VHDX中"
date: 2024-05-27 00:00:00 +0800
categories: 工作
---

### 把win10系统装入VHDX中

要问把win10装入vhdx虚拟磁盘中有什么好处，个人电脑上没觉得什么好处或者坏处，或者备份方便，或者纯粹为了好玩。如果在人员流动大的公司环境，倒是可以为help desk快速重装系统提供方案，只需要进PE把vhdx文件覆盖一下就完事。现有一朋友在公司内使用该方案已经2周年，并没遇到什么问题。至于硬盘损坏导致的数据恢复要恢复一大个大文件而导致的难度上升，不在讨论范畴内。重要数据多放几份，多复制粘贴备份，比什么都强。

#### 使用VHDX_OneKey安装系统到vhdx中

这里使用一个偷懒方案，直接使用VHDX_OneKey把系统装到vhdx中。还是2013年更新的软件，不过无所谓，功能正常适合用即可。这里启动菜单只能添加到本机启动菜单，如果是全新安装，则需要使用PE下安装方案。

![image-1716810926314](/assets/images/sjeq/image-1716810926314.png)

提前下载好win10 iso，用资源管理器打开会挂载为一个光盘

![image-1716813480251](/assets/images/sjeq/image-1716813480251.png)

![image-1716813516748](/assets/images/sjeq/image-1716813516748.png)

![image-1716813531537](/assets/images/sjeq/image-1716813531537.png)

![image-1716813638779](/assets/images/sjeq/image-1716813638779.png)

完成之后可以直接添加启动项到启动菜单中

![image-1716813689067](/assets/images/sjeq/image-1716813689067.png)

![image-1716813703182](/assets/images/sjeq/image-1716813703182.png)

（这台实验机是server 2019 DC系统）

![image-1716813837223](/assets/images/sjeq/image-1716813837223.png)

![image-1716813902402](/assets/images/sjeq/image-1716813902402.png)

![image-1716813970597](/assets/images/sjeq/image-1716813970597.png)

完成

![image-1716814263092](/assets/images/sjeq/image-1716814263092.png)

#### 处理虚拟内存配置问题提示

如果启动之后有这个提示，去改一下虚拟内存位置即可。

![image-1716814284263](/assets/images/sjeq/image-1716814284263.png)

![image-1716814530346](/assets/images/sjeq/image-1716814530346.png)

![image-1716814403598](/assets/images/sjeq/image-1716814403598.png)

![image-1716814419535](/assets/images/sjeq/image-1716814419535.png)

重启后就不提示页面文件配置问题了。

#### 全手动操作安装win10到vhdx中

先进PE（这里使用优启通3.7 EasyU3.7），使用磁盘管理，或者bootice创建vhdx虚拟磁盘

###### 先进行硬盘分区

这里使用MBR分区，对应BIOS引导。

![image-1716815947782](/assets/images/sjeq/image-1716815947782.png)

这里使用GPT分区，对应UEFI引导。(至于双启，这里不讨论)

![image-1716816054549](/assets/images/sjeq/image-1716816054549.png)

##### 选择一：通过系统自带磁盘管理建立vhdx虚拟磁盘

这里有两块硬盘，已有一块提前分好区，本次将VHDX存放到该硬盘中。

![image-1716814762510](/assets/images/sjeq/image-1716814762510.png)

![image-1716814790168](/assets/images/sjeq/image-1716814790168.png)

![image-1716814833387](/assets/images/sjeq/image-1716814833387.png)

##### 选择二：通过bootice创建vhdx虚拟磁盘

![image-1716814930419](/assets/images/sjeq/image-1716814930419.png)

![image-1716814983858](/assets/images/sjeq/image-1716814983858.png)

![image-1716814991936](/assets/images/sjeq/image-1716814991936.png)

然后再资源管理器中找到该文件，双击打开他，附加到系统中

![image-1716815039643](/assets/images/sjeq/image-1716815039643.png)

![image-1716815070647](/assets/images/sjeq/image-1716815070647.png)

给虚拟磁盘分区（至于虚拟磁盘使用MBR分区表还是GUID分区表其实影响不大，引导程序不在该虚拟磁盘。）

![image-1716815241666](/assets/images/sjeq/image-1716815241666.png)

![image-1716815253312](/assets/images/sjeq/image-1716815253312.png)

##### 把系统装到vhdx虚拟磁盘

如果使用系统ISO自带的setup.exe进行安装，则不需要提前对虚拟磁盘分区

使用PE自带的EIX，重启的勾最好去掉，部署好系统之后还有其他操作。

![image-1716815352575](/assets/images/sjeq/image-1716815352575.png)

##### MBR分区+BIOS引导 添加启动菜单

双击打开刚才部署好系统的VHDX，这里打开后挂载到G盘

![image-1716820681808](/assets/images/sjeq/image-1716820681808.png)

当前环境引导盘为C:\其他情况下按实际情况确定引导盘符。VHDX文件可以和引导在同一分区下，也可以在不同分区下。

必要说明的一点是VHDX所在物理分区大小要比VHDX大上1G左右，如VHDX文件设置50G，所在分区最好有51G，且不要把其他文件存放在该分区。因为VHDX文件在系统启动后会扩展到实际大小，如50G。如果物理分区空间不够就会蓝屏，启动失败。可以设置开机不扩展，不过存在隐患，这里不做赘述。

把G:\Windows\Boot\PCAT文件夹复制到C:\下并改名为Boot当前目录状态

![image-1716820887130](/assets/images/sjeq/image-1716820887130.png)

再把该目录下的bootmgr和bootnxt剪切到C:\根目录下

![image-1716820937922](/assets/images/sjeq/image-1716820937922.png)

这两个是BIOS启动系统必要文件

打开BOOTICE，编辑BCD

![image-1716821159897](/assets/images/sjeq/image-1716821159897.png)

![image-1716821229042](/assets/images/sjeq/image-1716821229042.png)

![image-1716821238508](/assets/images/sjeq/image-1716821238508.png)

![image-1716821269772](/assets/images/sjeq/image-1716821269772.png)

选择VHDX所在磁盘，分区，以及写入设备文件路径，\代表该分区根目录这里只该分区根目录下WIN_VHD文件夹下的Win10.vhdx文件

![image-1716821391203](/assets/images/sjeq/image-1716821391203.png)

好了，重启就OK了

##### GUID分区+ UEFI 引导 添加启动菜单

GUID分区EFI引导需要创建ESP分区

![image-1716821981927](/assets/images/sjeq/image-1716821981927.png)

给ESP分区分配好盘符，分到到G盘

![image-1716822015413](/assets/images/sjeq/image-1716822015413.png)

把装好系统的VHDX双击打开，挂载到系统中，此次挂到为H盘

复制H:\Windows\Boot\EFI文件夹到G:\下，再进入G:\EFI目录，新建文件夹Microsoft，并把除Microsoft文件夹外的所有文件移动到Microsoft目录中，再新建Boot文件夹，进入刚才的Microsoft文件夹把bootmgfw.efi文件复制出来放到Boot文件夹中，并重命名为bootx64.efi

![image-1716822606889](/assets/images/sjeq/image-1716822606889.png)

![image-1716822586646](/assets/images/sjeq/image-1716822586646.png)

![image-1716822576500](/assets/images/sjeq/image-1716822576500.png)

再回到Microsoft文件夹，新建文件夹Boot，BCD文件需要放在该目录下打开BOOTICE，编辑BCD

![image-1716821159897](/assets/images/sjeq/image-1716821159897.png)

![image-1716823404262](/assets/images/sjeq/image-1716823404262.png)

![image-1716823411003](/assets/images/sjeq/image-1716823411003.png)

此后步骤和BIOS+MBR引导时一致，借用BIOS引导的配置图。

![image-1716821269772](/assets/images/sjeq/image-1716821269772.png)

选择VHDX所在磁盘，分区，以及写入设备文件路径，\代表该分区根目录这里只该分区根目录下WIN_VHD文件夹下的Win10.vhdx文件

![image-1716821391203](/assets/images/sjeq/image-1716821391203.png)

注意使用UEFI引导时，如果启动文件不是winload.efi，就改成winload.efi，再保存

![image-1716823468706](/assets/images/sjeq/image-1716823468706.png)

好了，重启就OK了

### 把现有win10(Server 2019)系统迁移到VHDX中

此时仍然需要使用PE，先进PE（这里使用优启通3.7 EasyU3.7）

在磁盘管理新建vhdx

![image-1716823988685](/assets/images/sjeq/image-1716823988685.png)

并建好分区

![image-1716824026554](/assets/images/sjeq/image-1716824026554.png)

再用Ghost把系统分区克隆过来即可，系统就迁移到VHDX中，按照刚才方法添加相应引导程序，新建BCD即可

![image-1716824102972](/assets/images/sjeq/image-1716824102972.png)

![image-1716824889798](/assets/images/sjeq/image-1716824889798.png)

Server2019已迁移到VHDX中运行。

![image-1716824938577](/assets/images/sjeq/image-1716824938577.png)

上次在物理机内970 PRO所在系统分区Ghost克隆分区时出现25002报错，忽略报错之后没法正常进系统。后来使用Diskgenius的迁移至虚拟机功能，把系统分区克隆为vmdk文件，再把vmdk使用StarWind V2V Image Converter转换成vhdx虚拟盘，挂载出来把多余的esp删掉后，再恢复引导盘，修改BCD后正常启动。

![image-1716824456155](/assets/images/sjeq/image-1716824456155.png)

此时系统运行在VHDX虚拟磁盘中

![image-1716824599676](/assets/images/sjeq/image-1716824599676.png)

附：Ghost 25002报错

![image-1716824368560](/assets/images/sjeq/image-1716824368560.png)

```
https://jingyan.baidu.com/article/a3761b2b16c7841577f9aa6b.html
右击，命令提示符，输入ghost32.exe -ntexact，回车，进入ghost还原界面，再次选择你的镜像文件和还原目的路径，就可以静等进度条前进了。。。

https://knowledge.broadcom.com/external/article/238782/image-deploy-results-in-ghost-solution-s.html
In one instance we were able to resolve this issue by launching ghost with additional switches before deploying the problematic image

ghost64.exe -NTEXACT -NTIC -NTIL

-NTEXACT: Enable an exact restore of the NTFS source volume layout.
-NTIC: Ignore the NTFS volume CHKDSK bit.
-NTIL: Ignore non-empty NTFS Log File check (Inconsistent volume).
```