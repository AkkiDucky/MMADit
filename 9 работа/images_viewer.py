from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, QCoreApplication
from PyQt5.QtGui import QPixmap
import sys
import os

class App(QWidget):
    root = QVBoxLayout()
    curr_index = 0
    list_paths = []
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        set_path = QPushButton('изменить путь')
        set_path.clicked.connect(self.set_path)
        self.root.addWidget(set_path)
        
        self.label = QLabel()
        self.root.addWidget(self.label)

        box = QHBoxLayout()
        back = QPushButton('<')
        back.clicked.connect(self.back)
        forv = QPushButton('>')
        forv.clicked.connect(self.forv)
        box.addWidget(back)
        box.addWidget(forv)
        
        self.root.addLayout(box)
        
        self.setLayout(self.root)
        self.setWindowTitle('Image Viewer')
        self.resize(500,500)
        self.show()
    def set_path(self):
        formats = ['png', 'jpg', 'jpeg', 'tiff', 'bmp']
        file = str(QFileDialog.getExistingDirectory(self, "Выберите путь"))
        if file:
            self.path = file
            for i in os.listdir(file):
                s = i.split('.')
                if s[len(s)-1] in formats:
                    self.list_paths.append(file+'/'+i)
            f = self.list_paths[0]
            pxmap = QPixmap(f)
            self.label.setPixmap(pxmap)
    def back(self):
        if not self.curr_index==0:
            self.curr_index -= 1
            f = self.list_paths[self.curr_index]
            pxmap = QPixmap(f)
            self.label.setPixmap(pxmap)
    def forv(self):
        if not self.curr_index == len(self.list_paths)-1:
            self.curr_index += 1
            f = self.list_paths[self.curr_index]
            pxmap = QPixmap(f)
            self.label.setPixmap(pxmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
