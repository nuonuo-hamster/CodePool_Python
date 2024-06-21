import time

def update_display():
    for i in range(10):
        # 清除当前行
        print("\r", end="")
        # 输出新内容
        print("Loading: [{}]".format("#" * i), end="")
        # 等待一段时间
        time.sleep(0.5)
    print("\r", end="")

update_display()
