import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

# Fake training data
X = np.array([
[2,3,80,200000,90],
[1,4,100,500000,95],
[6,1,20,30000,20],
[12,0,10,10000,5],
[24,0,5,5000,3],
[3,2,60,150000,70],
[8,1,25,45000,25],
[36,0,6,8000,2]
])

y = np.array([1,1,0,0,0,1,0,0])

model = RandomForestClassifier()

model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))

print("Model saved successfully!")