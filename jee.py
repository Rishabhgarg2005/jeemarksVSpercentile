import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("jee_marks_percentile_rank_2009_2026.csv")
print(data.head())
print(data.isna().sum())
data =data.drop(columns ="Total_Candidates")
print(data.head())
data["Year"] = data["Year"].astype("int")
data["Percentile"] = data["Percentile"].astype("float")
plt.figure(figsize =(10,120))
sns.lineplot(x ="Year",y ="Percentile",data =data)
plt.title("Percentile Rank of JEE Marks Over the Years")
plt.xlabel("Year")
plt.ylabel("Percentile Rank")
plt.show()
X =data.drop(colums ="Percentile")
y =data["percentile"]
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=123)
