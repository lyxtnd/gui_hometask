import sys
from PySide6 import QtCore, QtGui, QtWidgets


DISPLAY_FONT_FAMILY = "Segoe UI"
BUTTON_FONT_FAMILY = "Segoe UI"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("QMainWindow { background-color: rgb(211, 150, 140); }")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.resul = QtWidgets.QLabel(self.centralwidget)
        self.resul.setGeometry(QtCore.QRect(11, 8, 378, 100))

        display_font = QtGui.QFont(DISPLAY_FONT_FAMILY, 36)
        display_font.setBold(False)
        display_font.setItalic(False)
        self.resul.setFont(display_font)
        self.resul.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # Отступ справа, чтобы текст не прилипал к краю и не съезжал при масштабировании
        self.resul.setContentsMargins(0, 0, 12, 0)
        self.resul.setWordWrap(False)
        self.resul.setStyleSheet(
            "QLabel {\n"
            "    background-color: rgb(247, 244, 213);\n"
            "    color: rgb(16, 86, 102);\n"
            "    border-radius: 6px;\n"
            "}"
        )
        self.resul.setObjectName("resul")

        button_font = QtGui.QFont(BUTTON_FONT_FAMILY, 22)
        button_font.setBold(False)
        button_font.setItalic(False)

        # Цвета для каждой кнопки: (геометрия, объект, фон, текст, фон_при_нажатии, текст_при_нажатии)
        buttons_spec = [
            (QtCore.QRect(11, 422, 90, 70), "btn_punct", "rgb(247, 244, 213)", "rgb(16, 86, 102)", "rgb(225, 220, 180)", "rgb(10, 60, 72)"),
            (QtCore.QRect(107, 422, 90, 70), "btn_0", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(203, 422, 90, 70), "btn_eqv", "rgb(247, 244, 213)", "rgb(16, 86, 102)", "rgb(225, 220, 180)", "rgb(10, 60, 72)"),
            (QtCore.QRect(299, 422, 90, 70), "btn_plus", "rgb(131, 153, 88)", "rgb(16, 86, 102)", "rgb(105, 125, 68)", "rgb(247, 244, 213)"),
            (QtCore.QRect(299, 346, 90, 70), "btn_minus", "rgb(131, 153, 88)", "rgb(16, 86, 102)", "rgb(105, 125, 68)", "rgb(247, 244, 213)"),
            (QtCore.QRect(11, 270, 90, 70), "btn_4", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(203, 346, 90, 70), "btn_3", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(107, 346, 90, 70), "btn_2", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(11, 346, 90, 70), "btn_1", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(299, 270, 90, 70), "btn_mul", "rgb(131, 153, 88)", "rgb(16, 86, 102)", "rgb(105, 125, 68)", "rgb(247, 244, 213)"),
            (QtCore.QRect(203, 270, 90, 70), "btn_6", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(107, 270, 90, 70), "btn_5", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(107, 194, 90, 70), "btn_8", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(203, 194, 90, 70), "btn_9", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(299, 194, 90, 70), "btn_div", "rgb(131, 153, 88)", "rgb(16, 86, 102)", "rgb(105, 125, 68)", "rgb(247, 244, 213)"),
            (QtCore.QRect(11, 194, 90, 70), "btn_7", "rgb(247, 244, 213)", "rgb(131, 153, 88)", "rgb(225, 220, 180)", "rgb(95, 115, 60)"),
            (QtCore.QRect(203, 118, 90, 70), "btn_sqrt", "rgb(16, 86, 102)", "rgb(131, 153, 88)", "rgb(10, 62, 74)", "rgb(170, 195, 120)"),
            (QtCore.QRect(107, 118, 90, 70), "btn_del", "rgb(16, 86, 102)", "rgb(131, 153, 88)", "rgb(10, 62, 74)", "rgb(170, 195, 120)"),
            (QtCore.QRect(11, 118, 90, 70), "btn_clr", "rgb(16, 86, 102)", "rgb(247, 244, 213)", "rgb(10, 62, 74)", "rgb(255, 255, 255)"),
            (QtCore.QRect(299, 118, 90, 70), "btn_power", "rgb(16, 86, 102)", "rgb(131, 153, 88)", "rgb(10, 62, 74)", "rgb(170, 195, 120)"),
        ]

        for rect, obj_name, bg, fg, pressed_bg, pressed_fg in buttons_spec:
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setGeometry(rect)
            btn.setFont(button_font)
            btn.setObjectName(obj_name)
            btn.setStyleSheet(
                f"QPushButton {{\n"
                f"    background-color: {bg};\n"
                f"    color: {fg};\n"
                f"    border-radius: 6px;\n"
                f"}}\n"
                f"QPushButton:pressed {{\n"
                f"    background-color: {pressed_bg};\n"
                f"    color: {pressed_fg};\n"
                f"}}"
            )
            setattr(self, obj_name, btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.data = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.resul.setText(_translate("MainWindow", "0"))
        self.btn_punct.setText(_translate("MainWindow", "."))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_eqv.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_mul.setText(_translate("MainWindow", "×"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_div.setText(_translate("MainWindow", "÷"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_sqrt.setText(_translate("MainWindow", "√"))
        self.btn_del.setText(_translate("MainWindow", "Del"))
        self.btn_clr.setText(_translate("MainWindow", "Clr"))
        self.btn_power.setText(_translate("MainWindow", "xʸ"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_div.clicked.connect(lambda: self.write_number("/"))
        self.btn_mul.clicked.connect(lambda: self.write_number("*"))
        self.btn_sqrt.clicked.connect(lambda: self.write_number("**(1/2)"))
        self.btn_power.clicked.connect(lambda: self.write_number("**"))
        self.btn_del.clicked.connect(lambda: self.write_number(self.btn_del.text()))
        self.btn_clr.clicked.connect(lambda: self.write_number(self.btn_clr.text()))
        self.btn_punct.clicked.connect(lambda: self.write_number(self.btn_punct.text()))

        self.btn_eqv.clicked.connect(self.results)

    def update_display(self, num):
        if not self.data:
            self.data = num
        else:
            self.data += num

        self.show_display(self.data)

    def show_display(self, text):
        display_text = text.replace("**", "^")
        display_text = display_text.replace("*", "×")
        display_text = display_text.replace("/", "÷")

        font = QtGui.QFont(DISPLAY_FONT_FAMILY)
        font.setItalic(False)
        font.setBold(False)

        # Учитываем правый отступ (contentsRect уже вычитает contentsMargins)
        available_width = max(1, self.resul.contentsRect().width())
        max_size = 36
        min_size = 10

        for size in range(max_size, min_size - 1, -1):
            font.setPointSize(size)
            metrics = QtGui.QFontMetrics(font)
            if metrics.horizontalAdvance(display_text) <= available_width:
                break

        self.resul.setFont(font)
        self.resul.setText(display_text)

    def write_number(self, num):
        if num == "Clr":
            self.data = ""
            self.show_display("0")
            return

        if num == "Del":
            self.data = self.data[:-1]
            self.show_display(self.data if self.data else "0")
            return

        self.update_display(num)

    def results(self):
        if not self.data:
            return

        try:
            result = eval(self.data, {"__builtins__": {}}, {})

            if isinstance(result, complex):
                self.show_display("Invalid result")
                self.data = ""
                return

            if abs(result) > 10**12:
                result_text = format(result, ".3e")
            else:
                result_text = str(result)

            self.data = result_text
            self.show_display(result_text)

        except ZeroDivisionError:
            self.data = ""
            self.show_display("Not defined")
        except (SyntaxError, TypeError, NameError, ValueError, OverflowError):
            self.data = ""
            self.show_display("Invalid syntax")


class CalculatorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setFocusPolicy(QtCore.Qt.NoFocus)

    def keyPressEvent(self, event):
        key = event.key()
        text = event.text()

        if text and text in "0123456789+-*/().":
            self.ui.write_number(text)

        elif text == ",":
            self.ui.write_number(".")

        elif key in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter) or text == "=":
            self.ui.results()

        elif key == QtCore.Qt.Key_Backspace:
            self.ui.write_number("Del")

        elif key == QtCore.Qt.Key_Escape:
            self.ui.write_number("Clr")

        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = CalculatorWindow()
    MainWindow.show()
    MainWindow.setFocus()

    sys.exit(app.exec())