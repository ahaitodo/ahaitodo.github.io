#!/usr/bin/env python3
"""
sjeq.com 文章迁移脚本
从 Z-Blog PHP 网站抓取文章并转换为 Jekyll Markdown 格式
"""

import os
import re
import html
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

# 文章ID列表
ARTICLE_IDS = [
    # 分享分类
    1, 3, 11, 12, 13, 14, 15, 17, 18, 19, 20,
    # 工作分类
    4, 5, 6, 7, 8, 9, 10, 16, 21, 22
]

BASE_URL = "https://www.sjeq.com/?id={}"
OUTPUT_DIR = Path("_posts")
IMAGE_DIR = Path("assets/images/sjeq")

# 分类映射
CATEGORY_MAP = {
    "分享": "分享",
    "工作": "工作"
}

def clean_html_content(html_content):
    """清理HTML内容，转换为纯文本/Markdown"""
    # 移除style标签和内容
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)
    # 移除script标签和内容
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    # 处理图片 - 获取真实URL
    html_content = re.sub(
        r'<img[^>]*data-original="([^"]+)"[^>]*>',
        lambda m: f'![image]({m.group(1)})',
        html_content
    )
    html_content = re.sub(
        r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>',
        lambda m: f'![{m.group(2)}]({m.group(1)})',
        html_content
    )
    # 处理链接
    html_content = re.sub(
        r'<a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>',
        lambda m: f'[{m.group(2)}]({m.group(1)})',
        html_content
    )
    # 处理换行
    html_content = re.sub(r'<br\s*/?>', '\n', html_content)
    html_content = re.sub(r'<br[^>]*>', '\n', html_content)
    # 处理段落
    html_content = re.sub(r'<p[^>]*>', '\n', html_content)
    html_content = re.sub(r'</p>', '\n', html_content)
    # 处理标题
    html_content = re.sub(r'<h1[^>]*>([^<]+)</h1>', lambda m: f'# {m.group(1)}', html_content)
    html_content = re.sub(r'<h2[^>]*>([^<]+)</h2>', lambda m: f'## {m.group(1)}', html_content)
    html_content = re.sub(r'<h3[^>]*>([^<]+)</h3>', lambda m: f'### {m.group(1)}', html_content)
    html_content = re.sub(r'<h4[^>]*>([^<]+)</h4>', lambda m: f'#### {m.group(1)}', html_content)
    # 处理列表
    html_content = re.sub(r'<li[^>]*>([^<]+)</li>', lambda m: f'- {m.group(1)}', html_content)
    html_content = re.sub(r'<ul[^>]*>', '\n', html_content)
    html_content = re.sub(r'</ul>', '\n', html_content)
    html_content = re.sub(r'<ol[^>]*>', '\n', html_content)
    html_content = re.sub(r'</ol>', '\n', html_content)
    # 处理strong/b
    html_content = re.sub(r'<strong[^>]*>([^<]+)</strong>', lambda m: f'**{m.group(1)}**', html_content)
    html_content = re.sub(r'<b[^>]*>([^<]+)</b>', lambda m: f'**{m.group(1)}**', html_content)
    # 处理em/i
    html_content = re.sub(r'<em[^>]*>([^<]+)</em>', lambda m: f'*{m.group(1)}*', html_content)
    html_content = re.sub(r'<i[^>]*>([^<]+)</i>', lambda m: f'*{m.group(1)}*', html_content)
    # 处理代码
    html_content = re.sub(r'<code[^>]*>([^<]+)</code>', lambda m: f'`{m.group(1)}`', html_content)
    html_content = re.sub(r'<pre[^>]*>([^<]+)</pre>', lambda m: f'\n```\n{m.group(1)}\n```\n', html_content)
    # 移除其他HTML标签
    html_content = re.sub(r'<[^>]+>', '', html_content)
    # 解码HTML实体
    html_content = html.unescape(html_content)
    # 清理多余空行
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    # 清理多余空格
    html_content = re.sub(r'  +', ' ', html_content)
    return html_content.strip()

def extract_article_info(html_text, article_id):
    """从HTML中提取文章信息"""
    info = {
        'id': article_id,
        'title': '',
        'date': '',
        'category': '',
        'content': ''
    }

    # 提取标题
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_text)
    if title_match:
        info['title'] = html.unescape(title_match.group(1).strip())

    # 提取日期 - 格式: (2010-05-28)
    date_match = re.search(r'\((\d{4}-\d{2}-\d{2})\)', html_text)
    if date_match:
        info['date'] = date_match.group(1)
    else:
        info['date'] = datetime.now().strftime('%Y-%m-%d')

    # 提取分类
    cate_match = re.search(r'<span class="cate"><a[^>]*>([^<]+)</a></span>', html_text)
    if cate_match:
        info['category'] = html.unescape(cate_match.group(1).strip())

    # 提取正文内容 - 在 div class="single" 内
    content_match = re.search(r'<div class="single[^"]*"[^>]*>(.*?)</div>\s*<div class="copynotice"', html_text, re.DOTALL)
    if content_match:
        info['content'] = clean_html_content(content_match.group(1))

    return info

def generate_filename(info):
    """生成Jekyll格式的文件名"""
    # 格式: YYYY-MM-DD-title.md
    date = info['date']
    # 处理标题 - 移除特殊字符，转换为小写，用连字符连接
    title = info['title']
    # 中文标题保留，替换特殊字符
    title_safe = re.sub(r'[^\w一-鿿\-]', '-', title)
    title_safe = re.sub(r'-+', '-', title_safe).strip('-')

    filename = f"{date}-{title_safe}.md"
    return filename

def create_markdown_file(info):
    """创建Markdown文件"""
    filename = generate_filename(info)
    filepath = OUTPUT_DIR / filename

    # 构建frontmatter
    frontmatter = f"""---
layout: mypost
author: 三九二七
title: "{info['title']}"
date: {info['date']} 00:00:00 +0800
categories: {info['category']}
---

"""

    full_content = frontmatter + info['content']

    return filepath, full_content

def download_image(url, local_path):
    """下载图片到本地"""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            local_path.parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"下载图片失败: {url} - {e}")
    return False

def replace_image_urls(content, article_id):
    """替换图片URL为本地路径"""
    # 找到所有图片URL
    image_urls = re.findall(r'!\[.*?\]\(([^)]+)\)', content)

    for url in image_urls:
        # 提取文件名
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
            continue

        # 本地路径
        local_path = IMAGE_DIR / filename
        new_url = f"/assets/images/sjeq/{filename}"

        # 下载图片
        print(f"下载图片: {url}")
        download_image(url, local_path)

        # 替换URL
        content = content.replace(url, new_url)

    return content

def fetch_article(article_id):
    """抓取单篇文章"""
    url = BASE_URL.format(article_id)
    print(f"抓取文章: {url}")

    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"抓取失败: {url} - {e}")
    return None

def main():
    """主函数"""
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    fail_count = 0

    for article_id in ARTICLE_IDS:
        print(f"\n处理文章 ID={article_id}")

        html_text = fetch_article(article_id)
        if not html_text:
            fail_count += 1
            continue

        info = extract_article_info(html_text, article_id)
        if not info['title']:
            print(f"未能提取标题，跳过 ID={article_id}")
            fail_count += 1
            continue

        # 替换图片URL
        info['content'] = replace_image_urls(info['content'], article_id)

        # 创建文件
        filepath, content = create_markdown_file(info)

        # 检查文件是否已存在
        if filepath.exists():
            print(f"文件已存在: {filepath}")
            # 添加文章ID区分
            filepath = OUTPUT_DIR / f"{info['date']}-{info['title']}-{article_id}.md"

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"创建文件: {filepath}")
        print(f"标题: {info['title']}")
        print(f"日期: {info['date']}")
        print(f"分类: {info['category']}")

        success_count += 1

    print(f"\n迁移完成: 成功 {success_count} 篇, 失败 {fail_count} 篇")

if __name__ == '__main__':
    main()