#INSPECT THE DATA, REMOVE IRRELEVANT COLUMNS/FEATURES, CLEAN DATA IN DATE COLUMN
import pandas as pd
import re
df = pd.read_csv('./BL_books.csv')
df.columns = ['Identifier','Edition Statement','Place of Publication','Date of Publication','Publisher','Title',
                'Author','Contributors','Corporate Author','Corporate Contributors','Former owner',
                'Engraver','Issuance type','Flickr URL','Shelfmarks']

#Inspect the data and describe any issues observed
print('Number of instances = %d' % (df.shape[0]))
print('Number of attributes = %d' % (df.shape[1]))
print('Number of missing values:')
for col in df.columns:
    print('\t%s: %d' % (col,df[col].isna().sum()))

#Remove fields that refer to internal processes at the British Library 
df = df.drop(['Corporate Author','Corporate Contributors','Former owner','Engraver','Issuance type','Shelfmarks'],
             axis=1)

#Clean data in column Date of Publication
df['Date of Publication'] = df['Date of Publication'].str.extract(r'(\d{4})')
df.head() #default is to show 5 rows, we can change it by using data.head(2) to show 2 rows



#DATA CLEANING TO REPLACE NAN VALUES WITH THE MEAN OF THE FIELD & REPLACE CATEGORICAL LABELS WITH NUMERICAL LABELS
import pandas as pd

#Load the CSV file country-income.csv which includes both numerical and categorical values
df = pd.read_csv('./country-income.csv')
df.columns = ['Region','Age','Income','Online Shopper']

#Print the number of missing values for each attribute
print('Number of missing values:')
for col in df.columns:
    print('\t%s: %d' % (col,df[col].isna().sum()))
    
#Data cleaning in order to replace any NaN values with the mean of the value for a given field
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Income'] = df['Income'].fillna(df['Income'].mean())

#Replace any categorical labels with numerical labels

#Print the number of regions and their counts in the dataset
noOfRegions = df['Region'].value_counts()
print('\nNumber of regions: \n{}'.format(noOfRegions))

#country code numbers have been chosen to map the region to numerical value
#for the online shopper as Yes or No, 1 and 0 has been chosen respectively
map_dict = {'Region':{'India':91,'Brazil':55,'USA':1},'Online Shopper':{'Yes':1,'No':0}} 
df.replace(map_dict,inplace=True)

#Display the resulting dataset
df


#PLOT SCATTERPLOTS OF SHOE SIZE VX MALE&FEMALE SUBJECTS, COMPUTE PEARSON'S CORRELATION COEFFICIENT TO INFER THE RELATIONSHIP BETWEEN THE FEATURES
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Load the CSV file shoesize.csv
df = pd.read_csv('./shoesize.csv')
df.columns = ['Index','Gender','Size','Height']

df_female = df.loc[df['Gender'] == 'F']
df_male   = df.loc[df['Gender'] == 'M']

#Plot the scatterplots of shoe size versus height for female 
plt.scatter(df_female['Size'], df_female['Height'],color='red')
plt.title("Shoe size versus height for Female")
plt.xlabel("Shoe size")
plt.ylabel("Height")
plt.show()

#Compute the Pearson's correlation coefficient of shoe size versus height for female 
cor_coef_female,p_value_female = stats.pearsonr(df_female['Size'], df_female['Height'])
print('For female Pearson"s correlation coefficient is {}'.format(cor_coef_female))

#Plot the scatterplots of shoe size versus height for male
plt.scatter(df_male['Size'], df_male['Height'],color='blue')
plt.title("Shoe size versus height for Male")
plt.xlabel("Shoe size")
plt.ylabel("Height")
plt.show()

#Compute the Pearson's correlation coefficient of shoe size versus height for male
cor_coef_male,p_value_male = stats.pearsonr(df_male['Size'], df_male['Height'])
print('For male Pearson"s correlation coefficient is {}'.format(cor_coef_male))
