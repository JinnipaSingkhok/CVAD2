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
feats = extract_features("OIIA.jpg")
print(feats)

import os
import pandas as pd
image_dir = 'images'
data = []
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.jpg', '.png')):
        label = 'cat' if 'cat' in filename.lower() else 'dog'
        path = os.path.join(image_dir, filename)
        feats = extract_features(path)
        feats['filename'] = filename
        feats['label'] = label
        data.append(feats)
df = pd.DataFrame(data)
print(df.head())

df.to_csv('A.csv', index=False)
print("Feature table saved as features.csv")
