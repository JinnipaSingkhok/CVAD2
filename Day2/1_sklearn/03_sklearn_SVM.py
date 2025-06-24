from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=1)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svm = SVC(kernel='linear')  # ลองเปลี่ยนเป็น 'rbf' 'poly'
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, y_pred))
