'''
Built on 3/6/2021
DEV:APJ '''

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import Fuzzy_Engine as FE

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 179)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 181))
        self.label.setStyleSheet("border-image: url(Design/vital.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 110, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 140, 191, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 70, 161, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(360, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 70, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton.clicked.connect(self.Get_LiveReadings)     
        self.pushButton_2.clicked.connect(self.Get_Fuzzy)   

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Smart Anesthesia Machine"))
        self.label_2.setText(_translate("Dialog", "Heart Rate:"))
        self.label_3.setText(_translate("Dialog", "OxyS. Rate:"))
        self.pushButton.setText(_translate("Dialog", "Get Live Readings"))
        self.pushButton_2.setText(_translate("Dialog", "Give Anasthesia"))
        self.label_4.setText(_translate("Dialog", "Anes. Rate:"))

#code
    def Get_LiveReadings(self):
        HeartRate=random.randint(60,100)
        OxyS=random.randint(80,100)
        self.lineEdit.setText(str(HeartRate))
        self.lineEdit_2.setText(str(OxyS))

    def Get_Fuzzy(self):
        HeartRate=int(self.lineEdit.text())
        RespirationRate=int(self.lineEdit_2.text())
        Speed=FE.FuzzyEngine_Topic(HeartRate,RespirationRate)
        self.lineEdit_3.setText(str(Speed['Pump_Speed']))
        print(Speed)
        
        

    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
