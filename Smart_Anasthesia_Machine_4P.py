

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import Fuzzy_Engine_2 as FE
import serial

try:
    ser = serial.Serial("COM6", '9600')#Give your arduino common ports here
    print('[ CONNECTED to HARDWARE ]')
except:
    print('[ HARDWARE not CONNECTED ]')


class CRGS(object):
    def crgs(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 231)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 231))
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
        self.pushButton.setGeometry(QtCore.QRect(290, 160, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 190, 191, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 130, 161, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(360, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 70, 91, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 70, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(290, 100, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 100, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton.clicked.connect(self.Get_LiveReadings)     
        self.pushButton_2.clicked.connect(self.Get_Fuzzy)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Smart Anesthesia Machine"))
        self.label_2.setText(_translate("Dialog", "Heart Rate:"))
        self.label_3.setText(_translate("Dialog", "Resp. Rate:"))
        self.pushButton.setText(_translate("Dialog", "Get Live Readings"))
        self.pushButton_2.setText(_translate("Dialog", "Give Anasthesia"))
        self.label_4.setText(_translate("Dialog", "Anes. Rate:"))
        self.label_5.setText(_translate("Dialog", "BIS. Rate:"))
        self.label_6.setText(_translate("Dialog", "Tem. Rate:"))

    def Get_LiveReadings(self):
        HeartRate=random.randint(60,100)
        OxyS=random.randint(80,100)
        BIS=random.randint(40,60)
        Temp=random.randint(36,39)
        self.lineEdit.setText(str(HeartRate))
        self.lineEdit_2.setText(str(OxyS))
        self.lineEdit_4.setText(str(BIS))
        self.lineEdit_5.setText(str(Temp))

    def Get_Fuzzy(self):
        HeartRate=int(self.lineEdit.text())
        OxyS=int(self.lineEdit_2.text())
        BIS=int(self.lineEdit_4.text())
        TEMP=int(self.lineEdit_5.text())
        #print(HeartRate,OxyS,BIS,TEMP)
        Speed=FE.FuzzyEngine_Topic(HeartRate,OxyS,BIS,TEMP)
        self.lineEdit_3.setText(str(Speed['Pump_Speed']))
        try:
            ser.write(str.encode(str(self.lineEdit_3.text())))
        except:
            print('[ Cannot Connect to the Hardware ]')
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CRGS()
    ui.crgs(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
