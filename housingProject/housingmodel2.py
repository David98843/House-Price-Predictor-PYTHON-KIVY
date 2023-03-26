import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split,cross_val_score, cross_val_predict
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score


#load the training data
data=pd.read_csv("Housing.csv")
X=data[[
    'area',
    'bedrooms',
    'bathrooms',

]].values

y=data['price'].values


#split the training data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2, random_state=0)

#Scale the training data
StandardScaler().fit_transform(X_train)

#validation set
c_val_x = X_test[80:,:]
c_val_y = y_test[80:]
StandardScaler().fit_transform(c_val_x)

#training the model
model=linear_model.LinearRegression().fit(X_train, y_train)

c_val = cross_val_predict(model,c_val_x,c_val_y,cv=5)

print(r2_score(c_val_y, c_val))
print(c_val[20:].astype('int'))
print(c_val_y[20:])

#save trained model
filename="housingModel2.sav"
joblib.dump(model,filename)

#predict testing data
pred=model.predict(X_test)
pred=np.array(pred).astype("int")

print(pred[0:4])
print(y_test[0:4])

print("Score Training:",model.score(X_train,y_train))
print("Score Testing:",model.score(X_test,y_test))

errors = []
for x in range(0,48):
    error = y_test[x] - pred[x]
    errors.append(error)


plt.plot(errors)
plt.grid()
plt.show()