import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import seaborn as sns

def get_unique_values(df, column):
  return df[df[column].notnull()][column].unique()

def run(file):
  df = pd.read_csv(file, header=0)
  # cols = df.columns
  # print("Columns:", cols)

  df['Presence of sidewalk'] = (df['Presence of sidewalk'] == "Yes").astype(int)
  numeric_features = df.select_dtypes(include=[np.number])
  categorical_features = df.select_dtypes(include=['category'])
  print(numeric_features)
  plt.figure(figsize=(10, 10))
  sns.heatmap(numeric_features.corr(), annot=True)
  plt.show()

run("data/accident-data.csv")
