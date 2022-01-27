import re
from time import sleep, time
from PIL import Image
import pytesseract
import os
import cv2
import aircv as ac
import yaml


device_name = "127.0.0.1:21513"

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
    imgsrc = 'r' + imgsrc
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


def image_t_str(imgsrc):
    # image = Image.open(r'../temp/127.0.0.1_21523/sc.png')
    # imgsrc = 'r' + imgsrc
    image = Image.open(imgsrc)  
    with open(r'./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader) 
    # print(database) 
    box = tuple_data(database['识别区域']['I_1'])  # 确定拷贝区域大小
    region = image.crop(box)  # 将im表示的图片对象拷贝到region中，大小为box
    # region.show()  
    text = pytesseract.image_to_string(region, lang='chi_sim')
    # print(text)
    textRegex = re.compile(r'(\w*)')
    text_filter = textRegex.search(text).group()
    print(text_filter)

def image_t_int(imgsrc):
    # image = Image.open(r'../temp/127.0.0.1_21523/sc.png')
    image = Image.open(imgsrc)  
    with open(r'./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader) 
    box = tuple_data(database['识别区域']['id'])  # 确定拷贝区域大小
    region = image.crop(box)  # 将im表示的图片对象拷贝到region中，大小为box
    region = region.resize((200, 40),Image.ANTIALIAS)  
    region = region.convert('L')   
    threshold = 150  
    table = []  
    for i in range(256):  
        if i < threshold:
            table.append(0) 
        else:
            table.append(1)
    region = region.point(table, '1')
    # region.show() 
    text = pytesseract.image_to_string(region)
    # print(text)
    textRegex = re.compile(r'(\w*)')
    text_filter = textRegex.search(text).group()
    print(text_filter)


def other_test():
    with open('./data/database.yaml', encoding="UTF-8") as f:
        database = yaml.load(f, Loader=yaml.Loader)
    print(database)
    print(type(database['点击区域']['清除缓存']))

    x = tuple_data(database['点击区域']['清除缓存'])

    print(x)
    print(type(x))
    pass

# x = matchImg(r'../bf/image/sc_xzfd_jj2.png', r'../bf/image/xzfd_yes.png', 0.4)
# print(x)


image_t_str(r'../temp/127.0.0.1_21523/sc.png')

image_t_int(r'../bf/image/sc copy.png') 


# other_test()

