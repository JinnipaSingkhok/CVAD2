# ให้คุณใช้ข้อมูล Iris dataset เพื่อเทรนและทดสอบโมเดลทั้ง 4 ตัว ได้แก่
# # k-Nearest Neighbors (k=3)
# # Support Vector Machine (kernel='linear')
# # Decision Tree (max_depth=3)
# # Random Forest (n_estimators=100)
# # จากนั้น พล็อตกราฟเปรียบเทียบความแม่นยำ (accuracy) ของแต่ละโมเดล
# # Guide
# # Load ข้อมูลจาก sklearn.datasets.load_iris()
# # แบ่ง train/test ด้วย train_test_split(test_size=0.3)
# # สร้างโมเดลทั้ง 4
# # Train + Predict + คำนวณ accuracy
# # Plot bar chart เพื่อเปรียบเทียบ accuracy ของแต่ละโมเดล

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.5, random_state=42)

# Initialize models
models = {
    'kNN (k=3)': KNeighborsClassifier(n_neighbors=3),
    'SVM (linear)': SVC(kernel='linear'),
    'Decision Tree': DecisionTreeClassifier(max_depth=3),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

# Train and evaluate each model
accuracies = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies[name] = acc
    print(f"{name} Accuracy: {acc:.2f}")

# Plot comparison
plt.figure(figsize=(8, 5))
plt.bar(accuracies.keys(), accuracies.values())
plt.ylim(0.8, 1.0)
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison on Iris Dataset")
plt.xticks(rotation=15)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
