import re
from time import sleep, time
from PIL import Image
import pytesseract
import os
import cv2
import aircv as ac
import yaml


device_name = "127.0.0.1:21503"

def tuple_data(data):
    return eval((repr(data).replace("\'", "")))

def adb_shell_tap(device_name, x):
    os.system(f"adb -s {device_name} shell input tap {x}")

def adb_shell_swipe(device_name, x):
    os.system(f"adb -s {device_name} shell input swipe {x}")


def matchImg(imgsrc, imgobj, confidencevalue=0.5):  # imgsrc=原始图像，imgobj=待查找的图片
    with open(r'./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader)
    x = database['模拟滑动']['模拟滑动至远程战术分队']
    print(x)
    adb_shell_swipe(device_name, x)
    x = database['点击位置']['点击远程战术分队']
    # sleep(2)
    print(x)
    adb_shell_tap(device_name, x)
    x = database['点击位置']['确认远程战术分队']
    # sleep(2)
    print(x)
    adb_shell_tap(device_name, x)
    image = Image.open(imgsrc)
    # image.show()
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_template(imsrc, imobj, confidencevalue)
    if match_result is not None:
        print(match_result)
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    else:
        match_result = '识别率在' + str(confidencevalue) + '时，没有识别到任何信息'
    return match_result


def image_t_str():
    image = Image.open(r'../temp/127.0.0.1_62025/sc.png') 
    with open(r'./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader)
    print(database) 
    box = tuple_data(database['点击区域']['清除缓存'])  # 确定拷贝区域大小
    region = image.crop(box)  # 将im表示的图片对象拷贝到region中，大小为box
    # image.show()
    region.show()
    # image = pyautogui.screenshot(r'D:\Project\git\AutoArknights\1_1.png', region=(564, 541, 216, 69))
    # print(im)
    # image = Image.open("bf/text.png")
    # print(image)
    text = pytesseract.image_to_string(region, lang='chi_sim')
    print(text)
    textRegex = re.compile(r'(\w*)')
    text_filter = textRegex.search(text).group()
    # print(text_filter)


def other_test():
    with open(r'./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader)
    print(database)
    print(type(database['点击区域']['清除缓存']))

    x = tuple_data(database['点击区域']['清除缓存'])

    print(x)
    print(type(x))
    pass

x = matchImg(r'../bf/image/sc_xzfd_jj2.png', r'../bf/image/xzfd_yes.png', 0.4)
print(x)


# image_t_str()


# other_test()

