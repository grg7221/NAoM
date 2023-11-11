from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from NAoM import NAoM, InvalidAlgorithmOperator, InvalidSubstringArgument, EmptyRulesList
import sys


class UI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('ui.ui', self)

        self.alph = []

        self.AddRuleButton = self.findChild(QPushButton, "AddRuleButton")
        self.DeleteRuleButton = self.findChild(QPushButton, "DeleteRuleButton")
        self.AlphButton = self.findChild(QPushButton, 'AlphButton')
        self.ProcessButton = self.findChild(QPushButton, 'ProcessButton')

        self.AddRuleButton.clicked.connect(self.addrule)
        self.AlphButton.clicked.connect(self.setalph)
        self.ProcessButton.clicked.connect(self.process)
        self.DeleteRuleButton.clicked.connect(self.deleterule)

        self.AlphInput = self.findChild(QLineEdit, 'AlphInput')
        self.InputString = self.findChild(QLineEdit, 'InputStringText')

        self.OutText = self.findChild(QTextBrowser, 'OutText')
        self.Rules = self.findChild(QTextBrowser, 'Rules')
        font = QFont()
        font.setPointSize(12)
        self.Rules.setFont(font)

        self.ShowProcess = self.findChild(QCheckBox, 'ShowProcessCheck')

        self.RuleInput = self.findChild(QLineEdit, 'RuleInputEdit')
        self.RuleOperator = self.findChild(QLineEdit, 'RuleOperatorEdit')
        self.RuleOutput = self.findChild(QLineEdit, 'RuleOutputEdit')

        self.error = QMessageBox()
        self.error.setIcon(QMessageBox.Critical)
        self.error.setWindowTitle("Ошибка")


    def setalph(self):
        self.alph = self.AlphInput.text().split(' ')
        if len(self.alph) != []:
            #self.AlphInput.setReadOnly(True)
            self.example = NAoM(self.alph)
            self.OutText.setText('Alphabet: ' + ', '.join(self.example.alph))
        else:
            self.error.setText("Ошибка алфавита")
            self.error.setInformativeText('Алфавит должен содержать хотя бы один символ!')
            self.error.exec_()

    def addrule(self):
        if len(self.alph) != 0:
            input = self.RuleInput.text()
            operator = self.RuleOperator.text()
            output = self.RuleOutput.text()
            try:
                self.example.add_rule(input, operator, output)
                self.update_rules()
            except InvalidSubstringArgument:
                self.error.setText("Ошибка правила")
                self.error.setInformativeText('Неверно указана подстрока! Она должна состояить из символов алфавита.')
                self.error.exec_()
            except InvalidAlgorithmOperator:
                self.error.setText("Ошибка правила")
                self.error.setInformativeText('Неверно указан оператор!')
                self.error.exec_()
        else:
            self.error.setText("Ошибка алфавита")
            self.error.setInformativeText('Сначала необходимо задать алфавит (каждый символ через пробел)!')
            self.error.exec_()

    def deleterule(self):
        self.example.delete_rule(-1)
        self.update_rules()

    def update_rules(self):
        self.Rules.clear()
        text = ''
        for rule in self.example.rules:
            text += rule.input + rule.operator + rule.output + '\n'
        self.Rules.setText('Rules:\n' + text)

    def process(self):
        if len(self.alph) != 0:
            try:
                result = "".join(self.example.processing(self.InputString.text(), show_process = self.ShowProcess.isChecked()))
                self.OutText.setText(result)
            except EmptyRulesList:
                self.error.setText("Ошибка списка правил")
                self.error.setInformativeText('Сначала необходимо задать правила!')
                self.error.exec_()
        else:
            self.error.setText("Ошибка алфавита")
            self.error.setInformativeText('Сначала необходимо задать алфавит (каждый символ через пробел)!')
            self.error.exec_()


app = QApplication([])
window = UI()
window.show()
app.exec_()