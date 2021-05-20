from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, QCoreApplication
import sys
from PyQt5.QtGui import QDoubleValidator

class App(QWidget):
    root = QVBoxLayout()
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.digits = QHBoxLayout()
        first = QVBoxLayout()
        second = QVBoxLayout()
        self.digits.addLayout(first)
        self.digits.addLayout(second)
        onlyDigit = QDoubleValidator()
        self.one = QLineEdit()
        self.one.setValidator(onlyDigit)
        first.addWidget(QLabel('Первое число'))
        first.addWidget(self.one)
        self.root.addLayout(self.digits)

        self.two = QLineEdit()
        self.two.setValidator(onlyDigit)
        second.addWidget(QLabel('Второе число'))
        second.addWidget(self.two)
        
        self.operations = QHBoxLayout()
        plus = QPushButton('+')
        plus.clicked.connect(self.plus)
        minus = QPushButton('-')
        minus.clicked.connect(self.minus)
        multiply = QPushButton('*')
        multiply.clicked.connect(self.multiply)
        divide = QPushButton('/')
        divide.clicked.connect(self.divide)
        mul = QPushButton('^')
        mul.clicked.connect(self.mul)
        
        self.operations.addWidget(plus)
        self.operations.addWidget(minus)
        self.operations.addWidget(multiply)
        self.operations.addWidget(divide)
        self.operations.addWidget(mul)
        self.root.addLayout(self.operations)

        self.root.addWidget(QLabel('Результат'))
        self.result = QLineEdit(readOnly=True)
        self.root.addWidget(self.result)

        self.setLayout(self.root)
        self.setWindowTitle('Калькулятор')
        self.resize(200, 100)
        self.show()
    def plus(self):
        try:
            a = float(self.one.text())
            b = float(self.two.text())
            self.result.setText(str(a+b))
        except:
            self.result.setText('введите числа')
    def minus(self):
        try:
            a = float(self.one.text())
            b = float(self.two.text())
            self.result.setText(str(a-b))
        except:
            self.result.setText('введите числа')
    def multiply(self):
        try:
            a = float(self.one.text())
            b = float(self.two.text())
            self.result.setText(str(a*b))
        except:
            self.result.setText('введите числа')
    def divide(self):
        try:
            a = float(self.one.text())
            b = float(self.two.text())
            if b == 0.0:
                self.result.setText('нельзя делить на ноль')
            else:
                self.result.setText(str(a/b))
        except:
            self.result.setText('введите числа')
    def mul(self):
        try:
            a = float(self.one.text())
            b = float(self.two.text())
            res = a
            for i in range(int(b)-1):
                res = res*a
            self.result.setText(str(res))
        except:
            self.result.setText('введите числа')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
