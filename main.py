import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2

df = pd.read_csv('Employee.csv')
#label encoding on Education
ordinal_label = {k: i for i, k in enumerate(df['Education'].unique(),0)}
df['Education'] = df['Education'].map(ordinal_label)

#label encoding on Gender
df['Gender']=np.where(df['Gender']=="Male",1,0)

#label encoding on City
ordinal_label = {k: i for i, k in enumerate(df['City'].unique(),0)}
df['City'] = df['City'].map(ordinal_label)

#label encoding on EverBenched
ordinal_label = {k: i for i, k in enumerate(df['EverBenched'].unique(),0)}
df['EverBenched'] = df['EverBenched'].map(ordinal_label)

#train Test split is usually done to avaoid overfitting
X_train, X_test, y_train, y_test = train_test_split(df[['Education','JoiningYear','City','PaymentTier','Age','Gender','EverBenched','ExperienceInCurrentDomain']],
                                                df['LeaveOrNot'],test_size=0.3,random_state=100)

print(X_train['Gender'].unique())

print(X_train.head())
#Fscore and pvalue
f_p_values=chi2(X_train,y_train)

print(f_p_values)

p_values=pd.Series(f_p_values[1])
p_values.index=X_train.columns

print(p_values)

print(p_values.sort_values(ascending=False))

#test1 = X_train,y_train


#chi2, p, dof, expected = chi2_contingency(test1)

#print("Chi-square statistic:", chi2)
#print("p-value:", p)
#print("Degrees of freedom:", dof)
#print("Expected frequencies:", expected)







