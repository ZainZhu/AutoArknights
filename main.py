# -*- coding:utf-8 -*-
# Author: Jython Qjq


# 工具主入口

from source import tools
from source import tools
from source.states import public_recruitment
from source.states import investment_rystem


def main():
    state_dict = {
        'public_recruitment': public_recruitment.PublicRecruitment(),
        'investment_rystem': investment_rystem.InvestmentRystem(),
    }
    auto_ark = tools.Auto_Ark(state_dict, 'investment_rystem')

    auto_ark()


if __name__ == '__main__':
    main()
