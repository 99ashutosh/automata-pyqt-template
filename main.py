import sys
from PyQt5 import QtWidgets, QtGui
from automata import automata
from DFA import *


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(1161,664)
        self.checkButton.clicked.connect(self.check_String)
        self.exitButton.clicked.connect(self.exit_prog)

    def check_String(self):
        string = self.textEdit.toPlainText()
        if(automata.check_string(string)):
            self.label_5.setText("Accepted")
            self.label_8.setText(string)
            self.label_5.setStyleSheet("color: green;")
            automata.gen_transition_png()
            self.label_13.setText(automata.get_last_transition())
            self.label_19.setPixmap(QtGui.QPixmap("transition_history.png"))
            automata.reset_states()

        else:
            self.label_5.setText("Not Accepted")
            self.label_8.setText(string)
            self.label_5.setStyleSheet("color: red;")
            automata.gen_transition_png()
            self.label_13.setText(automata.get_last_transition())
            self.label_19.setPixmap(QtGui.QPixmap("transition_history.png"))
            automata.reset_states()

    
    def exit_prog(self):
        sys.exit()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
