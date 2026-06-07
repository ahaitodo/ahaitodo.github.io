---
layout: post
title: "Markdown做数据表格批理在每行前插入“|”"
date: 2026-02-25
categories: 默认分类
tags: []
---

## 方法1：手动插入（最简单）

  1. 复制数据到记事本，光标移到第一行最前面

  2. 直接输入 `|`

  3. 按 `↓` 键到下一行

  4. 重复操作...（虽然笨但有效）。😅之前数据少，我都是在记事本这样用笨方法操作。今天近百行数据复制到Notepad++可以更快。

## **方法2：Notepad++（最快）**

![](/assets/images/ya0/image-lvvb.png)

  1. **打开Notepad++** 📄

  2. **按 Ctrl+H** 打开替换对话框

  3. **查找内容** ：`^` （表示行首）

  4. **替换为** ：`|` （就是个竖线符号）

  5. **勾选"正则表达式"** ✅

  6. **点击"全部替换"** 🚀

### **🎯 操作原理**

  * `^` = 匹配每行的开头位置

  * 替换为 `|` = 在每行开头插入竖线

  * 这样每行就变成了 `|2026-02-22|22:00:10|...`

### **💡 补充说明**

如果您想用更保险的方式（避免空行也被处理）：

  * **查找** ：`^[^\n]` （匹配行首的非换行符）

  * **替换为** ：`|$0` （在行首加|，$0表示匹配到的字符）  
一般查找 `^` 替换成 `|` 就够用了！👍

如图：

![](/assets/images/ya0/image-iweo.png)

* * *

[ ](javascript:handleLike\('3a1169f0-d6c5-40f0-a2fa-678f6e8ee789'\))

#### Recommended

2025-07-30 [苹果mac mini主机安装windows10/11](/archives/macos-to-windows)

2025-07-25 [mac OS 把Command/win键换成 ctrl键](/archives/macOS-Command-win-to-ctrl)

2025-07-03 [手机微信100多G聊天记录，备份到电脑的步骤方法](/archives/steps-and-methods-for-backing-up-wechat-chat-records-to-a-computer)

Prev Post [自己动手做一个私人导航主页](/archives/Make%20your%20own%20private%20navigation%20page)

Next Post [告别手写抄！这个电子天平小工具，让我每天准点下班](/archives/ElectronicBalance)

* * *
