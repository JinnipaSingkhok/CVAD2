import numpy as np
from PIL import Image #PIL = Python Image Library
img = Image.open("OIIA.jpg")
img = img.convert("RGB")
img_np = np.array(img)
print(img_np.shape)
