from Task import *
from Memory import *
from Ui_Window import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.TOTAL_INSTRUCTIONS = None
        self.PAGE_CAPACITY = None
        self.TOTAL_BLOCKS = None
        self.algorithm = None

        self.FIFO_pushButton.clicked.connect(self.choose_FIFO)
        self.LRU_pushButton.clicked.connect(self.choose_LRU)
        self.pushButton.clicked.connect(self.run)

    def choose_FIFO(self):
        # 选择FIFO算法
        self.algorithm = "FIFO"
        self.selected_algorithm_label.setText("当前算法：FIFO")
    
    def choose_LRU(self):
        # 选择LRU算法
        self.algorithm = "LRU"
        self.selected_algorithm_label.setText("当前算法：LRU")

    def show_memory(self, memory):
        self.memory_tableWidget.setRowCount(0)
        for index, block in enumerate(memory.blocks):
            rowPosition = self.memory_tableWidget.rowCount()
            self.memory_tableWidget.insertRow(rowPosition)
            self.memory_tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(f"{index}"))
            self.memory_tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(f"{block.instructions}"))

    def run(self):
        # 获取输入框的值
        self.TOTAL_INSTRUCTIONS = int(self.instructions_lineEdit.text())
        self.PAGE_CAPACITY = int(self.page_capacity_lineEdit.text())
        self.TOTAL_BLOCKS = int(self.total_blocks_lineEdit.text())

        if self.TOTAL_INSTRUCTIONS == None or self.PAGE_CAPACITY == None or self.TOTAL_BLOCKS == None or self.algorithm == None:
            return None
        
        myTask = Task(self.TOTAL_INSTRUCTIONS)
        myMemory = Memory(self.TOTAL_BLOCKS, self.PAGE_CAPACITY)

        temp = list(range(self.TOTAL_INSTRUCTIONS))
        pages = [temp[i : i + 10] for i in range(0, len(temp), self.PAGE_CAPACITY)]

        while myTask.is_task_complete() == False:
            # 取指令
            instruction = myTask.get_instruction()
            self.instrcution_count_label.setText(f"执行第{myTask.executed_instructions}条指令")
            self.instruction_num_label.setText(f"当前指令编号：{instruction}")

            # 在内存中寻找指令
            page_index, page_offset = myMemory.find_instruction(instruction)

            # 指令不在内存中
            if page_index == None:
                # 找目标页
                for i, p in enumerate(pages):
                    if instruction in p:
                        page = p
                        id = i
                        break
                self.instruction_page_num_label.setText(f"当前指令页号：{id}")
                self.instruction_page_offset_label.setText(f"当前指令页内偏移：{page.index(instruction)}")

                if myMemory.find_empty_block() == None:
                    # 没有空的块：调页
                    if self.algorithm == "FIFO":
                        myMemory.swap_accord_to_FIFO(page)
                    elif self.algorithm == "LRU":
                        myMemory.swap_accord_to_LRU(page)
                    self.show_memory(myMemory)
                else:
                    # 有空的块：加载
                    myMemory.load_page(page)
                    self.show_memory(myMemory)
            # 指令在内存中
            else:
                self.instruction_page_num_label.setText(f"当前指令内存块号：{page_index}")
                self.instruction_page_offset_label.setText(f"当前指令内存块内偏移：{page_offset}")
            
            self.page_fault_count_label.setText(f"缺页数：{myMemory.page_fault_count}")
        
        self.page_fault_rate_label.setText(f"缺页率：{myMemory.page_fault_count / self.TOTAL_INSTRUCTIONS: .2%}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())