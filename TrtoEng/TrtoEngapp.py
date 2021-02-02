# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:17:42 2021

@author: esmac
"""
#Kütüphaneler
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QTextEdit
from PyQt5.QtGui import QPalette,QColor,QFont


#Arka planları boyamak için Color adında bir class oluşturuyoruz.
class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)
        
"""
Ana pencereyi oluşturmak için bir class tanımladık. Ana pencere özellikleri __init__ fonksiyonu
altında topladık. initUI fonksiyonunda layoutları hizalama,renk belirleme ve onlara QTextEdit
ile yazma özelliği verdik. txt2'ye sadece okuma özelliği verdik ki oluşturulan metni kullanıcı
kopyalayabilsin.Ve son olarak oluşturduğumuz butona translate fonksiyonu göndererek etkin bir hale getirdik.
""" 

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("TRtoENG")
        self.setGeometry(400,150,1000,800)
        self.initUI()
        
    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Color("#9999a3"))
        layout.addWidget(Color("#8c8c9e"))
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(50)
        
        self.lbl1=QtWidgets.QLabel(self)
        self.lbl1.setText("Turkish Text")
        self.lbl1.setFont(QFont('Times', 10))
        self.lbl1.resize(150,35)
        self.lbl1.move(13,9)

        self.txt1 = QTextEdit(self)
        self.txt1.move(23,40)
        self.txt1.resize(950,310)
    

        self.lbl2=QtWidgets.QLabel(self)
        self.lbl2.setText("English Text")
        self.lbl2.setFont(QFont('Times', 10))
        self.lbl2.resize(150,30)
        self.lbl2.move(13,430)

        self.txt2 = QTextEdit(self)
        self.txt2.move(23,460)
        self.txt2.resize(950,310)
        self.txt2.setReadOnly(True)
    
    
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(870,385)
        self.btn.setText("Translate")
        self.btn.clicked.connect(self.translate)
    
    #Burada Türkçe karakterleri İngilizce karaktere çevirmek için bir translate adında bir fonksiyon tanımladık.
    def translate(self):
        tr="ğĞçÇşŞüÜöÖıİ"
        en="gGcCsSuUoOiI"
        result = str(self.txt1.toPlainText()).translate(str(self.txt1.toPlainText()).maketrans(tr,en))     
        self.txt2.setText(result)

        
        
#Son olarak app fonksiyonu ile sistemden uygulamamızı başlatıp,ana classımızı çağrıyoruz.        
def app():
    app=QApplication(sys.argv)
    win=MainForm()
    win.setFixedSize(1000,800) #pencere ayarlarını sabit kıldım. Bu nedenle kullanıcı herhangi bir büyültme ya da küçültme yapamaz
    win.show()
    sys.exit(app.exec_())
    
app()    

"""
Bu uygulamayı bir .exe dosyasına dönüştürdüm isterseniz son olarak oraya bakıp projeyi inceleyebilirsiniz.
"""
        
        
        
 
 