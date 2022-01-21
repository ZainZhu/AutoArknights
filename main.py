# -*- coding:utf-8 -*-
# Author: Jython Qjq


# 工具主入口

from source import tools
from source import setup
from source.states import public_recruitment
from source.states import investment_rystem
from source.states import end


def main() -> object:
    """
    [总控，负责调度，负责工具执行内容与执行设备的中控制]

    调用:
        object: Auto_Ark(设备名，执行内容字典，执行内容字典关键字)
    """
    # 执行内容字典
    state_dict = {
        'public_recruitment': public_recruitment.PublicRecruitment(),
        'investment_rystem': investment_rystem.InvestmentRystem(),
        'end':end.End()
    }
    for device_name in setup.C.device_name_list:
        auto_ark = tools.Auto_Ark(device_name, state_dict, 'investment_rystem')
        auto_ark()


if __name__ == '__main__':
    main()
