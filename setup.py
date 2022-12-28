import sys
import os
from cx_Freeze import setup, Executable

files = ["TG_icon.ico","image", "yolo_cpp_dll.dll","yolov3.weights","classes.names","cudnn_adv_infer64_8.dll","cudnn_adv_train64_8.dll","cudnn_cnn_infer64_8.dll","cudnn_cnn_train64_8.dll","cudnn_ops_infer64_8.dll","cudnn_ops_train64_8.dll","zlibwapi.dll"]
exFiles = ["matplotlib.tests", "numpy.random._examples"]

target = Executable(
    script="AIVCtools.py",
    base=None,
    icon='TG_icon.ico'
)

setup(
    name = "AutoLabel",
    version = "1.0.0.1",
    description = "Auto Labelling Software By Syafi'i",
    author = "Syafi'i",
    options = {'build_exe' : {'include_files' : files , 'excludes' : exFiles}},
    executables = [target]
)
