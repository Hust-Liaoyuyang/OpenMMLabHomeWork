**作业**：基于 RTMDet 的气球检测

**背景**：熟悉目标检测和 MMDetection 常用自定义流程。

**任务**：

1. 基于提供的 notebook，将 cat 数据集换成气球数据集
2. 按照视频中 notebook 步骤，可视化数据集和标签
3. 使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标
4. 用网上下载的任意包括气球的图片进行预测，将预测结果发到群里
5. 按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里
   需提交的测试集评估指标（不能低于baseline指标的50%）

- 目标检测 RTMDet-tiny 模型性能不能 65 mAP

**数据集**
气球数据集可以直接下载 <https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip>

同时也欢迎各位选择更复杂的数据集进行训练，可以选用一下 10 类的饮料数据集。
<https://github.com/TommyZihao/Train_Custom_Dataset/tree/main/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E9%9B%86>

课程当中的ipynb请在下面链接下载：
<https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E4%B8%89%E6%AC%A1%E4%BD%9C%E4%B8%9A/rtmdet_cat_tutorial.ipynb>





### 1、可视化数据集

![1686285268476](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/dataset_visual.png?raw=true)

### 2、可视化标签

![1686294649000](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/label_visual.png?raw=true)

### 3、测试集评估指标

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.795
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.916
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.870
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.101
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.636
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.885
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.250
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.808
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.836
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.100
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.733
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.911
06/10 13:34:09 - mmengine - INFO - bbox_mAP_copypaste: 0.795 0.916 0.870 0.101 0.636 0.885
06/10 13:34:10 - mmengine - INFO - Epoch(test) [3/3]    coco/bbox_mAP: 0.7950  coco/bbox_mAP_50: 0.9160  coco/bbox_mAP_75: 0.8700  coco/bbox_mAP_s: 0.1010  coco/bbox_mAP_m: 0.6360  coco/bbox_mAP_l: 0.8850  data_time: 0.7047  time: 1.5096
```

### 4、预测结果

![1686376032578](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/1_raw.jpg?raw=true)

### 5、特征图可视化

**可视化neck三个输出通道**

![1686377009254](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/1_neck.jpg?raw=true)

**可视化backbone三个输出通道**

![1686377023089](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/1_backbone.jpg?raw=true)

### 6、Grad-Based CAM 可视化

**neck 输出的最小输出特征图的 Grad CAM**

![1686377584143](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/1_neck_mingramcam.jpg?raw=true)

**neck 输出的最大输出特征图的 Grad CAM**

![1686377612080](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%89%E6%AC%A1/MMDetection/1_neck_maxgramcam.jpg?raw=true)

