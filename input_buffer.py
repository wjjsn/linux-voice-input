import threading
import readchar
import subprocess
import queue

# 共享缓冲区（线程安全）
send_buf = queue.Queue()

def keyboard_listener():
    """专门负责监听按键的子线程"""
    try:
        print("按键监听已启动...")
        while True:
            # 这里会阻塞，但只阻塞这个子线程
            key = readchar.readkey()
            if key == '\n':  # 过滤掉回车键
                continue
            send_buf.put(key)
    except KeyboardInterrupt:
        print("\n按键监听已停止")
        return
        exit(0)
    except Exception as e:
        print(f"按键监听出错: {e}")

def main():
    while True:
        # 阻塞等待第一个按键（避免空转和固定睡眠）
        first_key = send_buf.get()

        # 取出当前已有的按键序列
        current_keys = [first_key]
        while True:
            try:
                current_keys.append(send_buf.get_nowait())
            except queue.Empty:
                break

        # 在这里处理按键序列
        subprocess.run(f"wl-copy {''.join(current_keys)} --primary", shell=True)
        subprocess.run(f"wl-copy {''.join(current_keys)}", shell=True)
        subprocess.run("sudo ydotool key Shift+Insert", shell=True)

if __name__ == "__main__":
    try:
        t = threading.Thread(target=keyboard_listener, daemon=True)
        t.start()
        main()
    except KeyboardInterrupt:
        print("\n程序结束")
