import os
import pandas as pd
import numpy as np

#Components of Series
#examples pd.Series(data=None,index=None,dtype=None,copy=True|False)
#data - any array or sequence ndarray, list, dict
#index - unique, same length as the data np.arrange()
#dtype - data type
#copy - copy data

#Creating series from Scratch
#s = pd.Series()
#print(s)

# #Creating a Series from List
# day = [11,8,4,7]
# calendar = pd.Series(day)
# print(calendar)

# import calendar
# year_2022 = calendar.calendar(2022)
# print(year_2022)

# month_2022 = calendar.month(2022,6)

# #Creating a series from ndarray
# data = np.array(['apple','banana','orange','kiwi'])
# s = pd.Series(data)
# print(s)

# #Creating a series from dict
# data = {'apple':0.99, 'banana':2.35,'orange':3,'kiwi':4}
# fruits = pd.Series(data)
# print(fruits)

# #Creating a Series from a scaler
# s = pd.Series(4,index = [1,2,3,4])
# print(s)

# #Creating Lables
# arr = [1,2,3,4,5]
# index = ['a','b','c','d','e']
# s = pd.Series(arr,index=index)
# print(s)

# #Accessing Items
# days = [1,2,3,4,5,6,7]
# index = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# calendar = pd.Series(days,index = index)
# print(calendar['Monday'])

# ##Accessing Items via Indices
# days = [1,2,3,4,5,6,7]
# index = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# calendar = pd.Series(days,index = index)
# print(calendar[[3,5]])

# ##Accessing a Range of items
# days = [1,2,3,4,5,6,7]
# index = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# calendar = pd.Series(days,index = index)
# print(calendar[3:6])

#Create a simple pandas series from a dict
#Create a function that takes uer input fo rthe lang
#and the program outputs the average annual salaray

# salary = {'Python': 120000, 'JavaScript': 118000, 'Java':104000, 'C#':97000, 'C++': 97000, 'Go': 93000, 'R': 93000, 'Swift':93000, 'PHP':81000}
# language = pd.Series(salary)
# #print(language)

# def anything(usr):
#     if usr in salary:
#         print('${0:,.2f}'.format(language[usr]))
#     else:
#         print('language not found.')

# anything(usr=input("enter lang: ").capitalize())

# #Creating a DataFrame
# df = pd.DataFrame()
# print(df)

# #Creating a DF from a list
# data = ['Python','JavaScript','Java','C#']
# df = pd.DataFrame(data)
# print(df)

#Creating a DF from a list of lists
# data = [['Python',12000],['JavaScript',118000],['Java',104000]]
# df = pd.DataFrame(data)
# print(df)

# #Adding Labels to DataFrame
# data = [['Python',12000],['JavaScript',118000],['Java',104000]]
# df = pd.DataFrame(data,columns=['Language','Salary'])
# print(df)

#Create a Pandas DataFrame from a list of lists for a student roster
#Include First Name, Last Name, COurse. Create an index for the student ID
#starting at 100
# student_data = [['Mike','Kroffon','Data Science'],['Aileen','Dover','Python'],['Anita','Job','WebDev'],['Claire','Voiant','CyberSecurity']]
# index = [100,101,102,103]
# df = pd.DataFrame(student_data,index=index,columns=['FirstName','LastName','Course'])
# print(df)


# #Selecting columns
# #Using a list
# student_data = [['Mike','Kroffon','Data Science'],['Aileen','Dover','Python'],['Anita','Job','WebDev'],['Claire','Voiant','CyberSecurity']]
# index = [100,101,102,103]
# df = pd.DataFrame(student_data,index=index,columns=['FirstName','LastName','Course'])
# print(df['Course'])



# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th'])
# }
# df = pd.DataFrame(data)
# print(df)

# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th'])
# }
# df = pd.DataFrame(data)
# print(df['Language'])

#Adding Columns

# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th'])
# }
# df = pd.DataFrame(data)
# df['Number of Jobs'] = pd.Series([19000,24000,29000],index=['1st','2nd','3rd'])
# print(df)

#Deleteing Columns
# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th'])
# }
# df = pd.DataFrame(data)
# df['Number of Jobs'] = pd.Series([19000,24000,29000],index=['1st','2nd','3rd'])
# print(df)
# del df['Number of Jobs']
# print(df)

#using the pop method
# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th'])
# }
# df = pd.DataFrame(data)
# df['Number of Jobs'] = pd.Series([19000,24000,29000],index=['1st','2nd','3rd'])
# print(df)
# df.pop('Salary')
# print(df)

#Selecting Rows using .loc[] - used to select data bsed on their lable

# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
#         'Number of JObs': pd.Series([19000,24000,29000], index =['1st','2nd','3rd'])        
# }
# df = pd.DataFrame(data)
# print(df.loc['1st'])

# #using the iloc[] attribute - used to select data based on index
# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
#         'Number of JOos': pd.Series([19000,24000,29000], index=['1st','2nd','3rd'])        
# }
# df = pd.DataFrame(data)
# print(df.iloc[0:2])

#adding rows

# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
#         'Number of JOos': pd.Series([19000,24000,29000], index=['1st','2nd','3rd'])        
# }
# df = pd.DataFrame(data)

# new_df = {'language':'C#','Salary':97000, 'Number of Jobs':18000}
# df.append(new_df,ignore_index=True)
# print(df)
#Adding a name = param to the series
# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
#         'Number of JOos': pd.Series([19000,24000,29000], index=['1st','2nd','3rd'])        
# }
# df = pd.DataFrame(data)

# new_df = pd.Series ({'language':'C#','Salary':97000, 'Number of Jobs':18000},name='5th')
# df.append(new_df,ignore_index=True)
# print(df)

#Deleting Rows
# data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
#         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
#         'Number of JOos': pd.Series([19000,24000,29000], index=['1st','2nd','3rd'])        
# }
# df = pd.DataFrame(data)
# print(df.drop('4th'))

#1. add a grades column
#2. add two new students
#3 Delete Mike Kroffon

# # #Selecting columns
# #Using a list
# student_data = [['Mike','Kroffon','Data Science'],['Aileen','Dover','Python'],['Anita','Job','WebDev'],['Claire','Voiant','CyberSecurity']]
# index = [100,101,102,103]
# df = pd.DataFrame(student_data,index=index,columns=['FirstName','LastName','Course'])
# df['Grades'] = pd.Series(['82','78','90','54'],index=index)
# print(df)

# student_data = [['Mike','Kroffon','Data Science'],['Aileen','Dover','Python'],['Anita','Job','WebDev'],['Claire','Voiant','CyberSecurity']]
# index = [100,101,102,103]
# df = pd.DataFrame(student_data,index=index,columns=['FirstName','LastName','Course'])
# df['Grades'] = pd.Series(['82','78','90','54'],index=index)
# new_df = {'FirstName': 'Jay','LastName':'Walker','Course':'DataScience','Grades':100}
# df.append(new_df,ignore_index=True)
# print(df)

# # data = {'Language':pd.Series(['Python','JavaScript','Java'],index=['1st','2nd','3rd']),
# #         'Salary': pd.Series([120000,118000,104000,97000],index=['1st','2nd','3rd','4th']),
# #         'Number of JOos': pd.Series([19000,24000,29000], index=['1st','2nd','3rd'])        
# # }
# # df = pd.DataFrame(data)

# # new_df = {'language':'C#','Salary':97000, 'Number of Jobs':18000}
# # df.append(new_df,ignore_index=True)
# # print(df)

#Loading and Printing CSV Files
filename = os.path.join(os.path.dirname(__file__),'titantic.csv')