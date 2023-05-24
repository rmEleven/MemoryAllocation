from Block import *


class Memory:
    def __init__(self, num_blocks, block_capacity):
        self.num_blocks = num_blocks  # 块个数
        self.page_fault_count = 0     # 缺页次数
        self.blocks = [Block(block_capacity) for _ in range(num_blocks)]  # 模拟块的Block对象
        self.max_load_order = 0   # 块被放入内存的次序的最大值
        self.max_usage_order = 0  # 块被使用的次序的最大值

    def find_instruction(self, instruction):
        for index, block in enumerate(self.blocks):
            if block.has_instruction(instruction):
                block.usage_order = self.max_usage_order + 1
                self.max_usage_order += 1
                return index, block.find_instruction_index(instruction)

        self.page_fault_count += 1
        return None, None
    
    def find_empty_block(self):
        for index, block in enumerate(self.blocks):
            if not block.instructions:
                return index

        return None
    
    def load_page(self, page):
        empty_block_index = self.find_empty_block()
        self.blocks[empty_block_index].instructions, page = page, self.blocks[empty_block_index].instructions

        self.blocks[empty_block_index].load_order = self.max_load_order + 1
        self.blocks[empty_block_index].usage_order = self.max_usage_order + 1

        self.max_load_order += 1
        self.max_usage_order += 1

    def choose_accord_to_FIFO(self):
        # 根据先进先出(FIFO)算法选择最先放入的块
        oldest_block_index = 0
        oldest_load_order = self.blocks[0].load_order

        for index, block in enumerate(self.blocks):
            if block.load_order < oldest_load_order:
                oldest_block_index = index
                oldest_load_order = block.load_order

        return oldest_block_index
    
    def choose_accord_to_LRU(self):
        # 根据最近最少使用(LRU)算法选择最早被使用的块
        least_used_block_index = 0
        least_usage_order = self.blocks[0].usage_order

        for index, block in enumerate(self.blocks):
            if block.usage_order < least_usage_order:
                least_used_block_index = index
                least_usage_order = block.usage_order

        return least_used_block_index

    def swap_accord_to_FIFO(self, page):
        selected_block_index = self.choose_accord_to_FIFO()
        self.blocks[selected_block_index].instructions, page = page, self.blocks[selected_block_index].instructions

        self.blocks[selected_block_index].load_order = self.max_load_order + 1
        self.blocks[selected_block_index].usage_order = self.max_usage_order + 1

        self.max_load_order += 1
        self.max_usage_order += 1

    def swap_accord_to_LRU(self, page):
        selected_block_index = self.choose_accord_to_LRU()
        self.blocks[selected_block_index].instructions, page = page, self.blocks[selected_block_index].instructions

        self.blocks[selected_block_index].load_order = self.max_load_order + 1
        self.blocks[selected_block_index].usage_order = self.max_usage_order + 1

        self.max_load_order += 1
        self.max_usage_order += 1
