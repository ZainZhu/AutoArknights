# 工具和脚本主控

import os
import time


class Auto_Ark():
    def __init__(self, state_dict, state_state):
        self.state_dict = state_dict
        self.state = self.state_dict[state_state]
        self.obj = self.state

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
            self.obj = self.state
        self.state.update()

    def __call__(self):
        self.obj()
        # self.update()
        pass

    def waiting_time(self):
        self.obj.waiting_time()
        pass

    def getting_information(self):
        self.obj.getting_information()
        pass

    def instruction_operation(self):
        self.obj.getting_information()
        pass

    def execute_action(self):
        self.obj.getting_information()
        pass

    ...


def read_device_name() -> list:
    """
    [读取设备名称]

    返回:
        list: [设备名称列表]
    """
    with os.popen(r'adb devices', 'r') as f:
        device_name_list = []
        devices = f.read()
        devices = devices.strip().split(
            "List of devices attached")[-1].split("\n")[1:]
        for i in devices:
            # print(i)
            x = i.split("\tdevice")[0]
            print(x)
            device_name_list.append(x)
        return device_name_list


class AdbHelper:
    """
    用于执行ADB相关操作
    """

    def __init__(self, device_name: str):
        """
        初始化 adb 操作对象, 使用 device_name 在 temp 里建立设备临时文件夹, 存储该 device 截图等
        :param device_name: 设备名称
        """
        os.getcwd()
        # 将类初始化参数 device_name 保存至当前对象变量 self.device_name
        self.device_name = device_name
        # 将设备名中 : 替换为 _ , 用于创建当前设备截图临时文件夹
        dir_name = device_name.replace(':', '_')
        # 当前设备临时文件夹相对路径
        self.device_dir = f"./temp/{dir_name}"
        print(f"初始化adb设备临时文件夹路径:{self.device_dir}")
        # 判断如果文件夹存在, 则删除文件夹
        if os.path.exists(self.device_dir):
            try:
                shutil.rmtree(self.device_dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        # 创建文件夹
        os.mkdir(self.device_dir)

    def screen_cap(self) -> None:
        """
        截取设备屏幕
        :return: None
        """
        # 根据指定设备名称截图, 名称为 sc.png
        os.system(
            f"adb -s {self.device_name} shell screencap -p /sdcard/sc.png")
        # 将截图文件存储在 temp 文件夹的当前设备名称路径下
        os.system(
            f"adb -s {self.device_name} pull /sdcard/sc.png {self.device_dir}")
