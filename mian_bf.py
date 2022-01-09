#!/uer/bin/env python
# -*- coding:utf-8 -*-
# Author: Jython
# Utilities 相关函式库

from PIL import Image
from PIL import ImageGrab
# 图像处理/展现的相关函数库
# import matplotlib.pyplot as plt
import pytesseract
import pyautogui
import re
import time
import os
import yaml

with open(r'config.yaml', encoding="UTF-8") as f:
    config = yaml.full_load(f)

print("END")
def run():
    # 获取内容
    all = ["先锋干员", "狙击干员", "医疗干员", "术师干员", "近卫干员", "重装干员", "辅助干员", "输出",
           "防护", "生存", "治疗", "费用回复", "群攻", "支援机械", "新手", "减速", "特种干员", '支援',
           "快速复活", "削弱", "位移", "资深干员", "召唤", "控场", "爆发", "高级资深干员"]
    yiban = ["先锋干员", "狙击干员", "医疗干员", "术师干员", "近卫干员", "重装干员", "辅助干员", "输出",
             "防护", "生存", "治疗", "费用回复", "群攻", "支援机械", "新手", "减速"] 
    zhuyao = ["特种干员", '支援', "快速复活", "削弱", "位移"]
    zishen = ["资深干员", "召唤", "控场", "爆发"]
    gaozi = ["高级资深干员"]

    # 选择目标
    pyautogui.keyDown('win')
    moniqi_pos = pyautogui.locateOnScreen(r'D:\Project\git\AutoArknights\moniqi.png')
    if moniqi_pos == None:
        goto_pos = 320, 1060
    else:
        goto_pos = pyautogui.center(moniqi_pos)
    pyautogui.keyUp('win')
    pyautogui.click(goto_pos)
    pyautogui.click(308, 995)

    # #点击左下
    pyautogui.click(467, 995)
    # #点击右上跳过键
    # pyautogui.click(1831, 64)
    # pyautogui.PAUSE = 1
    # #点击任意位置
    # pyautogui.click(1831, 64)
    # 点击左下任意位置
    # pyautogui.click(467, 995)
    # 截图
    i = 1
    # 开关
    switch = 5
    # 计数器
    counter = 0
    while counter > (switch / 2 + 1):
        image = pyautogui.screenshot(r'D:\Project\git\AutoArknights\1_1.png', region=(564, 541, 216, 69))
        # print(im)
        # image = Image.open("bf/text.png")
        # print(image)
        text = pytesseract.image_to_string(image, lang='chi_sim')
        textRegex = re.compile(r'(\w*)')
        text_filter = textRegex.search(text).group()

        with open("../resources/graphics/output.txt", 'a', encoding=" utf-8") as file:
            print(f"{text_filter}")
            file.write(str(text))
        if text_filter in all:
            counter += 1
        i += i

    pyautogui.keyDown('win')
    pyautogui.keyUp('win')
    pyautogui.moveTo(370, 1060, duration = 0.1)
    pyautogui.click()


class AutoArknights:
    def __init__(self):
        print("auto_ark_nights init.")


# 根目录路径
root_dir = os.getcwd()
# 训练/验证用的资料目录
data_path = os.path.join(root_dir, 'image')
# 测试用的图像
test_image = os.path.join(data_path, 'ASCII_Code.png')


# 载入图像
# image = Image.open(test_image)

# 存储图像并转换格式(jpg->png)
# image.save(os.path.join(data_path, 'new_image.png'))
#
# plt.imshow(image)
# plt.show()

# pyautogui.mouseInfo()
'''
pyautogui.mouseInfo()
705, 580
'''
pass


if __name__ == '__main__':
    run()