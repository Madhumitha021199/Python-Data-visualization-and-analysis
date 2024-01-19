import pandas as pd 
pd
df=pd.read_csv(r"C:/Users/U6070507/OneDrive - Clarivate Analytics/Desktop/PYTHON/smartphones - smartphones.csv")
print(df)
df.info()
df.duplicated()
df.ndim
df.pivot_table
df.columns
df.isna().sum()
df['model'].value_counts()
df['price'].value_counts()
df['ram'].value_counts()
df['battery'].value_counts()
import matplotlib.pyplot as plt
import seaborn as sns
d=df['price'].value_counts().plot(kind='box')
plt.xlabel('model')
plt.ylabel('price')
plt.show()
d=df['price'].value_counts().plot(kind='bar', color='green')
plt.xlabel('model')
plt.ylabel('price')
plt.title('Prices of Different Smartphones')
plt.show()
plt.show()
