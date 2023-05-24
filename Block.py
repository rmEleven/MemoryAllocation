class Block:
    def __init__(self, capacity):
        self.capacity = capacity  # 块容量
        self.load_order = None    # 块被放入内存的次序
        self.usage_order = None   # 块被使用的次序
        self.instructions = []    # 存放的指令

    def has_instruction(self, instruction):
        return instruction in self.instructions

    def find_instruction_index(self, instruction):
        if self.has_instruction(instruction):
            return self.instructions.index(instruction)
        else:
            return None
