#Create a scatter plot for the pair of distinct numerical features with the highest correlation
# Calculate the coorelation for the dataframe
corr=df.corr()
#Find the atrributes with highest correlation
df_highest_correlation = corr[corr>=0.8]
df_highest_correlation 

sns.scatterplot(y='total_phenols', x='flavanoids', data=df)
plt.show()


#Exclude the categorical feature, standardize the numerical features, and 
#display a projection obtained by multidimensional scaling. 
#Color the points by the categorical feature. 
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS
import numpy as np

#Sort the data by target
df_sorted = df.sort_values(by='target', ascending=True)
target_sorted = df_sorted['target']

#Exclude the categorical feature
X = df_sorted.drop(columns='target').to_numpy()

#Standardize the numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Display multidimensional scaling project based on colour
embedding = MDS(n_components=2)
    
Xp = embedding.fit_transform(X)
df_projection = pd.DataFrame({'x': Xp[:, 0], 'y': Xp[:, 1],
                              'target': target_sorted})

df_projection
#The attribute hue add colour to the scatter plot based to segregate the feature
sns.scatterplot(x='x', y='y', hue='target',data=df_projection)

#To show the lengends for various colours in the scatterplot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
