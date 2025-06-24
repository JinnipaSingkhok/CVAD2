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

plt.show(block=True)