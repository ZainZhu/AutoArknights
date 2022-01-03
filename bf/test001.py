from PIL import Image
from PIL import ImageGrab
import pytesseract, pyautogui, time, re


def ceshi1():
    text = pytesseract.image_to_string(Image.open('resources/graphics/text3.png'), lang="eng")
    print(text)
    pass


def ceshi2():
    all = [先锋干员, 狙击干员, 医疗干员, 术师干员, 近卫干员, 重装干员, 辅助干员, 输出,
           防护, 生存, 治疗, 费用回复, 群攻, 支援机械, 新手, 减速, 特种干员, 支援,
           快速复活, 削弱, 位移, 资深干员, 召唤, 控场, 爆发, 高级资深干员]
    yiban = [先锋干员, 狙击干员, 医疗干员, 术师干员, 近卫干员, 重装干员,
             辅助干员, 输出, 防护, 生存, 治疗, 费用回复, 群攻, 支援机械, 新手, 减速]
    zhuyao = [特种干员, 支援, 快速复活, 削弱, 位移]
    zishen = [资深干员, 召唤, 控场, 爆发]
    gaozi = [高级资深干员]
    # pyautogui.keyDown('win')
    # moniqi_pos = pyautogui.locateOnScreen('moniqi.png')
    # if moniqi_pos == None:
    #     goto_pos = 320, 1060
    # else:
    #     goto_pos = pyautogui.center(moniqi_pos)
    # pyautogui.keyUp('win')
    # pyautogui.click(goto_pos)
    # pyautogui.click(308, 995)

    # #点击左下招聘候选人
    # pyautogui.click(467, 995)
    # #点击右上跳过键
    # pyautogui.click(1831, 64)
    # pyautogui.PAUSE = 1
    # #点击任意位置
    # pyautogui.click(1831, 64)
    # 点击左下任意位置
    # pyautogui.click(467, 995)
    # 截图
    i = 0
    while i < 40:
        # image = pyautogui.screenshot(r'1_1.png',region=(564, 541, 216, 69))
        # print(im)
        image = Image.open("bf/text.png")
        # print(image)
        text = pytesseract.image_to_string(image, lang='chi_sim')
        textRegex = re.compile(r'(\w*)')
        text_ = textRegex.search(text).group()

        with open("resources/graphics/output.txt", 'a', encoding=" utf-8") as file:
            print(f"{text_}")
            file.write(str(text))
        i = i + 1
    # pyautogui.keyDown('win')
    # pyautogui.keyUp('win')
    # pyautogui.moveTo(370, 1060, duration = 0.1)
    # pyautogui.click()

    # pyautogui.mouseInfo()
    '''

    pyautogui.mouseInfo()
    705, 580
    '''

    pass


def ceshi3():
    image_list = []
    bbox = (565, 540, 780, 615)
    image_list.append(bbox)
    im = ImageGrab.grab(image_list[0])

    im.save('as.png')
    pass


def ceshi4():
    pass


def ceshi5():
    pass


if __name__ == '__main__':
    ceshi2()



