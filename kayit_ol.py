# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_ol.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(461, 651)
        Form_2.setMinimumSize(QtCore.QSize(461, 651))
        Form_2.setMaximumSize(QtCore.QSize(461, 651))
        self.widget_2 = QtWidgets.QWidget(Form_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 461, 651))
        self.widget_2.setStyleSheet("background-color: #292f45;\n"
"    color: #000000;\n"
"    border-color: #000000;")
        self.widget_2.setObjectName("widget_2")
        self.kayit_ol = QtWidgets.QPushButton(self.widget_2)
        self.kayit_ol.setGeometry(QtCore.QRect(230, 560, 141, 51))
        self.kayit_ol.setMinimumSize(QtCore.QSize(141, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_ol.setFont(font)
        self.kayit_ol.setStyleSheet("QPushButton\n"
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
        self.kayit_ol.setObjectName("kayit_ol")
        self.yeni_sifre_tekrari = QtWidgets.QLineEdit(self.widget_2)
        self.yeni_sifre_tekrari.setGeometry(QtCore.QRect(90, 470, 281, 40))
        self.yeni_sifre_tekrari.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yeni_sifre_tekrari.setFont(font)
        self.yeni_sifre_tekrari.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.yeni_sifre_tekrari.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.yeni_sifre_tekrari.setCursorPosition(0)
        self.yeni_sifre_tekrari.setObjectName("yeni_sifre_tekrari")
        self.yeni_sifre = QtWidgets.QLineEdit(self.widget_2)
        self.yeni_sifre.setGeometry(QtCore.QRect(90, 410, 281, 40))
        self.yeni_sifre.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yeni_sifre.setFont(font)
        self.yeni_sifre.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.yeni_sifre.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.yeni_sifre.setObjectName("yeni_sifre")
        self.yeni_kullanici_adi = QtWidgets.QLineEdit(self.widget_2)
        self.yeni_kullanici_adi.setGeometry(QtCore.QRect(90, 350, 281, 40))
        self.yeni_kullanici_adi.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yeni_kullanici_adi.setFont(font)
        self.yeni_kullanici_adi.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.yeni_kullanici_adi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.yeni_kullanici_adi.setObjectName("yeni_kullanici_adi")
        self.tc_no = QtWidgets.QLineEdit(self.widget_2)
        self.tc_no.setGeometry(QtCore.QRect(90, 170, 281, 40))
        self.tc_no.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tc_no.setFont(font)
        self.tc_no.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.tc_no.setText("")
        self.tc_no.setMaxLength(11)
        self.tc_no.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tc_no.setObjectName("tc_no")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(100, 50, 241, 71))
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
        self.tc_kontrol.setGeometry(QtCore.QRect(390, 180, 21, 21))
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
        self.kullanici_adi_kontrol.setGeometry(QtCore.QRect(390, 360, 21, 21))
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
        self.sifre_kontrol.setGeometry(QtCore.QRect(390, 420, 21, 21))
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
        self.sifre_tekrari_kontrol.setGeometry(QtCore.QRect(390, 480, 21, 21))
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
        self.hata_mesaji.setGeometry(QtCore.QRect(70, 520, 371, 41))
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
        self.ad = QtWidgets.QLineEdit(self.widget_2)
        self.ad.setGeometry(QtCore.QRect(90, 230, 281, 40))
        self.ad.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ad.setFont(font)
        self.ad.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.ad.setText("")
        self.ad.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ad.setObjectName("ad")
        self.soyad = QtWidgets.QLineEdit(self.widget_2)
        self.soyad.setGeometry(QtCore.QRect(90, 290, 281, 40))
        self.soyad.setMinimumSize(QtCore.QSize(251, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.soyad.setFont(font)
        self.soyad.setStyleSheet("QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.soyad.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.soyad.setObjectName("soyad")
        self.ad_kontrol = QtWidgets.QLabel(self.widget_2)
        self.ad_kontrol.setGeometry(QtCore.QRect(390, 240, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.ad_kontrol.setFont(font)
        self.ad_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.ad_kontrol.setText("")
        self.ad_kontrol.setObjectName("ad_kontrol")
        self.soyad_kontrol = QtWidgets.QLabel(self.widget_2)
        self.soyad_kontrol.setGeometry(QtCore.QRect(390, 300, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.soyad_kontrol.setFont(font)
        self.soyad_kontrol.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.soyad_kontrol.setText("")
        self.soyad_kontrol.setObjectName("soyad_kontrol")

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)
        Form_2.setTabOrder(self.tc_no, self.ad)
        Form_2.setTabOrder(self.ad, self.soyad)
        Form_2.setTabOrder(self.soyad, self.yeni_kullanici_adi)
        Form_2.setTabOrder(self.yeni_kullanici_adi, self.yeni_sifre)
        Form_2.setTabOrder(self.yeni_sifre, self.yeni_sifre_tekrari)
        Form_2.setTabOrder(self.yeni_sifre_tekrari, self.kayit_ol)
        Form_2.setTabOrder(self.kayit_ol, self.geri_don)

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Form"))
        self.kayit_ol.setText(_translate("Form_2", "KAYIT OL"))
        self.yeni_sifre_tekrari.setPlaceholderText(_translate("Form_2", "Parola Tekrar"))
        self.yeni_sifre.setPlaceholderText(_translate("Form_2", "Parola"))
        self.yeni_kullanici_adi.setPlaceholderText(_translate("Form_2", "Kullanıcı Adı"))
        self.tc_no.setPlaceholderText(_translate("Form_2", "T.C. Kimlik Numarası"))
        self.label.setText(_translate("Form_2", "Yeni Kayıt"))
        self.ad.setPlaceholderText(_translate("Form_2", "Ad"))
        self.soyad.setPlaceholderText(_translate("Form_2", "Soyad"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_2 = QtWidgets.QWidget()
    ui = Ui_Form_2()
    ui.setupUi(Form_2)
    Form_2.show()
    sys.exit(app.exec_())