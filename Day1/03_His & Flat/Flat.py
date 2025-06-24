import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread("OIIA.jpg",0)
plt.figure("Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure("Histogram")
plt.plot(hist, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Pixel Count')
plt.grid(True)

gray_flat = gray.flatten()
print("Flatten vector shape:", gray_flat.shape)
print("First 10 values:", gray_flat[:10])
plt.figure("Flatten Vector")
plt.plot(gray_flat[:1000], color='blue')  # แสดงแค่ 1000 จุดแรกเพื่อความเร็ว
plt.title('Flattened Grayscale Vector (first 1000 values)')
plt.xlabel('Pixel Index')
plt.ylabel('Intensity')
plt.grid(True)

plt.show(block=True)