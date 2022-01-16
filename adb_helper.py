#!/uer/bin/env python
# -*- coding:utf-8 -*-
# Author: ZainZhu
import os
import shutil


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
        os.system(f"adb -s {self.device_name} shell screencap -p /sdcard/sc.png")
        # 将截图文件存储在 temp 文件夹的当前设备名称路径下
        os.system(f"adb -s {self.device_name} pull /sdcard/sc.png {self.device_dir}")


# test
# dev_1_adb = AdbHelper("127.0.0.1:21503")
# dev_1_adb.screen_cap()
# dev_2_adb = AdbHelper("127.0.0.1:21513")
# dev_2_adb.screen_cap()
