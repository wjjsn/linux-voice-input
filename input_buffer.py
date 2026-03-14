import threading
import readchar
import subprocess
import queue

# 共享缓冲区（线程安全）
send_buf = queue.Queue()

CONTROL_CHARS = {"\x03", "\x04", "\x1b", "\n", "\b", "\r", "\x08"}
running = threading.Event()
running.set()


def keyboard_listener():
    """专门负责监听按键的子线程"""
    try:
        print("按键监听已启动...")
        while running.is_set():
            key = readchar.readkey()
            if key in CONTROL_CHARS:
                continue
            send_buf.put(key)
    except KeyboardInterrupt:
        running.clear()
    except Exception as e:
        print(f"按键监听出错: {e}")


def main():
    while running.is_set():
        try:
            first_key = send_buf.get(timeout=0.5)
        except queue.Empty:
            continue

        # 取出当前已有的按键序列
        current_keys = [first_key]
        while running.is_set():
            try:
                current_keys.append(send_buf.get_nowait())
            except queue.Empty:
                break

        # 在这里处理按键序列
        subprocess.run(f"wl-copy {''.join(current_keys)} --primary", shell=True)
        subprocess.run(f"wl-copy {''.join(current_keys)}", shell=True)
        result = subprocess.run(
            "sudo ydotool key Shift+Insert", shell=True, stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            print("执行 ydotool 失败")
        else:
            print(f"已复制粘贴: {''.join(current_keys)}")


if __name__ == "__main__":
    t = threading.Thread(target=keyboard_listener, daemon=True)
    t.start()
    main()
    print("\n程序结束")
