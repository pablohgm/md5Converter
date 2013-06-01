# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md5converter.ui'
#
# Created: Fri May 31 17:13:35 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import hashlib

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MD5Converter(object):
    def setupUi(self, MD5Converter):
        MD5Converter.setObjectName(_fromUtf8("MD5Converter"))
        MD5Converter.resize(320, 188)
        self.label = QtGui.QLabel(MD5Converter)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(MD5Converter)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 191, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.plainTextEdit = QtGui.QPlainTextEdit(MD5Converter)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 301, 78))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(MD5Converter)
        self.pushButton.setGeometry(QtCore.QRect(210, 50, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #events
        self.pushButton.clicked.connect(self.onConvertHandler)

        self.retranslateUi(MD5Converter)
        QtCore.QMetaObject.connectSlotsByName(MD5Converter)

    def onConvertHandler(self):
        tmpMd5Code = self.md5Encoding(self.lineEdit.text())
        self.plainTextEdit.setPlainText(tmpMd5Code)

    #Encode from argString to MD5
    def md5Encoding(self, argString):
        code = hashlib.md5()
        code.update(argString)
        return code.hexdigest()

    def retranslateUi(self, MD5Converter):
        MD5Converter.setWindowTitle(QtGui.QApplication.translate("MD5Converter", "MD5Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MD5Converter", "MD5 Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MD5Converter", "Convert", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MD5Converter = QtGui.QDialog()
    ui = Ui_MD5Converter()
    ui.setupUi(MD5Converter)
    MD5Converter.show()
    sys.exit(app.exec_())

