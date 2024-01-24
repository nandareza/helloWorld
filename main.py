import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from imblearn.over_sampling import SMOTE
from collections import Counter
smote = SMOTE()

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


print('-----------------------------------------------------------------------')

#Fscore and pvalue
f_p_values=chi2(X_train,y_train)

print(f_p_values)

p_values=pd.Series(f_p_values[1])
p_values.index=X_train.columns

print('-----------------------------------------------------------------------')

print(p_values.sort_values(ascending=False))


# Set the significance level
p_values = [6.480780e-01, 8.971951e-02, 3.542209e-03, 6.813234e-05, 4.867768e-05, 3.041257e-05, 2.161149e-05, 1.284051e-16]
alpha = 0.05


significant_variables = []
for i, p_value in enumerate(p_values):
    if p_value < alpha:
        significant_variables.append(i)

# Print the indices of significant variables
print("Indices of significant variables:", significant_variables)


#selected_columns = ['Education', 'City', 'PaymentTier', 'Age', 'Gender', 'EverBenched', 'LeaveOrNot']
file_path = 'C:/Users/Nanda Reza/output.csv'
#df[selected_columns].to_csv(file_path,index=False)

#Using SMOTE
df = pd.read_csv('output.csv')


X_train, X_test, y_train, y_test = train_test_split(df[['Education','City','PaymentTier','Age','Gender','EverBenched']],
                                                df['LeaveOrNot'],test_size=0.3,random_state=100)

X_train_smote, y_train_smote = smote.fit_resample(X_train.astype('float'),y_train)

# Convert the oversampled data to a new DataFrame
df_oversampled = pd.DataFrame(data=X_train_smote, columns=X_train.columns)
df_oversampled['LeaveOrNot'] = y_train_smote

print("Before SMOTE : " , Counter(y_train))
print("After SMOTE : " , Counter(y_train_smote))
print(df_oversampled.tail())
#suffle data frame rows
df = df_oversampled.sample(frac = 1)
print(df.tail())
# Save the oversampled DataFrame to a new CSV file
df.to_csv('output_oversampled.csv', index=False)
