import os
import pandas as pd
import numpy as np
import re

# #FILTERING DATA
filename = os.path.join(os.path.dirname(__file__),'titanic.csv')

# #SELECTING A SUBSET OF A DATAFRAME
# # age = pd.read_csv(filename)
# # print(age['Age'].head(10))

# #SELECTING MULTIPLE COLUMNS
# # age_sex = pd.read_csv(filename)
# # print(age_sex[['Age','Sex']])

# # #Filtering based on a single criterion
data = pd.read_csv(filename)
# # younger_than_15 = data['Age'] < 15
# # print(younger_than_15.head(10))

# #Filtering based on a single criterion with all columns
# # data = pd.read_csv(filename)
# # younger_than_15 = data['Age'] < 15 #retruns Pandas series with Boolean values 
# # younger_than_15 = data[data['Age'] < 15] #retruns selected data with all columns
# # print(younger_than_15.head(10))

# #Selecting a subset of rows and columns combined
# # younger_than_15 = data.loc[data['Age'] < 15, ['Sex','Survived']]
# # print(younger_than_15)

# #Filtering based on two criteria using bitwise operators & (AND)
# # seventy_year_olds = data[(data['Age'] >= 70) & (data['Age'] <= 79)]
# # print(seventy_year_olds)

# # seventy_year_olds = data[data['Age'].between(70,79)]
# # print(seventy_year_olds)

# #Filtering based on two criteria using bitwise operators & (AND) (USING DIFF COLUMNS)
# # sixty_year_old_females = data[data['Age'].between(60,69) & (data['Sex'] == 'female')]
# # print(sixty_year_old_females)

# # | = or
# #Filtering based on two criteria using the bitwise operator |(or) (SAME COLUMN)

# # second_n_third_classes = data[(data['Pclass'] == 2) | (data['Pclass'] == 3)]
# # print(second_n_third_classes.head(20))

# # FILTERING BASED ON MAXIMUM & MINIMUM VALUES
# # data['Fare'].idxmax() #retruns max values
# # data['Fare'].idxmin() #retruns min value

# # max_min_fare = data.loc[[data['Fare'].idxmax(),data['Fare'].idxmin()]]
# # print(max_min_fare)

# # PRACTICE
# #1. Find all survivors

# # survived = data[(data['Survived'] == 1) & (data['Name'])]
# # print(survived)

# #2. Find all deceased
# # deceased = data[(data['Survived'] == 0) & (data['Name'])]
# # print(deceased)

# #3. Find all pass that were traveling alone
# # tarveling_alone = data[(data['SibSp'] == 0) & (data['Parch'] == 0) & (data['Name'])]
# # print(tarveling_alone)

# #4. Find all pass traveling with spouse/relatives

# # traveling_with_spouse_relative = data[(data['Parch'] != 0)]
# # print(traveling_with_spouse_relative)

# #5. Find all male frist-class passengers who were traveling alone

# # single_first_class_male = data[(data['Pclass'] == 1) & (data['Sex'] == 'male') & (data['SibSp'] == 0) & (data['Parch'] == 0) & (data['Name'])]
# # print(single_first_class_male)

# #6. FInd all female thrid-class pass who were traveling alone
# # single_third_class_female = data[(data['Pclass'] == 3) & (data['Sex'] == 'female') & (data['SibSp'] == 0) & (data['Parch'] == 0) & (data['Name'])]
# # print(single_third_class_female)

# #7. FInd all first-class passengers who paid less than $100 for their ticket

# # first_class_less_than_100 = data[(data['Pclass'] == 1) & (data['Fare'] < 100)]
# # print(first_class_less_than_100)

# #8. Find number survivors per port of embarkstion, and where the most 1st class passegers came from

# # survivors_per_port_S = data[(data['Embarked'] == 'S')  & (data['Name'])]
# # print(f'Port S: {len(survivors_per_port_S)}')

# # survivors_per_port_Q = data[(data['Embarked'] == 'Q')  & (data['Name'])]
# # print(f' Port Q: {len(survivors_per_port_Q)}')

# # survivors_per_port_C = data[(data['Embarked'] == 'C')  & (data['Name'])]
# # print(f' Port C: {len(survivors_per_port_C)}')



# #9. FInd number of survivors per class 
# # survivors_per_first_class = data[(data['Pclass'] == 1) 
# # print(len(survivors_per_first_class))

# # survivors_per_second_class = data[(data['Pclass'] == 2)
# # print(len(survivors_per_second_class))

# # survivors_per_third_class = data[(data['Pclass'] == 3) & (data['Sex'] == 'female') & (data['SibSp'] == 0) & (data['Parch'] == 0) & (data['Name'])]
# # print(len(survivors_per_third_class))

# #10. Find all the passengers that were travelling with a spouse only.
# # spouse_only = data[(data['Survived'] == 0) & (data['Name']) & (data['SibSp'] == 1) & (data['Parch'] == 0)]
# # print(spouse_only)

# #CLEANING DATA
# #RETRIEVING TECHNICAL INFO ON A DATASET
filename = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(filename)

# #df.info()
# #print(df.describe())

# #print(df.isnull().sum())

# df.fillna(value=None,method=None,axis=None,inplace=True|False,limit=None,downcast=None)
# #value: values to be replaced
# #method: optional
# #axis: row = 1 column = 0
# #inplace: creates new dataframe if False
# #limit: max number of values to fill (used with method)
# #downcast: a dict of values used to fill specific data types


# #Replacing NaN values with 0
# df.fillna(value=0,inplace=True)
# print(df)
# df['Cabin'].fillna(value=0,inplace=True)
# print(df)

#Replacing Multiple Values iwth the same value
#students = {
            # 'Name':['Jay Walker','Chris P. Bacon','Anita Kiss', 'Carrie Oakey', 'Ben Kroberry'],
            # 'Course':['Python','JavaScript','Go','Web Dev','java'],
            # 'Grades':[98,90,100,89,92]
#}
#df = pd.DataFrame(students,columns=['Name','Course','Grades'])
# print(df)

# #Using replace()
# df['Course'] = df['Course'].replace(to_replace='Go',value='R')
# print(df)

# df.Course = df.Course.replace('java','C++')
# print(df)

# #Using loc[]
# df.loc[df.Course == 'C++','Course'] = 'PHP'
# print(df)

# #Specifiying column name and value
# df.Course[df.Course == 'PHP'] = 'PostgreSQL'
# print(df)

# #Replacing Multiple values with different values
# df['Grades'] = df['Grades'].replace(to_replace=[89,92],value=[98,29])
# print(df)

#Replacing a single value
# df.loc[(df.Name == 'Jay Walker') & (df.Course == 'Python') & (df.Grades == 98), 'Course' ] = 'Fortran'
# print(df)

df['Cabin'].fillna(value=0,inplace=True)

#Replacing disarrayed values with a singl value
# df.Cabin = pd.to_numeric(df.Cabin,errors='coerce').fillna(1).astype('int')
# print(df)

#CALCULATING THE MEAN
# CALC THE MEAN ON A SINGLE COLUMN
age_mean = df['Age'].mean()
print('Age Mean: {:.2f}'.format(age_mean))

#CALC THE MEAN ON MULTIPLE COLUMNS
age_fare = df[['Age','Fare']].mean()
print('Age mean: {:.2f}\nFare Mean: {:.2f}'.format(age_fare['Age'],age_fare['Fare']))

# #Calculate the mean from each row
# row_mean = df.mean(axis=1)
# print(row_mean)

#Calculating the STD
age_std = df['Age'].std()
print('Age std: {:.2f}'.format(age_std))

#Producing random age values
random_ages = np.random.randint(age_mean-age_std,age_mean+age_std)
print(random_ages)

#Storing new random ages to variable
new_age = df.Age.fillna(random_ages)

# #Pass new values to the table
# df['Age'].fillna(new_age,inplace=True)
# print(df.head(30))

find_nan = df['Age'].isna()
#print(find_nan.head(30))
print(find_nan.sum())

random_ages = np.random.randint(age_mean-age_std,age_mean+age_std,find_nan.sum())
print(random_ages)

random_ages = df.Age.fillna(pd.Series(random_ages,index=df.index[find_nan]))
print(random_ages.head(30))

df['Age'] = df.Age.fillna(pd.Series(random_ages, index=df.index[find_nan]))
print(df.head(30))

#clean the data and the steps to take to do that
#these are the steps to begin wiith on every dataset
#1. look for nan values and repalce
#2. find the mean
#3. Creating actual data for null values
#4. combine columns

#COMBINING COLUMNS
#without a function
df['Family Size'] = df['SibSp'] + df['Parch']
print(df.head(10))

#with a function
def create_fam_col(df):
    return df['SibSp'] + df['Parch']
df['Family Size'] = create_fam_col(df)
print(df.head(10))

#with a function
# df['Is Alone'] = 0
# df.loc[df['Family Size']==0,'Is Alone'] = 1
# print(df.head(10))

#with function
def create_is_alone_col(df,colname):
    def is_alone(a):
        if a == 0:
            return 1
        else:
            return 0
    return df[colname].apply(is_alone)
df['Is Alone'] = create_is_alone_col(df,'Family Size')
print(df.head(10))

#Dr. - Doctor
#Rev. - Clerical
#Master. - Scholar
#Major.,Col.,Capt. - Military
#Mr., Mrs., Ms., Miss. - Commoners
#Don.,Sir.,Mme.,Mlle.,Lady.,Countess.,Jonkeer - Nobility

def search_title(x):
    match x:
        case 'Rev.':
            return 'Clerical'
        case 'Master.':
            return 'Scholar'
        case 'Dr.':
            return 'Doctor'
        case 'Major.' | 'Col.' | 'Capt.':
            return 'Military'
        case 'Mr.' | 'Mrs.' | 'Ms.' | 'Miss.':
            return 'Commoner'
        case 'Don.' | 'Sir.' | 'Mme.' | 'Mlle.' | 'Lady.' | 'Countess.' | 'Jonkheer.':
            return 'Nobility'

#lambda parameteres : expression

df['Title'] = df['Name'].apply(lambda x:re.search('([A-Za-z]+)\.',x).group())
df['Title'] = df['Title'].apply(lambda x:search_title(x))
print(df.to_string)


#Find how many passengers are there based on title
clerical = df[df['Title']  == 'Clerical']
print('Clergy:', len(clerical))

scholar = df[df['Title'] == 'Scholar']
print('Scholar:', len(scholar))

doctor = df[df['Title'] == 'Doctor']
print('Doctor:' ,len(doctor))

military = df[df['Title'] == 'Military']
print('Military:',len(military))

commoner = df[df['Title'] == 'Commoner']
print('Commoner:',len(commoner))

nobility = df[df['Title'] == 'Nobility']
print('Nobility:',len(nobility))


# #Using replace() method
# df['Sex'] = df.Sex.replace({'male':1, 'female': 0})
# print(df)

#Using a function
def change_sex_values(df,colname):
    def sex(x):
        if x == 'male':
            return 1
        else:
            return 0
    return df[colname].apply(sex)
df['Numerical Sex'] = change_sex_values(df,'Sex')
print(df)

#replace or function 
# C =1 Q=2 S=3

df['Embarked'] = df.Embarked.replace({'C':1,'Q':2,'S':3})
print(df)

def change_embarked_values(df,colname):
    def embark(x):
        if x == 'C':
            return 1
        elif x == 'Q':
            return 2
        else:
            return 3
    return df[colname].apply(embark)
df['Port Number'] = change_embarked_values(df,'Embarked')
print(df)

#Removing DUPLICATES
fruit_list = [['Apple', 0.45], ['Banana',2.43],['Pineapple',3.99],['Apple',0.45]]
fruits = pd.DataFrame(fruit_list,columns=['Name','Price'])
print(fruits.duplicated())

fruits.drop_duplicates(inplace=True)
print(fruits)

#Dropping UNNECESSARY COLUMNS
drop_columns_list = ['PassengerId','Sex','Embarked','SibSp','Parch','Ticket']
final_dataset = df.drop(drop_columns_list,axis=1)
print(final_dataset)

final_dataset.to_csv('final_dataset.csv')

# print(df.isna().sum())