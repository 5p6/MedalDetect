import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QScrollArea

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scrollable Text Editor Example')

        # 创建一个 QTextEdit 控件
        self.text_edit = QTextEdit()

        # 创建一个 QScrollArea 控件
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # 设置为可调整大小
        scroll_area.setWidget(self.text_edit)  # 设置 QTextEdit 为 QScrollArea 的子组件

        # 创建一个 QWidget 作为主窗口的中央部件
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(scroll_area)  # 将 QScrollArea 添加到布局中

        # 将 central_widget 设置为主窗口的中央部件
        self.setCentralWidget(central_widget)

        # 写入大量文本，用于测试滚动条
        for i in range(100):
            self.text_edit.append(f'Line {i}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
