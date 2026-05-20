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