# -*- coding: utf-8 -*-
"""verimaden.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rl05gQ7EHLRWnVGFs8u--7dPNiIKXqF5
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df=pd.read_csv('/content/drive/MyDrive/student-mat.csv')
of=pd.read_csv('/content/drive/MyDrive/student-mat.csv')

df

df.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

df['average_grade']=(df['G1']+df['G2']+df['G3'])/3
of['average_grade']=(df['G1']+df['G2']+df['G3'])/3

df=df.drop(['G1','G2','G3'],axis=1)

sns.barplot(x=df['school'],y=df['average_grade'],data=df)

sns.barplot(x=df['sex'],y=df['average_grade'],data=df)

sns.barplot(x=df['age'],y=df['average_grade'],data=df)

sns.barplot(x=df['address'],y=df['average_grade'],data=df)

sns.barplot(x=df['famsize'],y=df['average_grade'],data=df)

sns.barplot(x=df['Pstatus'],y=df['average_grade'],data=df)

sns.barplot(x=df['Fedu'],y=df['average_grade'],data=df)

sns.barplot(x=df['Medu'],y=df['average_grade'],data=df)

sns.barplot(x=df['Mjob'],y=df['average_grade'],data=df)

sns.barplot(x=df['Fjob'],y=df['average_grade'],data=df)

sns.barplot(x=df['studytime'],y=df['average_grade'],data=df)

sns.countplot(x=df['studytime'])

sns.barplot(x=df['activities'],y=df['average_grade'],data=df)

sns.barplot(x=df['health'],y=df['average_grade'],data=df)

sns.barplot(x=df['freetime'],y=df['average_grade'],data=df)

sns.barplot(x=df['internet'],y=df['average_grade'],data=df)


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in list(df.columns):
    df[i]=le.fit_transform(df[i])

df['average_grade']=of['average_grade']
of=of.drop(['average_grade'],axis=1)

of.head(5)

df.head(5)

y=df['average_grade']
x=df.drop(['average_grade'],axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
list_models=[]
list_scores=[]
list_errors=[]
lr=LinearRegression()
lr.fit(x_train,y_train)
pred_1=lr.predict(x_test)
score_1=r2_score(y_test,pred_1)
error_1=mean_squared_error(y_test,pred_1)
print("R2 score: "+str(score_1))
print("mean squared error: "+str(error_1))
list_models.append('linear regression')
list_scores.append(score_1)
list_errors.append(error_1)



i=0
for value in y_test:
  print(str(i)+"."+"TEST: "+str(value)+" TAHMİN: "+str(pred_1[i]))
  i+=1

from sklearn.ensemble import RandomForestRegressor
rfg=RandomForestRegressor()
rfg.fit(x_train,y_train)
pred_2=rfg.predict(x_test)
score_2=r2_score(y_test,pred_2)
error_2=mean_squared_error(y_test,pred_2)
print("R2 score: "+str(score_2))
print("mean squared error: "+str(error_2))
list_models.append('randomforest')
list_scores.append(score_2)
list_errors.append(error_2)

i=0
for value in y_test:
  print(str(i)+"."+"TEST: "+str(value)+" TAHMİN: "+str(pred_2[i]))
  i+=1

plt.figure(figsize=(12,5))
plt.bar(list_models,list_errors,width=0.3)
plt.xlabel('regressors')
plt.ylabel('mean squared error')
plt.show()

plt.figure(figsize=(12,5))
plt.bar(list_models,list_scores,width=0.3)
plt.xlabel('regressors')
plt.ylabel('r2 score')
plt.show()

import seaborn as sns
sns.heatmap(of.corr())
#yorumlamak gerekirse G1,G2 ve G2,G3  arasında kuvvetli bi ilişki var

dataset = pd.read_csv('/content/drive/MyDrive/student-mat.csv')
dataset = dataset[['studytime', 'failures', 'Dalc', 'Walc','health','absences','traveltime',
                   'G1', 'G2', 'G3']] 
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
dataset.head(5)

#YENİ VERİ SETİ İLE
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2)

i=0
for value in y_test:
  print("TEST: "+str(value)+" TAHMİN: "+str(y_pred[i]))
  i+=1

list_models=[]
list_scores=[]
list_errors=[]

score_new1=r2_score(y_test, y_pred)
error_new1=mean_squared_error(y_test,y_pred)
print("R2 score: "+str(score_new1))
print("mean squared error: "+str(error_new1))
list_models.append('linear regression')
list_scores.append(score_new1)
list_errors.append(error_new1)

regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(x_train, y_train)

y_pred2 = regressor.predict(x_test)
np.set_printoptions(precision=2) 
i=0
for value in y_test:
  print("TEST: "+str(value)+" TAHMİN: "+str(y_pred2[i]))
  i+=1

score_new2=r2_score(y_test, y_pred2)
error_new2=mean_squared_error(y_test,y_pred2)
print("R2 score: "+str(score_new2))
print("mean squared error: "+str(error_new2))
list_models.append('randomforest')
list_scores.append(score_new2)
list_errors.append(error_new2)



plt.figure(figsize=(12,5))
plt.bar(list_models,list_errors,width=0.3)
plt.xlabel('regressors')
plt.ylabel('mean squared error')
plt.show()

plt.figure(figsize=(12,5))
plt.bar(list_models,list_scores,width=0.3)
plt.xlabel('regressors')
plt.ylabel('r2 score')
plt.show()