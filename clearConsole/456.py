import time

def update_display():
    for i in range(10):
        # 清除当前内容
        print("\033[H\033[J", end="")
        # 输出新内容
        for j in range(i):
            j +=i
            print("Loading: [{}]".format("#" * j))
        # 等待一段时间
        time.sleep(0.5)

update_display()