# -*- coding:utf-8 -*-
# Author: Jython Qjq


# 工具主入口
# 工具和脚本主控q
from source import tools
from source.states import public_recruitment


def main():
    auto_ark = tools.Auto_Ark()
    auto_ark.obj = public_recruitment.PublicRecruitment()
    auto_ark()


if __name__ == '__main__':
    main()
