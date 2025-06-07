import sys
import joblib
import pandas as pd
import numpy as np
import warnings
from PyQt5.QtCore import Qt, QPropertyAnimation, QByteArray, QEasingCurve, QPoint, QRect, QSize, QTimer, pyqtProperty
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QColor, QIcon, QFont

class Data3App(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Diabetes Prediction Tool")
        # 设置可供选择的模型的路径
        self.models = {
            "Gradient Boosting" : ("Data3_Model/Gradient Boosting_model.pkl"),
            "Logistic Regression": ("Data3_Model/Logistic Regression_model.pkl"),
            "Random Forest": ("Data3_Model/Random Forest_model.pkl")
        }
        self.current_model = None
        self.scaler = joblib.load("data3_scaler.pkl")
        self.features = ["Hour", "Day", "Month", "Value"]
        self.init_ui()
        self.setup_styles()


    def init_ui(self):
        self.setWindowTitle("Diabetes Prediction Tool")
        self.setFixedSize(800, 800)
        #self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: #E6F3FF;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(15)

        #下拉列表
        self.model_combo = QComboBox()
        self.model_combo.addItems(self.models.keys())
        self.model_combo.installEventFilter(self)
        self.model_combo.currentTextChanged.connect(self.load_model)

        # 默认加载第一个模型
        if self.models:
            self.model_combo.setCurrentIndex(0)
            self.load_model(self.model_combo.currentText())

        main_layout.addWidget(QLabel("Select Model:"))
        main_layout.addWidget((self.model_combo))

        # 输入字段
        inputs = [
            ("Hour:", QLineEdit()),
            ("Day:", QLineEdit()),
            ("Month:", QLineEdit()),
            ("Value:", QLineEdit())
        ]

        self.input_fields = {label: field for label, field in inputs}

        for label, input_field in inputs:
            h_layout = QHBoxLayout()
            lbl = QLabel(label)
            lbl.setFixedWidth(180)
            h_layout.addWidget(lbl)
            input_field.setMinimumHeight(35)
            h_layout.addWidget(input_field)
            main_layout.addLayout(h_layout)

        # 预测按钮
        self.predict_btn = QPushButton("Predict Risk")
        self.predict_btn.setCursor(Qt.PointingHandCursor)
        self.predict_btn.clicked.connect(self.predict)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.predict_btn)

        # 结果显示
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setMinimumHeight(60)
        main_layout.addSpacing(15)
        main_layout.addWidget(self.result_label)

        # 返回按钮
        self.return_btn = QPushButton("Back")
        self.return_btn.setCursor(Qt.PointingHandCursor)
        self.return_btn.clicked.connect(self.go_to_start_page)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.return_btn)

        self.setLayout(main_layout)
        self.show()

    def load_model(self, model_name):
            try:
                model_file = self.models[model_name]
                # 忽略 XGBoost 的警告
               # warnings.filterwarnings("ignore", category=UserWarning)
                self.current_model = joblib.load(model_file)
                print(f"Model {model_name} loaded successfully!")
            except FileNotFoundError:
                self.show_error_message(f"Error: Model for {model_name} not found!")
            except Exception as e:
                self.show_error_message(f"Failed to load model: {str(e)}")

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #E6F3FF;
            }
            QLabel {
                color: #2C3E50;
                font-size: 12pt;
                font-weight: 500;
            }
            QLineEdit {
                background-color: white;
                border: 2px solid #3498DB;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 12pt;
                color: #34495E;
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-size: 12pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1B4F72;
            }
        """)
        self.result_label.setObjectName(("result_label"))

    def get_input_data(self):
        try:
            hour = float(self.input_fields["Hour:"].text())
            day = float(self.input_fields["Day:"].text())
            mon = float(self.input_fields["Month:"].text())
            val = float(self.input_fields["Value:"].text())
            return [hour, day, mon, val]
        except ValueError:
            #self.show_error_message("输入格式错误！请输入数字。")
            return None

    def predict(self):
        try:
            if self.current_model is None:
                self.show_error_message("Please select model！")
                return

            input_data = self.get_input_data()
            if input_data is None:
                self.show_error_message("Format Error")
                return

            input_df = pd.DataFrame([input_data], columns=self.features)
            input_scaled = self.scaler.transform(input_df)
            prediction = self.current_model.predict(input_scaled)[0]
            probability = self.current_model.predict_proba(input_scaled)[0][1]

            if prediction == 1:
                self.result_label.setText(f"High Risk（Probability：{probability:.2%}）")
                self.result_label.setStyleSheet("color: red;")
            else:
                self.result_label.setText(f"Low Risk（Probability：{probability:.2%}）")
                self.result_label.setStyleSheet("color: green;")
        except Exception as e:
            self.show_error_message(f"程序错误：{str(e)}")

    def show_error_message(self, message):
        """
        显示错误信息的弹窗
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)  # 设置图标为错误
        msg_box.setWindowTitle("Error")  # 设置标题
        msg_box.setText(message)  # 设置提示信息
        msg_box.setStandardButtons(QMessageBox.Ok)  # 添加“确定”按钮
        msg_box.exec_()  # 显示弹窗

    def go_to_start_page(self):
        """切换到开始界面"""
        self.stacked_widget.setFixedSize(400, 350)  # 调整窗口大小为 400x400
        self.stacked_widget.setCurrentIndex(0)