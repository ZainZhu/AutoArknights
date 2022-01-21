# 公开招募
# from source import setup


class End:
    def __init__(self):
        # 获取内容
        self.finished = True
        self.next = 'end'
        self.device_name = None
        self.abnormal_exit = False
        pass

    def update(self):

        pass

    def __call__(self, *args, **kwds):
        print("^" * 25 + "End" + "^" * 25)
        print(self.finished)
        self.getting_information()
        self.execute_action()
        pass

    def getting_information(self):
        print("负责获取程序当前运行状态")
        print("判断是否正常退出")

    def execute_action(self):

        if self.abnormal_exit == True:
            print("负责再次验证程序当前运行状态")
            print("负责报错和通知执行者")
            print("负责记录日志")
        else:
            print("正常退出输出结束语")
            print("xxx")
