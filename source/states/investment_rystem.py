# 前瞻性投资系统
import os
import time
from source.abc import BaseAction
from source import setup
from source import tools


class InvestmentRystem(BaseAction):
    def __init__(self):
        # 获取内容
        self.read_config()
        self.finished = False
        self.next = 'end'
        self.device_name = None


        pass

    # TODO: 没有设计好
    def update(self):
        pass

    def __call__(self, *args, **kwds):
        print("+" * 25 + "前瞻性投资系统" + "+" * 25)
        print(self.finished)
        self.waiting_time()
        self.getting_information()
        self.instruction_operation()
        self.execute_action()
        pass

    def waiting_time(self):
        time.sleep(0)
        print("将在待机0s时间后运行")
        pass

    def getting_information(self):
        print("负责获取程序窗口")
        # print(setup.C.device_name_list)
        print(self.device_name)
        adb_helper = tools.AdbHelper(self.device_name)
        adb_helper.screen_cap()
        print("负责获取程序当前运行状态")
        print("负责调整程序运行状态")
        print("负责获取程序之后操作所需的信息")

        print("负责获取程序操作的最终目的")
        pass

    def instruction_operation(self):
        print("负责计算完成目标的指令")
        print("负责判断目标是否需要循环完成和构建循环本体")
        print("负责每次循环之间的等待时间")
        print("负责输出指令集")
        pass

    def execute_action(self):
        print("负责再次验证程序当前运行状态")
        print("按照指令集操作")
        print("负责再次验证程序当前运行状态")
        print("负责报错和通知执行者")
        print("负责记录日志")
        # x = input("任务是否完成？：")
        x = "True"
        if x == "True":
            self.finished = True
        pass

    def read_config(self):
        self.config = setup.C.config
        pass
