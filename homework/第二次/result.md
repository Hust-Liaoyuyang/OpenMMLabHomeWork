**题目**：基于 ResNet50 的水果分类

**背景**：使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类

**任务**

> 1. 划分训练集和验证集
> 2. 按照 MMPreTrain CustomDataset 格式组织训练集和验证集
> 3. 使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型
> 4. 在水果数据集上进行微调训练
> 5. 使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类
>    需提交的验证集评估指标（不能低于 60%）

- ResNet-50

[![img](https://user-images.githubusercontent.com/18253636/243641271-c6c30aca-ebee-4b17-acd0-a05bd798c26f.jpg)](https://user-images.githubusercontent.com/18253636/243641271-c6c30aca-ebee-4b17-acd0-a05bd798c26f.jpg)

**作业数据集下载：**
链接：<https://pan.baidu.com/s/1YgoU1M_v7ridtXB9xxbA1Q>
提取码：52m9

**课程中猫狗数据集下载地址：**
<https://download.openmmlab.com/mmclassification/dataset/cats_dogs_dataset.tar>





### 对数据集进行划分

```python
import os

# 获取数据集文件夹路径
CustomDatasetPath = r'D:\workspace\datasets\fruit30_train'
# 获取数据集文件夹下的所有文件
CustomDatasetFile = os.listdir(CustomDatasetPath)
# 如果文件夹中不存在train、val、test文件夹，则创建
dataset_type = ['train', 'val', 'test']
for type in dataset_type:
    if type not in CustomDatasetFile:
        os.mkdir(os.path.join(CustomDatasetPath, type))
    else:
        # 清空文件夹
        os.removedirs(os.path.join(CustomDatasetPath, type))

# 遍历所有文件
for fruit_name in CustomDatasetFile:
    for type in dataset_type:
        os.mkdir(os.path.join(CustomDatasetPath, type, fruit_name))
    # 水果文件夹路径
    fruit_path = os.path.join(CustomDatasetPath, fruit_name)
    # 获取水果文件夹下的所有文件
    fruit_file = os.listdir(fruit_path)
    # 将水果文件夹下的所有文件分为训练集、验证集、测试集
    train_file = fruit_file[:int(len(fruit_file)*0.8)]
    val_file = fruit_file[int(len(fruit_file)*0.8):int(len(fruit_file)*0.9)]
    test_file = fruit_file[int(len(fruit_file)*0.9):]
    # 将训练集、验证集、测试集分别放入对应文件夹
    for file in train_file:
        os.rename(os.path.join(fruit_path, file), os.path.join(CustomDatasetPath, 'train', fruit_name, file))
    for file in val_file:
        os.rename(os.path.join(fruit_path, file), os.path.join(CustomDatasetPath, 'val', fruit_name, file))
    for file in test_file:
        os.rename(os.path.join(fruit_path, file), os.path.join(CustomDatasetPath, 'test', fruit_name, file))
    # 删除空文件夹
    os.removedirs(fruit_path)


```



### 配置文件

见MMPretrain下**resnet50_8xb32_in1k_fruit_classify.py**

### 验证集评估指标

```shell
06/06 22:26:30 - mmengine - INFO - Epoch(val) [100][55/55]    accuracy/top1: 67.8899  accuracy/top5: 92.8899  data_time: 0.0008  time: 0.0159
```

可以看出验证集的评估指标较低，原因，初始学习率设置过大，收敛困难，将学习率调小后验证集评估指标如下

```shell
2023/06/08 22:15:35 - mmengine - INFO - Epoch(val) [50][28/28]    accuracy/top1: 94.4954  accuracy/top5: 99.0826  data_time: 0.0253  time: 0.0380
```

达到了较好的94.4954

使用ImageClassificationInferencer 接口进行分类

![测试图像](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%BA%8C%E6%AC%A1/MMPretrain/88.png?raw=true)



![测试图像](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%BA%8C%E6%AC%A1/MMPretrain/prediction.jpg?raw=true)