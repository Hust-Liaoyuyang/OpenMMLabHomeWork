**题目**：基于RTMPose的耳朵穴位关键点检测

**背景**：根据中医的“倒置胎儿”学说，耳朵的穴位反映了人体全身脏器的健康，耳穴按摩可以缓解失眠多梦、内分泌失调等疾病。耳朵面积较小，但穴位密集，涉及耳舟、耳轮、三角窝、耳甲艇、对耳轮等三维轮廓，普通人难以精准定位耳朵穴位。

**任务**
1.Labelme标注关键点检测数据集（子豪兄已经帮你完成了）
2.划分训练集和测试集（子豪兄已经帮你完成了）
3.Labelme标注转MS COCO格式（子豪兄已经帮你完成了）
4.使用MMDetection算法库，训练RTMDet耳朵目标检测算法，提交测试集评估指标
5.使用MMPose算法库，训练RTMPose耳朵关键点检测算法，提交测试集评估指标
6.用自己耳朵的图像预测，将预测结果发到群里
7.用自己耳朵的视频预测，将预测结果发到群里
需提交的测试集评估指标（不能低于baseline指标的50%）

- 目标检测Baseline模型（RTMDet-tiny）
  [![242781076-0a1e11f3-5d6d-47b2-8617-06a83a490549](https://user-images.githubusercontent.com/18253636/242839237-e5b8d605-05f3-4e66-a33b-1ce8f8131574.jpg)](https://user-images.githubusercontent.com/18253636/242839237-e5b8d605-05f3-4e66-a33b-1ce8f8131574.jpg)
- 关键点检测Baseline模型（RTMPose-s）
  [![242781136-3c1eeaa9-3599-4a89-ae01-ca3eddc7f52e](https://user-images.githubusercontent.com/18253636/242839254-171bbd5d-b630-46a7-9df1-8eadb1034b19.png)](https://user-images.githubusercontent.com/18253636/242839254-171bbd5d-b630-46a7-9df1-8eadb1034b19.png)

**数据集**
耳朵穴位关键点检测数据集，MS COCO格式，划分好了训练集和测试集，并写好了样例config配置文件
链接: <https://pan.baidu.com/s/1swTLpArj7XEDXW4d0lo7Mg> 提取码: 741p
标注人：张子豪、田文博



自训练RTMDet-tiny

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.757
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.968
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.968
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.757
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.795
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.795
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.795
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.795
06/03 00:13:49 - mmengine - INFO - bbox_mAP_copypaste: 0.757 0.968 0.968 -1.000 -1.000 0.757
06/03 00:13:49 - mmengine - INFO - Epoch(val) [200][11/11]    coco/bbox_mAP: 0.7570  coco/bbox_mAP_50: 0.9680  coco/bbox_mAP_75: 0.9680  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.7570  data_time: 0.2474 
 time: 0.3138
```



自训练RTMDet-s

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.849
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.970
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.849
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.874
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.874
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.874
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.874
06/03 15:07:45 - mmengine - INFO - bbox_mAP_copypaste: 0.849 0.970 0.970 -1.000 -1.000 0.849
06/03 15:07:45 - mmengine - INFO - Epoch(val) [300][9/9]    coco/bbox_mAP: 0.8490  coco/bbox_mAP_50: 0.9700  coco/bbox_mAP_75: 0.9700  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.8490  data_time: 0.0940  t
ime: 0.1621
```



自训练RTMPose-s

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.753
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.970
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.793
 Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
 Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.976
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.793
06/03 19:05:55 - mmengine - INFO - Evaluating PCKAccuracy (normalized by ``"bbox_size"``)...
06/03 19:05:55 - mmengine - INFO - Evaluating NME...
06/03 19:05:55 - mmengine - INFO - Epoch(val) [300][6/6]    coco/AP: 0.752676  coco/AP .5: 1.000000  coco/AP .75: 0.970297  coco/AP (M): -1.000000  coco/AP (L): 0.752676  coco/AR: 0.792857  coco/AR .5: 1.000000  coco/AR .75: 0.97619
0  coco/AR (M): -1.000000  coco/AR (L): 0.792857  PCK: 0.976190  AUC: 0.136224  NME: 0.040038  data_time: 0.884498  time: 0.967561
```



目标检测结果

```shell
python .\demo\image_demo.py
..\datasets\MMPose\Ear210_Keypoint_Dataset_coco\images\DSC_5666.jpg
.\work_dirs\rtmdet_s_8xb32-300e_coco\rtmdet_s_8xb32-300e_coco.py
--weights .\work_dirs\rtmdet_s_8xb32-300e_coco\epoch_300.pth
--out-dir .\outputs\ear_detect
--device cuda:0
--pred-score-thr 0.3
```

![示例图像](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%80%E6%AC%A1/MMDetect/outputs/ear_detect/vis/DSC_5666.jpg?raw=true)



关键点检测结果

```shell
 python  .\demo\topdown_demo_with_mmdet.py 
 ..\mmdetection\work_dirs\rtmdet_s_8xb32-300e_coco\rtmdet_s_8xb32-300e_coco.py
 ..\mmdetection\work_dirs\rtmdet_s_8xb32-300e_coco\epoch_300.pth 
 .\data\rtmpose-s-ear.py 
 .\work_dirs\rtmpose-s-ear\epoch_300.pth 
 --input ..\datasets\MMPose\Ear210_Keypoint_Dataset_coco\images\DSC_5666.jpg 
 --output-root .\outputs\ear_keypoint 
 --device cuda:0 
 --bbox-thr 0.5 
 --kpt-thr 0.5 
 --nms-thr 0.3 
 --radius 8 
 --thickness 4 
 --draw-bbox 
 --draw-heatmap 
 --show-kpt-idx
```

![实例图像](https://github.com/Hust-Liaoyuyang/OpenMMLabHomeWork/blob/master/homework/%E7%AC%AC%E4%B8%80%E6%AC%A1/MMPose/outputs/ear_keypoint/DSC_5666.jpg?raw=true)

