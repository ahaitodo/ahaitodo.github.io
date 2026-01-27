---
layout: post
title: "Git常用命令速查表"
date: 2026-01-26 14:30:00 +0800
categories: 技术 工具
---

## 📚 Git常用命令整理

作为开发者，Git是每天都要用到的版本控制工具。这里整理了一份常用命令速查表，方便日常查阅。

### 基础操作

```bash
# 初始化仓库
git init

# 克隆远程仓库
git clone <url>

# 查看状态
git status

# 查看修改
git diff
```

### 提交代码

```bash
# 添加文件到暂存区
git add <file>
git add .

# 提交更改
git commit -m "提交信息"

# 修改最后一次提交
git commit --amend
```

### 分支操作

```bash
# 查看分支
git branch

# 创建分支
git branch <branch-name>

# 切换分支
git checkout <branch-name>

# 创建并切换分支
git checkout -b <branch-name>

# 合并分支
git merge <branch-name>

# 删除分支
git branch -d <branch-name>
```

### 远程操作

```bash
# 查看远程仓库
git remote -v

# 拉取远程更新
git pull

# 推送到远程
git push origin <branch-name>

# 设置上游分支
git push -u origin <branch-name>
```

### 历史查看

```bash
# 查看提交历史
git log

# 简洁查看历史
git log --oneline

# 图形化查看历史
git log --graph --oneline --all
```

## 💡 实用技巧

### 1. 撤销操作

```bash
# 撤销工作区修改
git checkout -- <file>

# 撤销暂存区的文件
git reset HEAD <file>

# 回退到某个版本
git reset --hard <commit-id>
```

### 2. 储藏功能

```bash
# 储藏当前修改
git stash

# 查看储藏列表
git stash list

# 应用储藏
git stash apply

# 应用并删除储藏
git stash pop
```

### 3. 标签管理

```bash
# 创建标签
git tag v1.0.0

# 查看标签
git tag

# 推送标签
git push origin v1.0.0
```

## 🎯 最佳实践

1. **提交信息规范**：使用清晰的提交信息，如 `feat:`, `fix:`, `docs:` 等前缀
2. **经常提交**：小步快跑，频繁提交可以更好地追踪变化
3. **分支策略**：使用功能分支进行开发，保持主分支稳定
4. **定期同步**：经常拉取远程更新，避免冲突积累

## 结语

熟练掌握Git命令可以大大提升开发效率。建议多在实际项目中练习，逐步建立肌肉记忆！

Happy Coding! 🚀
