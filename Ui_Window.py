# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\program\MemoryAllocation\Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(743, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_view = QtWidgets.QFrame(self.centralwidget)
        self.frame_view.setStyleSheet("QFrame {\n"
"    background-color: rgb(211, 211, 211)\n"
"}")
        self.frame_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_view.setObjectName("frame_view")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_view)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.memory_tableWidget = QtWidgets.QTableWidget(self.frame_view)
        self.memory_tableWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.memory_tableWidget.setObjectName("memory_tableWidget")
        self.memory_tableWidget.setColumnCount(2)
        self.memory_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.memory_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.memory_tableWidget.setHorizontalHeaderItem(1, item)
        self.memory_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.memory_tableWidget.horizontalHeader().resizeSection(0, 100)
        self.memory_tableWidget.horizontalHeader().resizeSection(1, 400)
        self.memory_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.memory_tableWidget)
        self.instrcution_count_label = QtWidgets.QLabel(self.frame_view)
        self.instrcution_count_label.setObjectName("instrcution_count_label")
        self.verticalLayout_2.addWidget(self.instrcution_count_label)
        self.instruction_num_label = QtWidgets.QLabel(self.frame_view)
        self.instruction_num_label.setObjectName("instruction_num_label")
        self.verticalLayout_2.addWidget(self.instruction_num_label)
        self.instruction_page_num_label = QtWidgets.QLabel(self.frame_view)
        self.instruction_page_num_label.setObjectName("instruction_page_num_label")
        self.verticalLayout_2.addWidget(self.instruction_page_num_label)
        self.instruction_page_offset_label = QtWidgets.QLabel(self.frame_view)
        self.instruction_page_offset_label.setObjectName("instruction_page_offset_label")
        self.verticalLayout_2.addWidget(self.instruction_page_offset_label)
        self.gridLayout.addWidget(self.frame_view, 0, 1, 1, 1)
        self.frame_control = QtWidgets.QFrame(self.centralwidget)
        self.frame_control.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_control.setStyleSheet("QFrame {\n"
"    background-color: rgb(211, 211, 211)\n"
"}")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instructions_label = QtWidgets.QLabel(self.frame_control)
        self.instructions_label.setObjectName("instructions_label")
        self.verticalLayout.addWidget(self.instructions_label)
        self.instructions_lineEdit = QtWidgets.QLineEdit(self.frame_control)
        self.instructions_lineEdit.setObjectName("instructions_lineEdit")
        self.verticalLayout.addWidget(self.instructions_lineEdit)
        self.page_capacity_label = QtWidgets.QLabel(self.frame_control)
        self.page_capacity_label.setObjectName("page_capacity_label")
        self.verticalLayout.addWidget(self.page_capacity_label)
        self.page_capacity_lineEdit = QtWidgets.QLineEdit(self.frame_control)
        self.page_capacity_lineEdit.setObjectName("page_capacity_lineEdit")
        self.verticalLayout.addWidget(self.page_capacity_lineEdit)
        self.total_blocks_label = QtWidgets.QLabel(self.frame_control)
        self.total_blocks_label.setObjectName("total_blocks_label")
        self.verticalLayout.addWidget(self.total_blocks_label)
        self.total_blocks_lineEdit = QtWidgets.QLineEdit(self.frame_control)
        self.total_blocks_lineEdit.setObjectName("total_blocks_lineEdit")
        self.verticalLayout.addWidget(self.total_blocks_lineEdit)
        self.select_algorithm_label = QtWidgets.QLabel(self.frame_control)
        self.select_algorithm_label.setObjectName("select_algorithm_label")
        self.verticalLayout.addWidget(self.select_algorithm_label)
        self.FIFO_pushButton = QtWidgets.QPushButton(self.frame_control)
        self.FIFO_pushButton.setObjectName("FIFO_pushButton")
        self.verticalLayout.addWidget(self.FIFO_pushButton)
        self.LRU_pushButton = QtWidgets.QPushButton(self.frame_control)
        self.LRU_pushButton.setObjectName("LRU_pushButton")
        self.verticalLayout.addWidget(self.LRU_pushButton)
        self.selected_algorithm_label = QtWidgets.QLabel(self.frame_control)
        self.selected_algorithm_label.setObjectName("selected_algorithm_label")
        self.verticalLayout.addWidget(self.selected_algorithm_label)
        self.pushButton = QtWidgets.QPushButton(self.frame_control)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.page_fault_count_label = QtWidgets.QLabel(self.frame_control)
        self.page_fault_count_label.setObjectName("page_fault_count_label")
        self.verticalLayout.addWidget(self.page_fault_count_label)
        self.page_fault_rate_label = QtWidgets.QLabel(self.frame_control)
        self.page_fault_rate_label.setObjectName("page_fault_rate_label")
        self.verticalLayout.addWidget(self.page_fault_rate_label)
        self.gridLayout.addWidget(self.frame_control, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.memory_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "内存块编号"))
        item = self.memory_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "内存块内容"))
        self.instrcution_count_label.setText(_translate("MainWindow", "执行第0条指令"))
        self.instruction_num_label.setText(_translate("MainWindow", "当前指令编号："))
        self.instruction_page_num_label.setText(_translate("MainWindow", "当前指令页号："))
        self.instruction_page_offset_label.setText(_translate("MainWindow", "当前指令页内偏移："))
        self.instructions_label.setText(_translate("MainWindow", "指令总数："))
        self.page_capacity_label.setText(_translate("MainWindow", "页大小："))
        self.total_blocks_label.setText(_translate("MainWindow", "内存块数："))
        self.select_algorithm_label.setText(_translate("MainWindow", "算法选择："))
        self.FIFO_pushButton.setText(_translate("MainWindow", "FIFO"))
        self.LRU_pushButton.setText(_translate("MainWindow", "LRU"))
        self.selected_algorithm_label.setText(_translate("MainWindow", "当前算法："))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.page_fault_count_label.setText(_translate("MainWindow", "缺页数："))
        self.page_fault_rate_label.setText(_translate("MainWindow", "缺页率："))
