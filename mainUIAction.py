import sys
import mainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QImage
import cv2
import numpy as np
from modelcom import *
import yaml


# 业务类需要继承两个类，一个设计的主界面，另一个是QMainWindow
class mainUIAction(mainUI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mainUIAction, self).__init__()
        # onnx 模型路径
        self.OnnxFile = None
        # 输入输出图像
        self.InputImage = None
        self.OutputImage = None
        # 模型
        self.model = None
        # Ui
        self.setupUi(self)
        # 设置回调事件
        self.pushButton_Input.clicked.connect(self.CallBackInput)
        self.pushButton_Onnx.clicked.connect(self.CallbackOnnx)
        self.pushButton_Run.clicked.connect(self.Run)
        self.pushButton_Write.clicked.connect(self.CallbackWrtie)
        self.pushButton_Result_Write.clicked.connect(self.CallbackResultWrtie)

    # 输入回调
    def CallBackInput(self):
        # 打开文件对话框，选择文件
        print("选择输入图像")
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*.png *.jpg *.bmp)')
        if self.checkNone(file_path):
            return False
        # 输入图像读取
        self.InputImage = cv2.imread(file_path)
        # 中间数据
        height, width, channels = self.InputImage.shape
        bytes_per_line = channels * width
        q_image = QImage(self.InputImage.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        # 设置 QLabel 的图像
        self.label_InputImage.setPixmap(pixmap)
        self.label_InputImage.setScaledContents(True)
        return True
    
    # 读取onnx回调
    def CallbackOnnx(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'Onnx Files (*.onnx)')
        # 是否为空
        if self.checkNone(file_path):
            return False
        # 是否为 onnx 模型
        strarr = file_path.split(".")
        if not strarr[len(strarr) - 1] == "onnx":
            print("输入模型错误,模型后缀应为 *.onnx !")
            return False
        # 设置 Onnx 模型路径
        self.OnnxFile = file_path
        print("开始读取 onnx 模型 !")
        self.ReadOnnx()
        print("读取完成 !")
        self.text_onnxpath.insertPlainText(file_path)
        return True
    
    # 写入回调
    def CallbackWrtie(self):
        # 打开文件对话框，选择文件
        print("选择保存路径")
         # 打开文件对话框，选择保存路径
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Images (*.png *.jpg)')
        if self.checkNone(file_path):
            return False
        cv2.imwrite(file_path,self.OutputImage)


    # 结果写入回调
    def CallbackResultWrtie(self):
        # 打开文件对话框，选择文件
        print("选择保存路径")
         # 打开文件对话框，选择保存路径
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Param', '', 'Params (*.yaml )')
        if self.checkNone(file_path):
            return False
        objects = []
        for detection in self.Detections:
            detect_yaml = { "object":{} }
            detect_yaml["object"]["class_name"] = detection["class_name"]
            detect_yaml["object"]["confidence"] = detection["confidence"]
            detect_yaml["object"]["box"] = {
                "lefttop": {"width" : int(detection["box"][0]), "height" : int(detection["box"][1])},
                "rightdown": {"width" : int(detection["box"][0] + detection["box"][2]), "height" :  int(detection["box"][1] + detection["box"][3])}
            }
            objects.append(detect_yaml)
        with open(file_path, "w") as file:
            yaml.dump(objects, file, default_flow_style=False)
        print("保存完成")
    def ReadOnnx(self):
        self.model = LoadModel(self.OnnxFile)

    def Run(self):
        # print(self.InputImage)
        if self.model == None:
            print("请查看输入的模型是否存在 ! ")
            return False
        elif self.InputImage.any() == None:
            print("请查看输入的图像是否存在 ! ")
            return False
        
        _,self.OutputImage,self.Detections = inference(self.InputImage,self.model)
        # print(Detections)
        # 中间数据
        height, width, channels = self.OutputImage.shape
        bytes_per_line = channels * width
        q_image = QImage(self.OutputImage.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        # 设置 QLabel 的图像
        self.label_OutputImage.setPixmap(pixmap)
        self.label_OutputImage.setScaledContents(True)

        self.text_edit.clear()
        for i,detection in enumerate(self.Detections):
            message = "Index {}  class name : {} , the confidence : {} ,the rectangle box :  left top point -->  {}   right down point --> {} ! \n".format(i,detection["class_name"],round(detection["confidence"],3),(int(detection["box"][0]),int(detection["box"][1])),(int(detection["box"][0] + detection["box"][2]),int(detection["box"][1] + detection["box"][3])))
            self.text_edit.append(message)
        return True

    def checkNone(self,file : str):
        return file == ""



