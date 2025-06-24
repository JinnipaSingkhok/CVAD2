import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread("OIIA.jpg",0)
plt.figure("Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

print("Shape:", gray.shape)
plt.show(block=True)
