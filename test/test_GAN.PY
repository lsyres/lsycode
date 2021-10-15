import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mnist_train.csv")
row = 0
data = df.iloc[row]
label = data[0]
img = data[1:].values.reshape(28,28)
plt.imshow(img)
plt.show()