# 工具和脚本
from . import read_config as C


class Auto_Ark():
    def __init__(self):
        # 获取内容
        self.read_config()
        
        pass

    def __call__(self, *args, **kwds):
        print(self.config)
        pass

    def read_config(self):
        self.config = C.config
        pass

    pass
