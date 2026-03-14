[English](README_EN.md)

---
# 一种在 Linux 下解决语音输入的办法

## 介绍
如果基于 fcitx5 插件写语音输入的话非常麻烦，并且在本地部署语音转文字效果不一定会很好，对接云端 API 的话又需要 money。但是手机语音转文字就非常方便了，直接用手机 ssh 连接到这个电脑，让 Python 脚本直接读取终端缓冲区的内容，复制到剪贴板，然后模拟按键粘贴就好了。

## 依赖

- [ydotool](https://github.com/ReimuNotMoe/ydotool)==0.1.8
- [wl-clipboard](https://github.com/bugaevc/wl-clipboard)==2.2.1
- [readchar](https://github.com/magmax/python-readchar)==4.2.1

## 测试环境

Linux 6.17.0-14-generic #14~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jan 15 15:52:10 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

Python==3.12.3

## 使用方法

通过ssh连接到这个电脑，运行 `python input_buffer.py`，在手机上输入语音转文字，按回车键发送，就会自动复制到剪贴板并粘贴到当前光标位置。

## 演示视频
