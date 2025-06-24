import pandas as pd
import numpy as np
import cv2
img = cv2.imread("OIIA.jpg")
img_rgb =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w, _ = img_rgb.shape
flat = img_rgb.reshape(-1, 3)
x, y = np.indices((h, w))
df = pd.DataFrame({
    'x': x.flatten(),
    'y': y.flatten(),
    'R': flat[:, 0],
    'G': flat[:, 1],
    'B': flat[:, 2]
})
print(df.head())
cv2.imshow("BGR",img)
cv2.imshow("RGB",img_rgb)
cv2.waitKey(0)
cv2.destroyWindow()