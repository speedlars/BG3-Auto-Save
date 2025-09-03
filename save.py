<<<<<<< HEAD
import tkinter as tk
import threading
import time
import pydirectinput
from datetime import datetime

min = 5

class AutoRefreshApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Refresh Controller")
        self.running = False

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        # 狀態顯示區域
        self.status_label = tk.Label(root, text="狀態：未啟動", fg="blue")
        self.status_label.pack(pady=5)

        self.action_label = tk.Label(root, text="動作：尚未執行", fg="green")
        self.action_label.pack(pady=5)

        self.thread = threading.Thread(target=self.auto_refresh)
        self.thread.daemon = True
        self.thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_status(self, message):
        self.status_label.config(text=f"狀態：{message}")

    def update_action(self, message):
        self.action_label.config(text=f"動作：{message}")

    def start(self):
        self.running = True
        self.update_status("已啟動")

    def stop(self):
        self.running = False
        self.update_status("已暫停")

    def auto_refresh(self):
        while True:
            if self.running:
                pydirectinput.keyDown('f5')
                time.sleep(1)
                pydirectinput.keyUp('f5')
                current_time = datetime.now().strftime("%H:%M")
                self.update_action(f"{current_time} 已存檔")
            time.sleep(min * 60)

    def on_close(self):
        self.running = False
        self.update_status("已關閉")
        self.root.destroy()

# 建立主視窗
root = tk.Tk()
app = AutoRefreshApp(root)
root.mainloop()
=======
import tkinter as tk
import threading
import time
import pydirectinput
from datetime import datetime

min = 5

class AutoRefreshApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Refresh Controller")
        self.running = False

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        # 狀態顯示區域
        self.status_label = tk.Label(root, text="狀態：未啟動", fg="blue")
        self.status_label.pack(pady=5)

        self.action_label = tk.Label(root, text="動作：尚未執行", fg="green")
        self.action_label.pack(pady=5)

        self.thread = threading.Thread(target=self.auto_refresh)
        self.thread.daemon = True
        self.thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_status(self, message):
        self.status_label.config(text=f"狀態：{message}")

    def update_action(self, message):
        self.action_label.config(text=f"動作：{message}")

    def start(self):
        self.running = True
        self.update_status("已啟動")

    def stop(self):
        self.running = False
        self.update_status("已暫停")

    def auto_refresh(self):
        while True:
            if self.running:
                pydirectinput.keyDown('f5')
                time.sleep(1)
                pydirectinput.keyUp('f5')
                current_time = datetime.now().strftime("%H:%M")
                self.update_action(f"{current_time} 已存檔")
            time.sleep(min * 60)

    def on_close(self):
        self.running = False
        self.update_status("已關閉")
        self.root.destroy()

# 建立主視窗
root = tk.Tk()
app = AutoRefreshApp(root)
root.mainloop()
>>>>>>> a3c0adf (Update from git)
