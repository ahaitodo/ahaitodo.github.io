---
layout: mypost
author: 三九二七
title: "为什么Google Chrome，输入某个域名会自动加https？"
date: 2023-09-17 00:00:00 +0800
categories: 分享
---

Google Chrome 浏览器有一个功能叫做 "HSTS" (HTTP Strict Transport Security)，
![01.png](/assets/images/sjeq/202309171694953487283036.png)

HSTS 是一项安全策略技术，通过服务器向浏览器发送特殊的响应头，要求浏览器只能通过 HTTPS 访问服务器，而不能使用 HTTP。

如果你曾经访问过该网站并且该网站启用了 HSTS，那么 Google Chrome 会记住这个设置，并在以后的访问中自动将 HTTP 转换为 HTTPS。这也就是为什么你每次输入域名时，Chrome 都会自动加上 https。

其它浏览器（如 Firefox 和 Safari）也支持 HSTS，但如果你没有在那些浏览器上访问过启用了 HSTS 的网站，那么它们不会自动添加 https。

请注意，一旦一个网站被浏览器记录为使用 HSTS，将很难取消。即使网站取消了SSL证书，你的电脑访问域名，还是会自动启用https，这个时候，如果用你Chrome ，则要在 Chrome 中，需要进入 chrome://net-internals/#hsts 页面，在 "Delete domain" 部分输入你的网站域名，然后点击 "Delete" 按钮。但请注意，HSTS 是一种重要的安全特性，禁用它可能会降低你的站点安全性。