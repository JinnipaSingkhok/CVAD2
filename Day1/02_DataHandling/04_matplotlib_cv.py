import cv2
import matplotlib.pyplot as plt
img_cv = cv2.imread("OIIA.jpg")
img_cv_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
plt.imshow(img_cv_rgb)
print(img_cv_rgb.shape)
plt.title("Image from OpenCV")
plt.axis('off')
plt.show()
