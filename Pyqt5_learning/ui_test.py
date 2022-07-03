# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Img_Processing_Wid(object):
    def setupUi(self, Img_Processing_Wid):
        Img_Processing_Wid.setObjectName("Img_Processing_Wid")
        Img_Processing_Wid.resize(1412, 952)
        Img_Processing_Wid.setWindowOpacity(1.0)
        self.B_FIle = QtWidgets.QPushButton(Img_Processing_Wid)
        self.B_FIle.setGeometry(QtCore.QRect(20, 30, 121, 51))
        self.B_FIle.setObjectName("B_FIle")
        self.image = QtWidgets.QLabel(Img_Processing_Wid)
        self.image.setGeometry(QtCore.QRect(310, 60, 400, 400))
        self.image.setText("")
        self.image.setObjectName("image")
        self.label1 = QtWidgets.QLabel(Img_Processing_Wid)
        self.label1.setGeometry(QtCore.QRect(400, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1.setAutoFillBackground(False)
        self.label1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Img_Processing_Wid)
        self.label2.setGeometry(QtCore.QRect(1000, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setAutoFillBackground(False)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.FFt = QtWidgets.QLabel(Img_Processing_Wid)
        self.FFt.setGeometry(QtCore.QRect(910, 60, 400, 400))
        self.FFt.setText("")
        self.FFt.setObjectName("FFt")
        self.IFFt = QtWidgets.QLabel(Img_Processing_Wid)
        self.IFFt.setGeometry(QtCore.QRect(300, 510, 400, 400))
        self.IFFt.setText("")
        self.IFFt.setObjectName("IFFt")
        self.label3 = QtWidgets.QLabel(Img_Processing_Wid)
        self.label3.setGeometry(QtCore.QRect(390, 470, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label3.setAutoFillBackground(False)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.B_FFT = QtWidgets.QPushButton(Img_Processing_Wid)
        self.B_FFT.setGeometry(QtCore.QRect(20, 180, 121, 51))
        self.B_FFT.setObjectName("B_FFT")
        self.B_IFFT = QtWidgets.QPushButton(Img_Processing_Wid)
        self.B_IFFT.setGeometry(QtCore.QRect(20, 320, 121, 51))
        self.B_IFFT.setObjectName("B_IFFT")

        self.retranslateUi(Img_Processing_Wid)
        QtCore.QMetaObject.connectSlotsByName(Img_Processing_Wid)

    def retranslateUi(self, Img_Processing_Wid):
        _translate = QtCore.QCoreApplication.translate
        Img_Processing_Wid.setWindowTitle(_translate("Img_Processing_Wid", "Img_Processing"))
        self.B_FIle.setText(_translate("Img_Processing_Wid", "openfile"))
        self.label1.setText(_translate("Img_Processing_Wid", "Original_Img"))
        self.label2.setText(_translate("Img_Processing_Wid", "FFT"))
        self.label3.setText(_translate("Img_Processing_Wid", "IFFT"))
        self.B_FFT.setText(_translate("Img_Processing_Wid", "FFT"))
        self.B_IFFT.setText(_translate("Img_Processing_Wid", "IFFT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Img_Processing_Wid = QtWidgets.QWidget()
    ui = Ui_Img_Processing_Wid()
    ui.setupUi(Img_Processing_Wid)
    Img_Processing_Wid.show()
    sys.exit(app.exec_())
