---
layout: post
title: "win11跳过联网激活步骤"
date: 2025-01-15
categories: 默认分类
tags: []
---

以下是一些跳过Windows 11联网激活步骤的方法：

#### 使用“oobe\bypassnro”命令

1、在出现联网界面后，按键盘“shift”+“f10”组合键，打开cmd命令行提示符输入框。

2、输入“oobe\bypassnro”命令并回车。

3、命令执行后电脑会自动重启，再次返回联网界面，此时会出现“我没有internet连接”的选项，选它即可跳过联网。

#### 使用“start ms-cxh:localonly”命令

1、同样在出现联网界面后，按键盘“shift”+“f10”组合键，打开cmd命令行提示符输入框。

2、输入“start ms-cxh:localonly”命令并回车。

3、命令正确执行后会弹出创建本地帐户的输入框，创建成功后，会跳回Windows初始化程序，继续操作。

#### 断网

1、可以直接拔掉网线，进行物理断网。

2、也可以通过网络共享中心的“更改适配器设置”禁用网卡。

#### 结束网络连接流进程

1、按键盘“shift”+“f10”组合键，打开cmd命令行提示符输入框。

2、输入“taskmgr”打开任务管理器。

3、结束其中的“网络连接流”或“network connection flow”进程。

#### 使用特定邮箱地址

在登录微软帐号时，使用邮箱地址“no@thankyou.com”，然后密码随便填，这样可能会跳过微软帐号登录，显示本地帐号创建。

* * *

[ ](javascript:handleLike\('a57b9bb9-360a-4b9a-9420-8d66e4b5f9fd'\))

#### Recommended

2025-06-26 [windows、macOS 、android的wireGuard客户端下载安装使用教程](/archives/windows-macOS-android-wireguard-Client-Download-install-and-use-the-tutorial)

2025-06-20 [全场景产品矩阵，支撑 AI 应用全流程落地](/archives/siliconflow)

2025-03-30 [一行代码自动续签ssl证书文件](/archives/ssl-updata)

Prev Post [阿里导出raw镜像下载到本地使用](/archives/raw%23pve)

Next Post [记录一下，linux全盘备份的两个方法](/archives/linuxtoimg)

* * *
