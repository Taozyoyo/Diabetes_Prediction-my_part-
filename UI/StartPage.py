from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class StartPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Diabetes Prediction Tool")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Start Page")
        self.setFixedSize(400, 350)

        # 设置背景颜色为淡蓝色
        self.setStyleSheet("background-color: #E6F3FF;")

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # 标题
        title_label = QLabel("Diabetes Prediction Tool")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Segoe UI", 16, QFont.Bold))  # 缩小字体大小
        title_label.setStyleSheet("color: #2C3E50; padding: 10px;")  # 设置内边距
        main_layout.addWidget(title_label)



        # 按钮 1
        btn1 = QPushButton("1")
        btn1.setCursor(Qt.PointingHandCursor)
        btn1.setMinimumHeight(60)  # 设置按钮高度
        btn1.setStyleSheet("""
                    QPushButton {
                        background-color: #3498DB;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        font-size: 16pt;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #2980B9;
                    }
                    QPushButton:pressed {
                        background-color: #1B4F72;
                    }
                """)
        btn1.clicked.connect(self.go_to_main_page)
        main_layout.addWidget(btn1)

        # 按钮 2
        btn2 = QPushButton("2")
        btn2.setCursor(Qt.PointingHandCursor)
        btn2.setMinimumHeight(60)  # 设置按钮高度
        btn2.setStyleSheet("""
                    QPushButton {
                        background-color: #3498DB;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        font-size: 16pt;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #2980B9;
                    }
                    QPushButton:pressed {
                        background-color: #1B4F72;
                    }
                """)
        btn2.clicked.connect(self.go_to_main2_page)
        main_layout.addWidget(btn2)

        # 按钮 3
        btn3 = QPushButton("3")
        btn3.setCursor(Qt.PointingHandCursor)
        btn3.setMinimumHeight(60)  # 设置按钮高度
        btn3.setStyleSheet("""
                    QPushButton {
                        background-color: #3498DB;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        font-size: 16pt;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #2980B9;
                    }
                    QPushButton:pressed {
                        background-color: #1B4F72;
                    }
                """)
        btn3.clicked.connect(self.go_to_main3_page)
        main_layout.addWidget(btn3)

        # 添加一个占位符，将标题推到顶部
        main_layout.addStretch(1)

        # 设置主布局
        self.setLayout(main_layout)



    def go_to_main_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(1)

    def go_to_main2_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(2)

    def go_to_main3_page(self):
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(3)