# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sifre_unuttum.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_3(object):
    def setupUi(self, Form_3):
        Form_3.setObjectName("Form_3")
        Form_3.resize(441, 587)
        self.widget_2 = QtWidgets.QWidget(Form_3)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 441, 591))
        self.widget_2.setStyleSheet("background-color: #292f45;\n"
"    color: #000000;\n"
"    border-color: #000000;")
        self.widget_2.setObjectName("widget_2")
        self.kaydet = QtWidgets.QPushButton(self.widget_2)
        self.kaydet.setGeometry(QtCore.QRect(220, 510, 141, 51))
        self.kaydet.setMinimumSize(QtCore.QSize(141, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kaydet.setFont(font)
        self.kaydet.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #f0742f;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 17px;\n"
"    border-color: #f0742f;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #fc7c11;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #ff6b35;\n"
"    color: #fff;\n"
"\n"
"}")
        self.kaydet.setFlat(True)
        self.kaydet.setObjectName("kaydet")
        self.yeni_sifre_tekrari = QtWidgets.QLineEdit(self.widget_2)
        self.yeni_sifre_tekrari.setGeometry(QtCore.QRect(80, 410, 281, 40))
        self.yeni_sifre_tekrari.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.yeni_sifre_tekrari.setFont(font)
        self.yeni_sifre_tekrari.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.yeni_sifre_tekrari.setMaxLength(100)
        self.yeni_sifre_tekrari.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.yeni_sifre_tekrari.setCursorPosition(0)
        self.yeni_sifre_tekrari.setObjectName("yeni_sifre_tekrari")
        self.yeni_sifre = QtWidgets.QLineEdit(self.widget_2)
        self.yeni_sifre.setGeometry(QtCore.QRect(80, 330, 281, 40))
        self.yeni_sifre.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.yeni_sifre.setFont(font)
        self.yeni_sifre.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.yeni_sifre.setMaxLength(100)
        self.yeni_sifre.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.yeni_sifre.setObjectName("yeni_sifre")
        self.kullanici_adi = QtWidgets.QLineEdit(self.widget_2)
        self.kullanici_adi.setGeometry(QtCore.QRect(80, 250, 281, 40))
        self.kullanici_adi.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.kullanici_adi.setFont(font)
        self.kullanici_adi.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.kullanici_adi.setMaxLength(100)
        self.kullanici_adi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.tc_no = QtWidgets.QLineEdit(self.widget_2)
        self.tc_no.setGeometry(QtCore.QRect(80, 170, 281, 40))
        self.tc_no.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tc_no.setFont(font)
        self.tc_no.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.tc_no.setText("")
        self.tc_no.setMaxLength(11)
        self.tc_no.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tc_no.setObjectName("tc_no")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(70, 60, 321, 71))
        self.label.setMinimumSize(QtCore.QSize(231, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.label.setObjectName("label")
        self.tc_kontrol = QtWidgets.QLabel(self.widget_2)
        self.tc_kontrol.setGeometry(QtCore.QRect(380, 180, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.tc_kontrol.setFont(font)
        self.tc_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.tc_kontrol.setText("")
        self.tc_kontrol.setObjectName("tc_kontrol")
        self.kullanici_adi_kontrol = QtWidgets.QLabel(self.widget_2)
        self.kullanici_adi_kontrol.setGeometry(QtCore.QRect(380, 260, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.kullanici_adi_kontrol.setFont(font)
        self.kullanici_adi_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.kullanici_adi_kontrol.setText("")
        self.kullanici_adi_kontrol.setObjectName("kullanici_adi_kontrol")
        self.sifre_kontrol = QtWidgets.QLabel(self.widget_2)
        self.sifre_kontrol.setGeometry(QtCore.QRect(380, 350, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.sifre_kontrol.setFont(font)
        self.sifre_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.sifre_kontrol.setText("")
        self.sifre_kontrol.setObjectName("sifre_kontrol")
        self.sifre_tekrari_kontrol = QtWidgets.QLabel(self.widget_2)
        self.sifre_tekrari_kontrol.setGeometry(QtCore.QRect(380, 430, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.sifre_tekrari_kontrol.setFont(font)
        self.sifre_tekrari_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.sifre_tekrari_kontrol.setText("")
        self.sifre_tekrari_kontrol.setObjectName("sifre_tekrari_kontrol")
        self.hata_mesaji = QtWidgets.QLabel(self.widget_2)
        self.hata_mesaji.setGeometry(QtCore.QRect(70, 460, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.hata_mesaji.setFont(font)
        self.hata_mesaji.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color: rgb(255, 0, 0);\n"
"padding-bottom:7px;")
        self.hata_mesaji.setText("")
        self.hata_mesaji.setObjectName("hata_mesaji")
        self.geri_don = QtWidgets.QPushButton(self.widget_2)
        self.geri_don.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.geri_don.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.geri_don.setFont(font)
        self.geri_don.setStyleSheet("QPushButton#geri_don {\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:none;\n"
"    color:rgba(255,255,255,230);\n"
"    padding-bottom:7px;\n"
"}\n"
"QPushButton#geri_don:pressed {\n"
"   color:        #B0BEC5;\n"
"\n"
"}")
        self.geri_don.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resimler/geri_don.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geri_don.setIcon(icon)
        self.geri_don.setIconSize(QtCore.QSize(50, 50))
        self.geri_don.setFlat(True)
        self.geri_don.setObjectName("geri_don")

        self.retranslateUi(Form_3)
        QtCore.QMetaObject.connectSlotsByName(Form_3)
        Form_3.setTabOrder(self.tc_no, self.kullanici_adi)
        Form_3.setTabOrder(self.kullanici_adi, self.yeni_sifre)
        Form_3.setTabOrder(self.yeni_sifre, self.yeni_sifre_tekrari)
        Form_3.setTabOrder(self.yeni_sifre_tekrari, self.kaydet)
        Form_3.setTabOrder(self.kaydet, self.geri_don)

    def retranslateUi(self, Form_3):
        _translate = QtCore.QCoreApplication.translate
        Form_3.setWindowTitle(_translate("Form_3", "Form"))
        self.kaydet.setText(_translate("Form_3", "GÜNCELLE"))
        self.kaydet.setShortcut(_translate("Form_3", "Return"))
        self.yeni_sifre_tekrari.setPlaceholderText(_translate("Form_3", "Yeni Parola Tekrarı"))
        self.yeni_sifre.setPlaceholderText(_translate("Form_3", "Yeni Parola"))
        self.kullanici_adi.setPlaceholderText(_translate("Form_3", "Kullanıcı Adı"))
        self.tc_no.setPlaceholderText(_translate("Form_3", "T.C. Kimlik Numarası"))
        self.label.setText(_translate("Form_3", "Şifre Sıfırlama"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_3 = QtWidgets.QWidget()
    ui = Ui_Form_3()
    ui.setupUi(Form_3)
    Form_3.show()
    sys.exit(app.exec_())