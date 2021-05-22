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
        self.calculate('plus', self.one.text(), self.two.text())
    def minus(self):
        self.calculate('minus', self.one.text(), self.two.text())
    def multiply(self):
        self.calculate('multiply', self.one.text(), self.two.text())
    def divide(self):
        self.calculate('divide', self.one.text(), self.two.text())
    def mul(self):
        self.calculate('mul', self.one.text(), self.two.text())
    def calculate(self, operation, a, b):
        try:
            a = float(a)
            b = float(b)
        except:
            self.result.setText('введите числа')
            return
        if operation == 'plus':
            self.result.setText(str(a+b))
        elif operation == 'minus':
            self.result.setText(str(a-b))
        elif operation == 'multiply':
            self.result.setText(str(a*b))
        elif operation == 'divide':
            self.result.setText(str(a/b))
        elif operation == 'mul':
            res = a
            for i in range(int(b)-1):
                res = res*a
            self.result.setText(str(res))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
