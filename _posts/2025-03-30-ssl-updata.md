---
layout: post
title: "一行代码自动续签ssl证书文件"
date: 2025-03-30
categories: 默认分类
tags: []
---

如果网站多，使用免费证书都是三个月，人工替换起来变得有点麻烦，

一不留神就会过期几天才发现，找了个自动续签的方法。

🔥httpsok一行命令，轻松搞定SSL证书自动续签。

**第一步：** 先注册账号： <https://httpsok.com/p/4Ltd> 要申请证书，然后**DNS配置验证。****当然你也可以手动下载配置证书，我喜欢这申请的通配证书。**![](/assets/images/ya0/image-tcio.png)

支持：nginx、通配符证书、七牛云、腾讯云、阿里云、CDN、OSS、LB（负载均衡）

1\. 证书到期前15天自动申请SSL证书自动替换SSL证书自动重载服务 无须人工介入 

2\. 安装成功后，会自动检测一次系统中的证书，并同步到控制台。

**第二步：** 安装脚本，本站以Nginx续签为例，运行：

curl -s https://get.httpsok.com/ | bash -s fJpJcRiaXkkhO3keDtys

![](/assets/images/ya0/image-ekti.png)

![](/assets/images/ya0/image-epam.png)

![](/assets/images/ya0/image-wqxz.png)

看到脚本已经把证书文件已经替换了,

![](/assets/images/ya0/image-bpoz.png)

![](/assets/images/ya0/image-wtff.png)

90天真的很快过，等下次它自动替换更新吧。

**免费SSL证书由什么时候12个月变为3个月呢？**

免费SSL证书的有效期从2023年11月开始调整为三个月‌，阿里云在2023年11月14日开始将其免费SSL证书的有效期从一年调整为三个月‌，此外，腾讯云也在2024年4月25日之后将免费SSL证书的有效期调整为三个月。

**免费SSL证书的有效期变化原因？**

‌国际顶级科技公司如Google的推动‌：Google一直在推动免费证书90天有效期的建议，以帮助及时发现可能存在的安全漏洞，降低风险‌。

* * *

[ ](javascript:handleLike\('3b25ab4e-8e96-42e1-8a3d-515ebdcf8ea6'\))

#### Recommended

2026-02-05 [干活牛马，除了openclaw还有国产的这款工具能帮你更快干活](/archives/use-openclaw-to-aipy-yaoqingma-jpU6)

2025-09-18 [windows快速导出导入打印机](/archives/windowskuai-su-dao-chu-dao-ru-da-yin-ji)

2025-08-10 [用DiskGenius备份还原windows系统分区](/archives/yong-diskgeniusbei-fen-huan-yuan-windowsxi-tong-fen-qu)

Prev Post [给防火墙流量加一个web监控大屏](/archives/fw-log)

Next Post [做一个员工硬件配置上报工具](/archives/updata)

* * *
