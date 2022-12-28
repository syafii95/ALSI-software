import glob,os
import time
import cv2
import numpy as np
import darknet
from cfgGenerator import generateYoloCfg
import pathlib
from MainWindow import Ui_MainWindow
import shutil
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

CLASSES=[]

class MainWindow(QMainWindow):
    def __init__(self,class_num):
        super(MainWindow, self).__init__()
        self.clssNum = class_num
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_2.addItems(CLASSES)
        self.ui.comboBox_2.currentIndexChanged.connect(self.comboBoxSelection)
        self.ui.radioButton_labelling.toggled.connect(lambda:self.radioStatus(self.ui.radioButton_labelling))
        self.ui.radioButton_Sorting.toggled.connect(lambda:self.radioStatus(self.ui.radioButton_Sorting))
        self.ui.btn_browse_2.clicked.connect(self.pick_new)
        self.ui.btn_start_2.clicked.connect(self.startAutoLabel)
        self.ui.lineEdit_2.setReadOnly(True)
        self.detectionHandler = darknet_detect(self.clssNum)
        self.sortingHandler = Sorting()
        self.detectionHandler.detectionStatus.connect(self.setLabelStatus)
        self.detectionHandler.progresStatus.connect(self.setProgressBar)
        self.detectionHandler.finishStatus.connect(self.enableStartBtn)
        self.sortingHandler.completeStatus.connect(self.setLabelStatus)
        self.sortingHandler.progresSortingStatus.connect(self.setProgressBar)
        self.sortingHandler.finishSortingStatus.connect(self.enableStartBtn)
        self.enableLabelling = False
        self.enableSorting = False

    def enableStartBtn(self,status):
        if status:
            self.ui.btn_start_2.setEnabled(True)

    def setProgressBar(self,val,maxLen):
        self.ui.progressBar_2.setMaximum(maxLen)
        self.ui.progressBar_2.setValue(val)

    def setLabelStatus(self,txt):
        self.ui.label_status.setText(txt)

    def comboBoxSelection(self):
        idx = self.ui.comboBox_2.currentIndex()
        txt = self.ui.comboBox_2.currentText()
        #print(idx,"is the current index")
        #print("The new selection is: ", txt)

    def radioStatus(self,b):
        if b.text() =="Auto Labelling":
            if b.isChecked() == True:
                #print('First++')
                self.ui.comboBox_2.setCurrentIndex(12)
                self.ui.comboBox_2.setEnabled(False)
                self.enableLabelling = True
            else:
                #print("First deselected")
                self.enableLabelling = False
        else:
            if b.isChecked() == True:
                #print('Second++')
                self.ui.comboBox_2.setEnabled(True)
                self.enableSorting = True
            else:
                #print("Second deselected")
                self.enableSorting = False

    def pick_new(self):
        dialog = QFileDialog()
        self.folder_path = dialog.getExistingDirectory(None, "Select Folder")
        self.ui.lineEdit_2.setText(self.folder_path)
        
    def startAutoLabel(self):
        clsAutoLabelTxt = self.ui.comboBox_2.currentText()
        if self.enableLabelling:
            self.ui.label_status.setText("Starting...")
            self.ui.btn_start_2.setEnabled(False)
            self.detectionHandler.runDetection(clsAutoLabelTxt,self.folder_path)
            
        if self.enableSorting:
            self.ui.label_status.setText("Sorting...")
            self.ui.btn_start_2.setEnabled(False)
            idxCls = self.ui.comboBox_2.currentIndex()
            self.sortingHandler.getPath(clsAutoLabelTxt,self.folder_path,idxCls)

        if not self.enableLabelling and not self.enableSorting:
            self.ui.label_status.setText("Please select atleast 1 options")
            #print("Please select atleast 1 options")
        

class Sorting(QThread):
    completeStatus=pyqtSignal(str)
    finishSortingStatus=pyqtSignal(bool)
    progresSortingStatus=pyqtSignal(int,int)
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.filecount=0

    def getPath(self,cls,path,idxCls):
        convSTR11 = path.replace("\\", "/")
        filePath = os.listdir(convSTR11)
        dst = f'{convSTR11}\{cls}'
        for filename in filePath:
            isText = filename.endswith(".txt")
            if isText:
                scFile = f'{convSTR11}/{filename}'
                with open(scFile) as f:
                    clsTxt = f.readline().strip('\n')
                    try:
                        if int(clsTxt[:2]) == idxCls: # sorting file to the new folder
                            self.filecount += 1
                            srcImg = f'{convSTR11}\{filename[:-4]}.jpg' #src image
                            srcImg = srcImg.replace("\\", "/") #src image
                            src = f'{convSTR11}\{filename}' # src text
                            src = src.replace("\\", "/") # src text
                            #self.completeStatus.emit(filename[:-4])
                            #print(self.filecount,len(filePath))
                            self.progresSortingStatus.emit(self.filecount,len(filePath))
                            lab = f'{self.filecount} image sorted'
                            self.completeStatus.emit(lab)
                            if not os.path.exists(dst): #if folder not exist
                                os.mkdir(dst)
                                shutil.copy2(src,dst) # copy text
                                shutil.copy2(srcImg,dst) # copy Image
                                print(f'Path not exist. Create new one: {dst}')
                                f.close()
                                os.remove(src) # delete txt file
                                os.remove(srcImg) # delete image file
                            else:
                                shutil.copy2(src, dst) # copy text
                                shutil.copy2(srcImg, dst) # copy Image 
                                f.close()
                                os.remove(src) # delete txt file
                                os.remove(srcImg) # delete image file
                    except:
                        print(" ")

        pathF = os.path.realpath(dst)
        try:
            os.startfile(pathF)
        except:
            print("Folder not exist")
        self.filecount=0 
        self.progresSortingStatus.emit(len(filePath),len(filePath))
        self.finishSortingStatus.emit(True)


class darknet_detect(QThread):
    detectionStatus=pyqtSignal(str)
    progresStatus=pyqtSignal(int,int)
    finishStatus=pyqtSignal(bool)
    def __init__(self,clsNum, parent=None):
        super().__init__(parent=parent)
        self.clsNum = clsNum
        config_file=generateYoloCfg(self.clsNum)
        self.imgCount=-1
        weights = "yolov3.weights"
        batch_size=1
        self.network, self.class_names, class_colors = darknet.load_network(config_file,CLASSES,weights,batch_size)
        self.width = darknet.network_width(self.network)
        self.height = darknet.network_height(self.network)
        self.darknet_image = darknet.make_image(self.width, self.height, 3)
        darknet.detect_image(self.network, self.class_names, self.darknet_image, thresh=0.25) ##Predict first dummy##     
        
    def runDetection(self,clsAutoLabelTxt,folderPath):
        newpathh = os.listdir(folderPath)
        for filename in newpathh:
            label=''
            isImage = filename.endswith(".jpg")
            if isImage:
                t = time.time() 
                image = cv2.imread(os.path.join(folderPath,filename))
                image_resized = cv2.resize(image, (self.width, self.height),
                                        interpolation=cv2.INTER_LINEAR)
                h, w, ch = image_resized.shape
                darknet.copy_image_from_bytes(self.darknet_image, image_resized.tobytes())
                bboxes = darknet.detect_image(self.network, self.class_names, self.darknet_image, thresh=0.25)
                bboxes = self.filterMultipleBbox(bboxes)
                for i in bboxes:
                    xc = i[2][0]/w
                    yc = i[2][1]/h
                    widthFrame = i[2][2]/w
                    heightFrame = i[2][3]/h
                    cls=int(i[0])
                    if CLASSES[cls] == clsAutoLabelTxt:
                        self.imgCount += 1
                        #print(f'Number of image: {clsAutoLabelTxt}')
                        stat = f'{self.imgCount} image complete'
                        label+=f"{12} {xc} {yc} {widthFrame} {heightFrame}\n"
                        self.saveLabel(filename,folderPath,label)
                        self.detectionStatus.emit(stat)
                        self.progresStatus.emit(self.imgCount,len(newpathh))
                #image = darknet.draw_boxes(bboxes, image_resized, class_colors, CLASSES)
                #cv2.imshow('image', image)
                #print(time.time()-t)

                cv2.waitKey(0)
        self.imgCount = 0
        self.progresStatus.emit(len(newpathh),len(newpathh))
        self.finishStatus.emit(True)
        print("Image labelling Complete")

    def saveLabel(self,filename,folderPath,label=None):
        txtFileName=f'{filename[:-4]}.txt'
        txtFileNames = os.path.join(folderPath,txtFileName)
        with open(txtFileNames, "a+") as f:
            f.seek(0)
            f.write(label)

    def filterMultipleBbox(self,best_bboxes):
        if len(best_bboxes) > 0:
            scores = [box[1] for box in best_bboxes]
            best_index = scores.index(max(scores))
            best_bboxes = [best_bboxes[best_index]]
        
        return best_bboxes

if __name__ == '__main__':
    #a = docker_detect()
    try:
        with open('classes.names','r') as names:
            for name in names:
                    CLASSES.append(name.strip('\n'))
    except FileNotFoundError as e:
        print("classes.names Missing")
        #classes.names not found, use default name instead
        CLASSES=["Good Glove","Tearing","Single Arm","Double Dip", "Unstripped","No Glove","Stained", "Lump", "Broken Former", "Other"]
    class_num = len(CLASSES)
    app = QApplication(sys.argv)
    window = MainWindow(class_num)
    window.show()
    ret=app.exec_()
    sys.exit(ret)