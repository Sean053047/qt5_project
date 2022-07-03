from sys import setdlopenflags
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage , QPixmap
import cv2
import numpy as np
from  matplotlib import pyplot as plt

from ui_test import Ui_Img_Processing_Wid
#Size of label which show image is 300*300


class MainWindow_controller(QtWidgets.QMainWindow):
    image_subtitle_set = {'jpg','jpeg','jpe','png'}
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Img_Processing_Wid()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.B_FIle.clicked.connect(self.open_file)
        self.ui.B_FFT.clicked.connect(self.Fourier_Transfome)
        self.ui.B_IFFT.clicked.connect(self.Inverse_Fourier_Transform)
    def open_file(self):
        self.imgpath, filetype = QFileDialog.getOpenFileName(self,
                "Open File",
                "/home/sean/Desktop/AICV/")                 # start path
        print(self.imgpath, filetype)
        file_subtitle = self.imgpath[self.imgpath.rfind('.')+1:]
        
        if file_subtitle not in MainWindow_controller.image_subtitle_set:
            print('The file is not an image!')
            return 
        else :
            self.img = cv2.imread(self.imgpath)
            self.Picture = cv2.resize(self.img, (400,400), interpolation=cv2.INTER_AREA)
            
            height , width , channel = self.Picture.shape
            bytesPerline = channel * width
            self.qimg = QImage(self.Picture , width , height ,bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.image.setPixmap(QPixmap.fromImage(self.qimg))
            
            
    def Fourier_Transfome(self):
        try :
            type(self.Picture)
        except: 
            self.ui.FFt.setText("There isn't any image.")
            return 
        self.Picture_Gray = cv2.cvtColor(self.Picture, cv2.COLOR_BGR2GRAY)
        fft = np.fft.fft2(np.float32(self.Picture_Gray))
        self.fshift =  np.fft.fftshift(fft)
        magnitude_spectrum = 20*np.log(np.abs(self.fshift))
        
        new = magnitude_spectrum

        original_interval = new.max()-new.min()
        new = 255/original_interval * (magnitude_spectrum-new.min())
        new = np.around(new,0)
        new.astype('u8')
        
        cv2.imwrite("./FFT.jpeg",magnitude_spectrum)
        magnitude_spectrum = cv2.imread('./FFT.jpeg',0)
        
        # print(f"max = {magnitude_spectrum.max()}\nmin = {magnitude_spectrum.min()}\nitemsize = {magnitude_spectrum.itemsize}")
        
        
        height , width = magnitude_spectrum.shape
        bytesPerline = width 
        self.qimgFft = QImage(magnitude_spectrum , width , height ,bytesPerline, QImage.Format_Indexed8)
        self.ui.FFt.setPixmap(QPixmap.fromImage(self.qimgFft))
        
        
        
        # plt.subplot(121),plt.imshow(self.Picture_Gray, cmap = 'gray')
        # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(magnitude_spectrum, cmap = 'gray')
        # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        # plt.show()
        
        # else :
        #     self.img = cv2.imread(self.imgpath)
        #     Picture = cv2.resize(self.img, (400,400), interpolation=cv2.INTER_AREA)
            
        #     height , width , channel = Picture.shape
        #     bytesPerline = 3 * width
        #     self.qimg = QImage(Picture , width , height ,bytesPerline, QImage.Format_RGB888).rgbSwapped()
        #     self.ui.image.setPixmap(QPixmap.fromImage(self.qimg))
        
    def Inverse_Fourier_Transform(self):
        try :
            type(self.Picture)
        except: 
            self.ui.IFFt.setText("There isn't any image.")
            return 
        try :
            type(self.fshift)
        except :
            self.ui.IFFt.setText("You haven't done Fourier Transform.")
            return
        
        ishift = np.fft.ifftshift(self.fshift)
        iimg = np.fft.ifft2(ishift)
        iimg = np.abs(iimg)

        cv2.imwrite("./IFFT.jpeg",iimg)
        iimg = cv2.imread('./IFFT.jpeg',0)
        
        width,height = iimg.shape
        bytesPerline = width
        self.qimgIfft = QImage(iimg , width , height ,bytesPerline, QImage.Format_Indexed8)
        self.ui.IFFt.setPixmap(QPixmap.fromImage(self.qimgIfft))
    # def open_folder(self):
    #     folder_path = QFileDialog.getExistingDirectory(self,
    #               "Open folder",
    #               "/home/sean/Desktop/")                 # start path
    #     print(folder_path)
    #     self.ui.show_folder.setText(folder_path)
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())