import json
import random
import cv2
import matplotlib.pyplot as plt

# 加载标注文件
annotation_file = 'D:/workspace/datasets/balloon/train/coco_format.json'
with open(annotation_file, 'r') as f:
    data = json.load(f)

# 随机选择8张图像
image_dir = 'D:/workspace/datasets/balloon/train'
image_ids = random.sample(data['images'], 8)

# 绘制标注边界框
fig, axs = plt.subplots(2, 4, figsize=(12, 6))
for i, image_id in enumerate(image_ids):
    # 读取图像
    image_path = image_dir + '/' + image_id['file_name']
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 获取图像对应的标注信息
    annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id['id']]

    # 绘制标注边界框
    for ann in annotations:
        bbox = ann['bbox']
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(image, (x, y), (w, h), (255, 0, 0), 2)

    # 在子图中显示图像
    axs[i // 4, i % 4].imshow(image)
    axs[i // 4, i % 4].axis('off')

plt.tight_layout()
plt.show()
