#question1
import pandas as pd
import numpy as np

d={'name':pd.Series(['nikhil','madhav','abhay','tanya']),
   'age':pd.Series([20,19,20,15]),
   'mail':pd.Series(['asdf@gmail.com','qwerty@gmail.com','zxcvb@gmail.com','poiuy@gmail.com']),
   'phoneno':pd.Series([8146394427,1234567890,4567890123,9876512340])}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)

#question2

df=pd.read_csv('question2-20.csv')
print(df.head(5))
print(df.head(10))
print("mean",df.mean)
print("describe",df.describe())
print(df.tail(10))
print("LOCATION")
print(df['Location'])

print(df['Location'].describe)

print("MINTEMP")
print(df['MinTemp'].describe())
print("Count ",df['MinTemp'].count())
print("Min ",df['MinTemp'].min())
print("Var ",df['MinTemp'].var())
print("Max ",df['MinTemp'].max())
print("Mean ",df['MinTemp'].mean())
print("Median ",df['MinTemp'].median())
print("Mode ",df['MinTemp'].mode())