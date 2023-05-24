# MemoryAllocation

## 项目简介

模拟内存管理的请求调页存储管理方式

假设每个页面可存放10条指令，分配给一个作业的内存块为4。模拟一个作业的执行过程，该作业有320条指令，即它的地址空间为32页，目前所有页还没有调入内存。

在模拟过程中，如果所访问指令在内存中，则显示其物理地址，并转到下一条指令；如果没有在内存中，则发生缺页，此时需要记录缺页次数，并将其调入内存。如果4个内存块中已装入作业，则需进行页面置换。

所有320条指令执行完成后，计算并显示作业执行过程中发生的缺页率。

置换算法可以选用FIFO或者LRU算法

作业中指令访问次序可以按照下面原则形成：  

50%的指令是顺序执行的，25%是均匀分布在前地址部分，25％是均匀分布在后地址部分。

## 项目结构

项目包含以下文件：

```
├── Task.py       # 模拟指令任务
├── Block.py      # 模拟内存块
├── Memory.py     # 模拟内存
├── Ui_Window.py  # 图形化用户界面设计
├── main.py       # 程序运行入口
├── .gitignore        # git忽略配置
├── requirements.txt  # 项目依赖项
├── README.md         # 项目说明文档
├── report.md         # 项目设计文档
└── images            # 文档需要的图片
    ├── ...
    ├── ...
    └── ...
```

## 如何运行

### 1. 安装 python

该项目使用 `python3.10.9` 请至少确保环境中安装了 `python3`

使用指令：

```shell
python --version
```

来检查环境中 `python` 的版本


### 2. 安装依赖项

使用指令：

```shell
pip install -r requirements.txt
```

来安装项目运行需要的依赖项

### 3. 运行程序

使用指令：

```shell
python .\main.py
```

来运行项目

界面整体：

<img src="images/overview.png">

选择FIFO算法：

<img src="images/selectFIFO.png">

FIFO算法结果：

<img src="images/resultFIFO.png">

选择LRU算法：

<img src="images/selectLRU.png">

LRU算法结果：

<img src="images/resultLRU.png">

### 4. 其他说明

默认每秒执行5条指令

可以在 `main.py` 文件的第 64 ~ 65 行自行设置

```python
QApplication.processEvents()  # 处理待处理的事件
time.sleep(0.2)               # 暂停0.2秒
```
