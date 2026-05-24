---
layout: mypost
author: 三九二七
title: "如果把notion的windows的版本设置为中文教程"
date: 2023-04-18 00:00:00 +0800
categories: 分享
---

notion是一款国外程序员开发的笔记软件，有着便利的笔记导入和编辑功能，但是因为软件没有自带的中文，所以很多用户不知道应该如何修改中文，其实国内有开发者制作了汉化文件，大家只要下载并修改文件即可变成中文版。

### notion怎么变成中文版

**一、桌面版：**

1、首先我们要下载一个汉化文件。【github下载地址】

2、然后在其中下载“notion-zh_CN.js”这个文件。

![image.png](/assets/images/sjeq/202304181681824677193835.png)

3、下载完成后，我们找到“notion”软件，打开文件所在的位置。

![image.png](/assets/images/sjeq/202304181681824651116306.png)

4、进入后，打开“resources”文件夹。

![image.png](/assets/images/sjeq/202304181681824693167241.png)

5、接着依次进入“app”和“renderer”文件夹。

![image.png](/assets/images/sjeq/202304181681824713106148.png)

6、将下载到的文件放入该文件夹。接着使用记事本打开“preload.js”文件。

![image.png](/assets/images/sjeq/202304181681824728197853.png)

7、打开后在文件最后加入“ require("./notion-zh_CN") // ”命令，保存即可使用中文版notion。

![image.png](/assets/images/sjeq/202304181681824743180420.png)