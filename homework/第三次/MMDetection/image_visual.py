import os
import matplotlib.pyplot as plt
from PIL import Image

original_images = []
images = []
texts = []
plt.figure(figsize=(16, 5))

image_paths = [filename for filename in os.listdir(r'D:\workspace\datasets\balloon\train')][:8]

for i, filename in enumerate(image_paths):
    name = os.path.splitext(filename)[0]

    image = Image.open(r'D:\workspace\datasets\balloon\train\\' + filename).convert("RGB")

    plt.subplot(2, 4, i + 1)
    plt.imshow(image)
    plt.title(f"{filename}")
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()