import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from StartPage import StartPage
from Data1Page import Data1App
from Data2Page import Data2App
from Data3Page import Data3App

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setFixedSize(400, 350)
        self.stacked_widget.setStyleSheet("background-color: #E6F3FF;")
        self.start_page = StartPage(self.stacked_widget)
        self.main_page = Data1App(self.stacked_widget)
        self.main2_page = Data2App(self.stacked_widget)
        self.main3_page = Data3App(self.stacked_widget)
        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.main2_page)
        self.stacked_widget.addWidget(self.main3_page)
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())