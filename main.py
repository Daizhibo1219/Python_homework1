import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from AirconditionWin2 import Ui_Form #AirconditionWin2是提前写好的UI界面
import requests
import json

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryAircondition(self): #queryAircondition是槽函数，和按钮queary_pushButton绑定，触发信号为clicked
        print('* quearyAircondion ')
        cityName = self.ui.Weather_comboBox.currentText() #将选择的城市名存入cityName
        CITYENAME=self.transCityname(cityName)            #再将相应的中文换成拼音

        r = requests.get('http://www.pm25.in/api/querys/co.json?city=' + CITYENAME + '&token=5j1znBVAsnSf5xQyNQyq') #获取城市空气质量信息
        hjson = json.loads(r.text)
        js = json.dumps(hjson, sort_keys=True, indent=4, separators=(',', ';'), ensure_ascii=False)
        msg1=js
        self.ui.textEdit.setText(msg1)  #将其显示在界面textEdit部分

    def transCityname(self,cityName):  #中文和拼音转换函数
        ename=''
        if cityName == '北京' :
            ename = 'beijing'
        elif cityName == '上海' :
            ename = 'shanghai'
        elif cityName == '合肥' :
            ename = 'hefei'
        elif cityName == '南京' :
            ename = 'nanjing'

        return ename
    def clearResult(self):  #清空界面信息的槽函数
        print('* clearResult ')
        self.ui.textEdit.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())