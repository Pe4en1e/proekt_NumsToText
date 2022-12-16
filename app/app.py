from PyQt6 import QtCore, QtGui, QtWidgets
import main

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(400, 600)
        Window.setMinimumSize(QtCore.QSize(400, 600))
        Window.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 401, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.background.setFont(font)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("/Users/alexanderdubrovin/Desktop/proekt/proekt_NumsToText/app/SPRK_default_preset_name_custom – 1.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.rub_input = QtWidgets.QLineEdit(self.centralwidget)
        self.rub_input.setGeometry(QtCore.QRect(36, 247, 328, 34))
        self.rub_input.setMinimumSize(QtCore.QSize(328, 34))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        self.rub_input.setFont(font)
        self.rub_input.setStyleSheet("background-image: url(/Users/alexanderdubrovin/Desktop/proekt/proekt_NumsToText/app/field.png);\n""color: #ffffff;\n""border: 0px;\n""background-color: #181717")
        self.rub_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rub_input.setPlaceholderText("")
        self.rub_input.setObjectName("rub_input")
        self.transfer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transfer_btn.setGeometry(QtCore.QRect(86, 351, 229, 35))
        self.transfer_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.transfer_btn.setStyleSheet("#transfer_btn{\n""background-image: url(/Users/alexanderdubrovin/Desktop/proekt/proekt_NumsToText/app/Button.png);\n""border: 0px\n""}\n""\n""#transfer_btn:hover {\n""background-image: url(/Users/alexanderdubrovin/Desktop/proekt/proekt_NumsToText/app/Button_hover.png);\n""border: 0px\n""}")
        self.transfer_btn.setText("")
        self.transfer_btn.setObjectName("transfer_btn")
        self.kopek_input = QtWidgets.QLineEdit(self.centralwidget)
        self.kopek_input.setGeometry(QtCore.QRect(36, 299, 328, 34))
        self.kopek_input.setMinimumSize(QtCore.QSize(328, 34))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        self.kopek_input.setFont(font)
        self.kopek_input.setStyleSheet("background-image: url(/Users/alexanderdubrovin/Desktop/proekt/proekt_NumsToText/app/field.png);\n""color: #ffffff;\n""border: 0px;\n""background-color: #181717")
        self.kopek_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.kopek_input.setPlaceholderText("")
        self.kopek_input.setObjectName("kopek_input")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(37, 404, 326, 178))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
<<<<<<< Updated upstream
        font.setPointSize(10)
=======
        font.setPointSize(12)
>>>>>>> Stashed changes
        self.result.setFont(font)
        self.result.setStyleSheet("color: #ffffff")
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result.setObjectName("result")
        Window.setCentralWidget(self.centralwidget)

<<<<<<< Updated upstream

        self.transfer_btn.clicked.connect(self.set_result)


=======
        self.transfer_btn.clicked.connect(self.set_result)

>>>>>>> Stashed changes
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "NumsToText"))


    def set_result(self):
        rubles = self.rub_input.text()
        kopek = self.kopek_input.text()
        output = main.zmn(rubles, kopek)
        self.result.setText(output)

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
