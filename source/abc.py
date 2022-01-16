# 定义行为类规则 方便联合开发
# 所有行为均需要有四个基础方法
#     待机时间 | waiting_time
#     获取信息 | getting_information
#     计算操作 | instruction_operation
#     执行操作 | execute_action
import abc


class BaseAction(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.finished = False
        self.next = None
        self.timer = 0
        pass

    @abc.abstractmethod
    def update(self, *args, **kwds):
        pass

    @abc.abstractmethod
    def waiting_time(self):
        pass

    @abc.abstractmethod
    def getting_information(self):
        pass

    @abc.abstractmethod
    def instruction_operation(self):
        pass

    @abc.abstractmethod
    def execute_action(self):
        pass

    ...
