---
layout: mypost
author: 三九二七
title: "H3CS6520-26Q-SI通过Console口登录设备设置IP打开web管理服务"
date: 2022-08-26 00:00:00 +0800
categories: 工作
---

一、连接

当无法登录设备WEB管理界面时,需要通过Console口本地登录设备｡

![image](https://www.sjeq.com/zb_users/plugin/UEditor/themes/default/images/spacer.gif)![image](https://www.sjeq.com/zb_users/plugin/UEditor/themes/default/images/spacer.gif)![image](/assets/images/sjeq/20230226173412_13295.png) 

连线：配置线(console线)RJ-45水晶头连接路由器的console口,DB9的串口连接电脑的com口｡如果电脑不带com口,请使用com口转USB接口的转换器，然后连接电脑的USB接口｡

## 2、准备工具

配置线:console线,一端是RJ-45水晶头,一端是DB9的串口｡如果电脑上无com口,可购买console线转USB配置线｡

![image](/assets/images/sjeq/202302261677403138262930.png) 

## 三、配置步骤

### **SecureCRT****软件设置（附件中为****CRT****软件，安装即可）**

1､打开“计算机”右键属性——设备管理器——端口（或者控制面板——系统——设备管理器），查看并确认电脑上使用的通信端口:本文使用COM3｡

![image](https://www.sjeq.com/zb_users/plugin/UEditor/themes/default/images/spacer.gif)![image](/assets/images/sjeq/202302261677403157208103.png) 

2､设置快速连接:协议Seriel,端口com3,波特率9600,数据位8,奇偶校验无,停止位1｡注意:数据流控制的所有勾都去掉｡

 ![image](/assets/images/sjeq/202302261677403176205678.png)

3､点击连接后进入对话框,敲回车键后出现<H3C>提示符,则可以正常输入命令｡

![image](/assets/images/sjeq/202302261677403185132264.png)

# **配置步骤**

<H3C>system-view

#创建本地用户admin，并设置登录密码为admin，服务类型为http跟https，用户级别为network-admin管理员级别

[H3C] local-user admin

[H3C-luser-manage-admin] password simple admin

[H3C-luser-manage-admin] service-type http https

[H3C-luser-manage-admin] authorization-attribute user-role network-admin

#配置交换机的管理地址：

[H3C] interface vlan-interface 1

[H3C-VLAN-interface1] ip address 10.0.37.200 255.255.255.0

#开启http跟https服务

[H3C-VLAN-interface1]ip http enable

[H3C]ip https enable

#保存配置

[H3C]save force

[H3C]quit