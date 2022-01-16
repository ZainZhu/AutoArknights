# 工具和脚本主控


class Auto_Ark():
    def __init__(self, state_dict, state_state):
        self.state_dict = state_dict
        self.state_state = self.state_dict[state_state]

        self.obj = self.state_state

    def __call__(self):
        self.obj()
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
