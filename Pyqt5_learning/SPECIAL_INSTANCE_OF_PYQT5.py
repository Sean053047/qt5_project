from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton)
from PyQt5.QtGui import QFont
import sys

class Mywidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()
    
    def __initUI(self):
        self.setWindowTitle("Hey Hey")
        self.setGeometry(400,300,500,500)  #座標：x,y   視窗寬高：寬,高

        self.mylabel =QLabel('hello world',self)      #創建標籤 並且設定標籤內容
        self.mylabel.setFont(QFont('Comic Mono',18))  #設定字形及大小
        self.mylabel.setStyleSheet("background-color: #CCCCFF")  
        
        # self.mylabel.setGeometry(10,100,100,60)       #與.move()有類似的功能，前兩個參數為移動Label 於視窗中的位置，後量個參數為限制Label顯示的長寬
        # self.mylabel.move(200,350)                    #移動 Label 在視窗中的位置
        
        self.mybutton = QPushButton('click',self)       #創建按鈕並給予按鈕上一個字串
        self.mybutton.move(50,40)
        self.mybutton.clicked.connect(self.onButtonClick)#當按鈕按下時連接事件
    def onButtonClick(self):
        self.mybutton.setText('CLICK')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywidget()
    w.show()
    sys.exit(app.exec_())