
import time
import threading
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()
clicking = False
interval = 0.1  # 初始连点间隔，默认0.1秒

def click_mouse():
    global interval
    while clicking:
        mouse.click(Button.left, 1)
        time.sleep(interval)

def on_press(key):
    global clicking
    if key == keyboard.Key.f2 and (keyboard.Controller().press(keyboard.Key.ctrl_l) or keyboard.Controller().press(keyboard.Key.ctrl_r)):
        clicking = not clicking
        if clicking:
            print("连点开始")
            threading.Thread(target=click_mouse).start()
        else:
            print("连点暂停")

def set_interval():
    global interval
    try:
        new_interval = float(input("请输入连点的时间间隔(秒)，最小0.01秒，最大5秒："))
        if 0.01 <= new_interval <= 5:
            interval = new_interval
            print(f"间隔时间设置为: {interval}秒")
        else:
            print("请输入一个有效的时间范围 (0.01-5 秒)")
            set_interval()
    except ValueError:
        print("无效的输入，请输入一个数字")
        set_interval()

def main():
    print("按Ctrl+F2开始或暂停连点")
    set_interval()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
