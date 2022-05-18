import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import os
from sklearn.model_selection import train_test_split

#print(os.getcwd())
bream_length_pd=pd.read_csv("bream_length.csv", names=["length"])
bream_weight_pd=pd.read_csv("bream_weight.csv",names=["weight"])
smelt_length_pd=pd.read_csv("smelt_length.csv", names=["length"])
smelt_weight_pd=pd.read_csv("smelt_weight.csv", names=["weight"])
#print(len(bream_length_pd))
#print(bream_length_pd)
#length = bream_length_pd+bream_weight_pd
#weight = bream_weight_pd + smelt_weight_pd
#print(bream_length_pd)

bream_length = pd.DataFrame.to_numpy(bream_length_pd)
bream_weight = pd.DataFrame.to_numpy(bream_weight_pd)
smelt_length = pd.DataFrame.to_numpy(smelt_length_pd)
smelt_weight = pd.DataFrame.to_numpy(smelt_weight_pd)
#print(bream_length.shape)

plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
#print(bream_length)
#print(bream_weight)
#print(smelt_length)
#print(smelt_weight)

length = np.concatenate([bream_length , smelt_length])
weight = np.concatenate([bream_weight , smelt_weight])

fish_data = np.column_stack((length,weight))
#print (fish_data)
print(fish_data.shape)
fish_target = np.concatenate((np.ones(35),np.zeros(14)))
print (fish_target)
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=41)#랜덤값41로 잡음

#print(train_input.shape, test_input.shape)
#print(test_target)
kn= KNeighborsClassifier()
kn.fit(train_input,train_target)
print(kn.score(test_input,test_target))

plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(test_input[:,0],test_input[:,1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()