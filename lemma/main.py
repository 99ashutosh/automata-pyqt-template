import sys
from PyQt5 import QtWidgets, QtGui
from lemma import *
from plemma import *

f_states = 0

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.label_26.setHidden(True)
        self.label_17.setHidden(True)
        self.label_19.setHidden(True)
        self.label_20.setHidden(True)
        self.label_25.setHidden(True)
        self.label_27.setHidden(True)
        self.str_gb.setEnabled(False)
        self.test_button.clicked.connect(self.init_conditions)
        self.check_button.clicked.connect(self.test_string)
        self.select_str_button.clicked.connect(self.select_string)
        self.pump_str.clicked.connect(self.pump)
        self.x_slide.valueChanged.connect(self.updateValues);
        self.y_slide.valueChanged.connect(self.updateValues);
        self.z_slide.valueChanged.connect(self.updateValues);


    def init_conditions(self):
        global states
        states = self.lineEdit.text()
        if (states == ''):
            self.label_26.setHidden(False)
        elif (int(states) % 2 != 0):
            states = int(states) + 1
            dis_str = plemma.getString(states)
            self.label_9.setText(dis_str)
            self.x_slide.setMaximum(states)
            self.y_slide.setMaximum(states)
            self.z_slide.setMaximum(states)
            self.label_10.setText(str(states))
            self.str_gb.setEnabled(True)


        else:
            states = int(states)
            dis_str = plemma.getString(states)
            self.label_9.setText(dis_str)
            self.x_slide.setMaximum(states)
            self.y_slide.setMaximum(states)
            self.z_slide.setMaximum(states)
            self.label_10.setText(str(states))
            self.str_gb.setEnabled(True)

    def select_string(self):
        print("WIP")

    def test_string(self):
        i = int(self.i_edit.text())
        fin_str = plemma.getFinalString()
        self.f_str.setText(fin_str)

    def pump(self):
        print("WIP")

    def updateValues(self):
        x_val = self.x_slide.value()
        y_val = self.y_slide.value()
        z_val = self.z_slide.value()
        if (x_val + y_val> states):
            self.x_slide.setValue(x_val-1)
        if (x_val + y_val +z_val> states):
            self.x_slide.setValue(x_val-1)
            self.y_slide.setValue(y_val-1)
        data = plemma.splitStrings(x_val,y_val,z_val)
        print(data)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
