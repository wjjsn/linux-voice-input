# Voice Input Solution for Linux

## Introduction

Developing a voice input solution based on fcitx5 plugins can be quite cumbersome. Additionally, deploying speech-to-text locally may not yield optimal results, while using cloud APIs can be costly. However, mobile speech-to-text is very convenient - simply use your phone to SSH into your computer, let the Python script read the terminal buffer, copy to clipboard, and simulate key presses to paste.

## Dependencies

- [ydotool](https://github.com/ReimuNotMoe/ydotool) == 0.1.8
- [wl-clipboard](https://github.com/bugaevc/wl-clipboard) == 2.2.1
- [readchar](https://github.com/magmax/python-readchar) == 4.2.1

## Test Environment

Linux 6.17.0-14-generic #14~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jan 15 15:52:10 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

Python == 3.12.3

## Usage

SSH into your computer from your phone, run `python input_buffer.py`, then use voice-to-text on your phone and press Enter to send. The text will automatically be copied to the clipboard and pasted at the current cursor position.

## Demo Video
