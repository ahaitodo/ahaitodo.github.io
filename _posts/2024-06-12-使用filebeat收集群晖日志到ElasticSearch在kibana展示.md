---
layout: mypost
author: 三九二七
title: "使用filebeat收集群晖日志到ElasticSearch在kibana展示"
date: 2024-06-12 00:00:00 +0800
categories: 工作
---

在ubuntu2204-1单机部署ElasticSearch

```
# 包安装ElasticSearch
wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/e/elasticsearch/elasticsearch-8.9.2-amd64.deb
dpkg -i elasticsearch-8.9.2-amd64.deb

# JVM优化
vim /etc/elasticsearch/jvm.options
## -Xms4g
-Xms1g
## -Xmx4g
-Xmx1g

# 关闭xpack安全功能
vim /etc/elasticsearch/elasticsearch.yml
xpack.security.enabled: false

systemctl enable --now elasticsearch.service

# 开启 bootstrap.memory_lock 优化

#修改elasticsearch.service
#vim /lib/systemd/system/elasticsearch.service
[Service]
#加下面一行
LimitMEMLOCK=infinity

systemctl daemon-reload 
systemctl restart elasticsearch.service
```

ElasticSearch安装完成