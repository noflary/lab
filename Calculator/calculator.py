import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_fourth.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_fourth.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_fourth.addWidget(self.b_3)
        
        self.b_4 = QPushButton("4", self)
        self.hbox_third.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_third.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_third.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_second.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_second.addWidget(self.b_9)

        self.b_delete = QPushButton("del", self)
        self.hbox_first.addWidget(self.b_delete)


        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)
        
        self.b_point = QPushButton(",", self)
        self.hbox_result.addWidget(self.b_point)

        self.b_plus = QPushButton("+", self)
        self.hbox_third.addWidget(self.b_plus)

        self.b_multiply = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiply)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_substract = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_substract)

        self.b_del = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_del)


        self.b_substract.clicked.connect(lambda: self._operation("-"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_delete.clicked.connect(lambda: self._operation_delete())
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_result.clicked.connect(self._result)
        


        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_point.clicked.connect(lambda: self._button("."))


    def _operation_delete(self):
        text = self.input.text()
        self.input.setText(text[:-1])
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
    def _operation(self, op):
        if self.input.text() != '':
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
        elif (self.input.text() == '') or (self.input.text().isalpha):
            self.input.setText(str("Введите число"))
    def _result(self):
        if self.input.text() != '':
            self.num_2 = float(self.input.text())
            if self.num_2 == 0 and self.op == '/':
                self.input.setText(str('Операция не определена'))
            else:
                if self.op == "+":
                    self.input.setText(str(self.num_1 + self.num_2))
                if self.op == "-":
                    self.input.setText(str(self.num_1 - self.num_2))
                if self.op == "*":
                    self.input.setText(str(self.num_1 * self.num_2)) 
                if self.op == "/":
                    self.input.setText(str(self.num_1 / self.num_2))
        elif (self.input.text() == '') or (self.input.text().isalpha):
            self.input.setText(str("Не удаётся обработать"))
app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())