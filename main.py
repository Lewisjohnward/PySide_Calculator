from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType

import sys
import math
import re

Form, Base = loadUiType("./ui/calculator.ui")

class Calculator(Base, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.number = ["", ""]
        self.number_selector = 0
        self.operator = ""
        
        for n in range(1, 10):
            getattr(self, "btn_%s" % n).pressed.connect(lambda v=n: self.handle_keypress(v))

        self.btn_0.clicked.connect(self.handle_zero)
        self.btn_00.clicked.connect(self.handle_dzero)
        self.btn_ac.clicked.connect(self.clear_all)
        self.btn_c.clicked.connect(self.clear_current_num)
        self.btn_dot.clicked.connect(self.insert_dot)

        self.btn_plus.clicked.connect(self.handle_plus)
        self.btn_multi.clicked.connect(self.handle_multi)
        self.btn_equals.clicked.connect(self.handle_equals)
        self.btn_minus.clicked.connect(self.handle_minus)
        self.btn_div.clicked.connect(self.handle_divide)
        self.btn_root.clicked.connect(self.handle_root)


    def handle_keypress(self, num):
        self.number[self.number_selector] += str(num)
        self.display_line.setText(self.number[self.number_selector])

    def handle_equals(self):
        if len(self.number[0]) == 0:
            return
        if len(self.number[1]) == 0:
            return

        self.number_selector = 0
        print(self.number[0], self.number[1])

        number_1 = float(self.number[0])
        number_2 = float(self.number[1])
        print(number_1, number_2)
        print(self.operator)
         
        
        if self.operator == "+":
            result = number_1 + number_2
        elif self.operator == "x":
            result = number_1 * number_2
        elif self.operator == "/":
            result = number_1 / number_2
        elif self.operator == "-":
            result = number_1 - number_2

        if result.is_integer():
            result = int(result)
        self.number[self.number_selector] = str(result)


        self.update_display()
        self.number[1] = ""
        self.operator = ""
        self.number[0] = ""

    def insert_dot(self):
        number = self.number[self.number_selector]
        print(number)
        if re.findall("\.", number):
            return
        number += "."
        self.number[self.number_selector] = number
        self.update_display()

    def handle_root(self):
        if len(self.number[self.number_selector]) > 0:
            number = int(self.number[self.number_selector])
            number = math.sqrt(number)
            if number.is_integer():
                number = int(number)
            self.number[self.number_selector] = str(number)
            self.update_display()


    def handle_minus(self):
        if len(self.number[self.number_selector]) > 0 and len(self.operator) == 0:
            self.number_selector += 1
            self.operator = "-"
            self.update_display()

    def handle_divide(self):
        if len(self.number[self.number_selector]) > 0 and len(self.operator) == 0:
            self.number_selector += 1
            self.operator = "/"
            self.update_display()

    def handle_multi(self):
        if len(self.number[self.number_selector]) > 0 and len(self.operator) == 0:
            self.number_selector += 1
            self.operator = "x"
            self.update_display()

    def handle_plus(self):
        if len(self.number[self.number_selector]) > 0 and len(self.operator) == 0:
            self.number_selector += 1
            self.operator = "+"
            self.update_display()


    def handle_dzero(self):
        if len(self.number[self.number_selector]) > 0:
            self.number[self.number_selector] += "00"
            self.update_display()

    def handle_zero(self):
        if len(self.number[self.number_selector]) > 0:
            self.number[self.number_selector] += "0"
            self.update_display()
        

    def clear_current_num(self):
        self.number[self.number_selector] = ""
        self.update_display()

    def clear_all(self):
        for n in range(0, 1):
            self.number[n] = ""
        self.number_selector = 0
        self.update_display()
        
    def update_display(self):
        self.display_line.setText(self.number[self.number_selector])


def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
