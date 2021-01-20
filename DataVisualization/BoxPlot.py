import seaborn as sns
import matplotlib.pyplot as plt

#6.3 Group observations by the categorical feature and create one box plot of alcohol for each group
plt.figure(figsize=(20,5))
df.groupby('target')
sns.boxplot(x='target', y='alcohol', data=df)
