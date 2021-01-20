# Loading dataset (http://roycekimmons.com/tools/generated_data)
import pandas as pd
import numpy as np

df = pd.read_csv('graduation_rate.csv')
#find and show the entire rows that correspond to the outliers regarding parental income 
#whose parents have a master's degree
df_copy = df[df['parental level of education'] == "master's degree"].sort_values(by='parental income')
data_mean, data_std = df_copy.mean(), df_copy.std()

# identify outliers using the interquartiles 
# (chose this method to be able to validate the data from the box plots in the section 1 provided)
q1 = df_copy.quantile(0.25)
q3 = df_copy.quantile(0.75)
iqr = q3 - q1

#fencing is being used to identify lower bound of the outlier by chooing a constant of 1.5 
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr)

# identify outliers
df_lower_bound = df[(df['parental income'] < lower_bound['parental income']) 
                    & (df['parental level of education'] == "master's degree")]
df_upper_bound = df[(df['parental income'] > upper_bound['parental income']) 
                    & (df['parental level of education'] == "master's degree")]


display(pd.concat([df_lower_bound,df_upper_bound]))
