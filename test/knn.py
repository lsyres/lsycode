from collections import Counter
import numpy as np

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1 - x2)**2))

class KNN:
    def __init__(self,k=3):
        self.k = k
    
    def fit(self,X,y):
        self.X_train = X
        self.y_train = y 
    
    def predict(self,X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self,x):
        # 在训练集里面计算所以其他点到x点的距离
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]
        # 根据距离排序，返回前K个邻居的 index
        k_idx = np.argsort(distances)[:self.k]
        # 提取出前k个最近邻居的类别labels
        k_neighbor_lables = [self.y_train[i] for i in k_idx]
        # 返回出现频率最高的类别label
        most_common = Counter(k_neighbor_lables).most_common(1)
        return most_common[0][0]

model = KNN(k=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)