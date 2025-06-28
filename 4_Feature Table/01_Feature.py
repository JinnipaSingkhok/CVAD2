import cv2
import numpy as np
def extract_features(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flat = gray.flatten()
    features = {
        'mean': np.mean(flat),
        'std': np.std(flat),
        'min': np.min(flat),
        'max': np.max(flat),
        'low_pct': np.sum(flat < 50) / len(flat) * 100,
        'high_pct': np.sum(flat > 200) / len(flat) * 100,
    }
    return features
feats = extract_features("example.jpg")
print(feats)

#ถ้าอยากได้ตาราง
import pandas as pd
df = pd.DataFrame([feats]).T
print(df)

