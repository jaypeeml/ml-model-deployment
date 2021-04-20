# -*- coding: utf-8 -*-
"""pytorch_create_save.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1644ZJOmg5Fi6hx5hvUKBqnUeHHWBTB5s
"""

import torch
import torch.nn as nn
from torch.nn import functional as F

import pandas as pd
import numpy as np

dataset = pd.read_csv('https://raw.githubusercontent.com/futurexskill/ml-model-deployment/main/storepurchasedata_large.csv')

dataset.describe()

dataset.head()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =.20,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

Xtrain_ = torch.from_numpy(X_train).float()
Xtest_ = torch.from_numpy(X_test).float()

Xtrain_

ytrain_ = torch.from_numpy(y_train)
ytest_ = torch.from_numpy(y_test)

ytrain_

Xtrain_.shape, ytrain_.shape

Xtest_.shape, ytest_.shape

input_size=2
output_size=2
hidden_size=10

class Net(nn.Module):
   def __init__(self):
       super(Net, self).__init__()
       self.fc1 = torch.nn.Linear(input_size, hidden_size) #fc stands for fully connected layer
       self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
       self.fc3 = torch.nn.Linear(hidden_size, output_size)# here we have 2 hidden layer of each size 10


   def forward(self, X):
       X = torch.relu((self.fc1(X)))  # relu activation fn in hidden layer1
       X = torch.relu((self.fc2(X)))  # relu activation fn in hidden layer2
       X = self.fc3(X)

       return F.log_softmax(X,dim=1) ## softmax activation fn in output layer

model = Net()

import torch.optim as optim
optimizer = torch.optim.Adam(model.parameters(), lr=0.01) # define learning rate
loss_fn = nn.NLLLoss() # define loss function

epochs = 100 # nueral network will learn 100 times

# train the nueral network
for epoch in range(epochs):
  optimizer.zero_grad()
  Ypred = model(Xtrain_)
  loss = loss_fn(Ypred,  ytrain_)
  loss.backward()
  optimizer.step()
  print('Epoch',epoch, 'loss',loss.item())

list(model.parameters())

torch.from_numpy(sc.transform(np.array([[40,20000]]))).float()

y_cust_20_40000 = model(torch.from_numpy(sc.transform(np.array([[40,20000]]))).float())
y_cust_20_40000

_, predicted_20_40000 = torch.max(y_cust_20_40000.data,-1)
predicted_20_40000

y_cust_42_50000 = model(torch.from_numpy(sc.transform(np.array([[42,50000]]))).float())
y_cust_42_50000

_, predicted_42_50000 = torch.max(y_cust_42_50000.data,-1)
predicted_42_50000

torch.save(model,'customer_buy.pt')

!ls

restored_model = torch.load('customer_buy.pt')

y_cust_20_40000 = restored_model(torch.from_numpy(sc.transform(np.array([[40,20000]]))).float())
y_cust_20_40000

_, predicted_20_40000 = torch.max(y_cust_20_40000.data,-1)
predicted_20_40000

model.state_dict()

torch.save(model.state_dict(),'customer_buy_state_dict')

!ls

new_predictor = Net()

y_cust_20_40000 = new_predictor(torch.from_numpy(sc.transform(np.array([[40,20000]]))).float())
y_cust_20_40000

!zip -r customer_buy_state_dict.zip customer_buy_state_dict

!ls

from google.colab import files

files.download('customer_buy_state_dict.zip')

