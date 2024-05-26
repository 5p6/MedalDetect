### 1.介绍
本仓库是一个用于金属缺陷检测系统的代码，它可以使用`config`中的`yolov8m.onnx`作为检测模型权重，使用yolov8计算金属表面缺陷，同时可以选择是否保存带有缺陷信息的图像或者目标缺陷信息。
### 2.实验环境
* Windows 11
* Python 3.9
* PyQt5
* OpenCV 4.x
* numpy
* yaml

### 3.使用方法
```shell
python main.py
```
其中本目录下的 `images` 为测试图像，`config` 文件夹下具有权重模型 `yolov8.m`.