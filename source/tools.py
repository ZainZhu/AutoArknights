# 工具和脚本主控


import time


class Auto_Ark():
    def __init__(self, state_dict, state_state):
        self.state_dict = state_dict
        self.state = self.state_dict[state_state]
        self.obj = self.state

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
            self.obj = self.state
        self.state.update()


    def __call__(self):
        self.obj()
        # self.update()
        pass

    def waiting_time(self):
        self.obj.waiting_time()
        pass

    def getting_information(self):
        self.obj.getting_information()
        pass

    def instruction_operation(self):
        self.obj.getting_information()
        pass

    def execute_action(self):
        self.obj.getting_information()
        pass

    ...
