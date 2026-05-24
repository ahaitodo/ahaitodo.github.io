---
layout: mypost
author: 三九二七
title: "Proxmox VE 删除节点下的VM"
date: 2021-12-28 00:00:00 +0800
categories: 工作
---

mv /etc/pve/nodes/nodename /root/nodename

注意空格

删除其中一个，则

rm /etc/pve/nodes/nodename/qemu-server/101.conf