---
layout: mypost
title: "测小米MiMo V2.5邀请码QJC7J2：价格打平DeepSeek"
date: 2026-06-07
categories: 默认分类
tags: [AI Agent, Token, ai]
---

## 写在前边

我在用 MiMo 开放平台体验 小米顶尖模型 MiMo V2.5等 ，通过我的邀请码注册为新用户，即得 ¥10 API 体验金。邀请码：QJC7J2。注册：<https://platform.xiaomimimo.com/?ref=QJC7J2>（注册后点控制台左下方入口填入，体验金40天有效）

安装也很简单，在终端运行一行脚本即可安装

npm install -g @mimo-ai/cli 

复制到终端回车一键安装体验。MiMo-V2.5 限免中，装好直接可用不用配置API-KEY。

![](/assets/images/ya0/image-lfux.png)  
大模型圈最近真的太卷了。前有 DeepSeek 打出“骨折价”，后有一众厂商跟进。但最近让我比较惊喜的，是小米旗下的 MiMo 开放平台。

很多人对小米大模型的印象还停留在“手机助手”，但如果你去关注一下最新的 benchmarks（基准测试），会发现他们的 **MiMo V2.5 Pro** 已经在悄悄屠榜了——SWE-bench 编程测试得分 57.2%，甚至超过了 DeepSeek V4 Pro。

![](/assets/images/ya0/a28985577afb3e3e950f13007c814c1f.png)

更关键的是，**价格完全对齐 DeepSeek** ：标准版输入（缓存）仅 2 分钱/百万 tokens，Pro 版输入（缓存）也只要 2 分 5。但 MiMo 是**多模态模型** ，除了读文字，还能直接看懂图片、听懂音频、分析视频。相当于用纯文本模型的价格，买到一个“长眼睛耳朵”的模型。

![](/assets/images/ya0/221e38c51c30d096cacfa728ed72ad50.png)

**我为什么觉得 MiMo V2.5 值得一试？**

  * **多模态原生支持** ：不再需要把图片转成文字描述喂给模型，直接传图、传视频，它就能理解。

  * **Token 效率极高** ：官方数据显示，在 ClawEval 任务解决测试中，Pro 版每条任务轨迹仅消耗约 7 万 Token，比 GPT-5.4 等模型减少 40%-60% 的消耗。这意味着同样的任务，你花的钱更少。

  * **编程与 Agent 能力突出** ：小米自研的 MiMo Coding Bench 评测中，Pro 版得分（73.7）已非常接近 Claude Opus 4.6（77.1）。




## **🔑 如何获取 MiMo API Key（超详细步骤）**

拿到体验金后，很多朋友可能不知道 API Key 在哪里生成。别担心，跟着下面 4 步走就行：

### **第 1 步：注册账号并领取体验金**

点击链接注册：<https://platform.xiaomimimo.com/?ref=QJC7J2>

注册完成后，登录控制台，在页面**左下方** 找到“邀请码/优惠券”入口，输入邀请码：**QJC7J2** ，¥10 体验金会自动到账。

### **第 2 步：进入 API Keys 管理页面**

登录 [MiMo 开放平台控制台](https://platform.xiaomimimo.com/#/console/api-keys)，在左侧菜单栏找到 **「API Keys」** 选项，点击进入。

### **第 3 步：创建新的 API Key**

点击页面上的 **「新建 API Key」** 或 **「Create API Key」** 按钮，弹窗后会让你给这个 Key 起一个名字（比如 “my-first-key”），方便以后管理。

### **第 4 步：复制并保存 API Key**

点击创建后，系统会生成一串以 `sk-` 开头的密钥。

> ⚠️ **重要提醒** ：这个 Key **只会在创建成功后显示一次** ！关闭页面后就再也看不到了。请务必**立即复制** 并保存到安全的地方（比如密码管理器或本地记事本）。如果不小心关掉了，只能重新建一个新的。

创建完成后，你就可以用这个 API Key 配合以下信息调用 MiMo 模型了：

**配置项**| **值**  
---|---  
**API Base URL**| `https://api.xiaomimimo.com/v1`  
**API Key**|  你刚才复制的 `sk-xxxxx`  
**模型名称示例**| `mimo-v2.5-pro` 或 `mimo-v2.5`  
  
## **🛠️ 配置到常用客户端**

### **方式一：Cherry Studio（推荐，最简单）**

Cherry Studio 已经**内置了 Xiaomi MiMo 的支持** ：

  1. 打开 Cherry Studio → 左下角「设置」→「模型服务」

  2. 直接搜索「Xiaomi MiMo」

  3. 填入你刚才复制的 API Key 即可（Host 默认不用改）




### **方式二：OpenAI 兼容客户端（Chatbox、NextChat、Open WebUI 等）**

由于 MiMo 兼容 OpenAI API 协议，任何支持 OpenAI 接口的客户端都可以直接接入：

  * **Base URL** ：`https://api.xiaomimimo.com/v1`

  * **API Key** ：你的 `sk-xxxxx`

  * **模型名** ：`mimo-v2.5-pro` 或 `mimo-v2.5`




### **方式三：代码直接调用（Node.js 示例）**

javascript
    
    
    const axios = require("axios");
    
    async function chat() {
      const res = await axios.post(
        "https://api.xiaomimimo.com/v1/chat/completions",
        {
          model: "mimo-v2.5-pro",
          messages: [{ role: "user", content: "你好，请介绍一下自己" }]
        },
        {
          headers: {
            Authorization: "Bearer sk-你的key",
            "Content-Type": "application/json"
          }
        }
      );
      console.log(res.data);
    }
    
    chat();

## **📋 推荐上手场景**

  * **代码开发** ：让 MiMo V2.5 Pro 帮你写单元测试、解释复杂代码

  * **图文理解** ：上传一张产品截图，让它生成 HTML/CSS 代码

  * **视频摘要** ：给它一个短视频链接，让它总结视频核心内容




## **💎 写在最后**

现在的 MiMo V2.5 系列，价格打平 DeepSeek，能力对标 Claude 和 GPT 的顶配版，而且还有多模态加持。趁着现在有体验金，感兴趣的可以注册试试，看看小米这支低调的 AI 团队到底做到了什么水平。

**邀请码：QJC7J2**  
**注册地址：** <https://platform.xiaomimimo.com/?ref=QJC7J2>
