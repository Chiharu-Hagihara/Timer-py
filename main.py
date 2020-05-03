from time import sleep

target_time = 10


def down_timer(secs):
    # for i in range(0,secs):から変更
    for i in range(secs, -1, -1):
        print(i)
        sleep(1)
    print("時間です！")


down_timer(target_time)
