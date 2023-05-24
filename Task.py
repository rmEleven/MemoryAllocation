import random


class Task:
    def __init__(self, total_instructions):
        self.total_instructions = total_instructions  # 指令总数
        self.executed_instructions = 0                # 已执行指令数
        self.last_instruction = None                  # 上一条指令编号

    def is_task_complete(self):
        return self.executed_instructions == self.total_instructions

    def get_instruction(self):
        if self.is_task_complete() == True:  # 任务是否结束
            return None

        instruction = None  # 本次需要执行的指令编号

        # 选取一个指令执行
        if self.executed_instructions % 6 == 0:
            # 在总地址部分均匀分布的情况
            instruction = random.randint(0, self.total_instructions - 1)
        elif self.executed_instructions % 6 == 2:
            # 在前地址部分均匀分布的情况
            instruction = random.randint(0, (self.last_instruction - 2) % self.total_instructions)
        elif self.executed_instructions % 6 == 4:
            # 在后地址部分均匀分布的情况
            instruction = random.randint((self.last_instruction + 1) % self.total_instructions, self.total_instructions - 1)
        else:
            # 顺序执行的情况
            instruction = (self.last_instruction + 1) % self.total_instructions

        self.executed_instructions += 1      # 已执行指令个数加1
        self.last_instruction = instruction  # 更新上一条指令编号

        return instruction  # 返回本次需要执行的指令编号
