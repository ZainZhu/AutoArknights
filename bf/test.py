#!/uer/bin/env python
# -*- coding:utf-8 -*-
# Author: Jython
# Utilities 相关函式库

from PIL import Image
from PIL import ImageGrab
# 图像处理/展现的相关函数库
import matplotlib.pyplot as plt
import pytesseract
import pyautogui
import re
import time
import os
import yaml

with open(r'../config.yaml', encoding="UTF-8") as f:
    config = yaml.full_load(f)
pyautogui.keyDown('win')

print("END")
