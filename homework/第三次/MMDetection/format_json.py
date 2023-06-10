import json

# 读取原始的JSON文件
with open(r'D:\workspace\datasets\balloon\val\coco_format.json', 'r') as f:
    data = json.load(f)

# 格式化JSON数据
formatted_json = json.dumps(data, indent=4)

# 输出格式化后的JSON数据到文件
with open(r'D:\workspace\datasets\balloon\val\coco_format.json', 'w') as f:
    f.write(formatted_json)