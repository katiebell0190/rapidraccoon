
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


# # print(get_dataset_names())

# iris = sns.load_dataset('iris')
# # print(iris.info())
# # print(iris.describe())

# print(iris.species.unique())

# #Load data set using load_dataset(0_function)
# iris = sns.load_dataset('iris')
# #Use option perameter
# sns.set(style='darkgrid')
# #Choose a plot type (take 3 params: x,y)
# sns.barplot(data=iris,x='species',y='petal_length')
# plt.show()
# sns.relplot(data=iris,x='species',y='petal_length')
# plt.show()

# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid')
# sns.relplot(data=penguins,x='bill_length_mm',y='flipper_length_mm',
#                 height=4, aspect=1,hue='sex',row='island',col='species')
# plt.show()


# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid')
# sns.displot(data=penguins,x='bill_length_mm',hue='species',
#                 height=4, aspect=1)
# plt.show()

#CATPLOT()
# 
# penguins = sns.load_dataset('exercise')
# print(penguins)
# sns.set(style='darkgrid')
# sns.catplot(data=penguins,x='kind',y='pulse', hue='kind',
#                 height=4, aspect=1)
# plt.show()

# #AXES - LEVEL PLOTS
# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid', rc={'figure.figsize':(3.3)})
# sns.scatterplot(data=penguins,x='species',y='island')
# plt.show()

# #histplot()
# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid', rc={'figure.figsize':(3,3)})
# sns.histplot(data=penguins,x='species',y='island')
# plt.show()

# #kdeplot()
# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid', rc={'figure.figsize':(3,3)})
# sns.kdeplot(data=penguins,x='bll_length_mm',hue = 'species')
# plt.show()

# #kdeplot()
# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set(style='darkgrid', rc={'figure.figsize':(3,3)})
# sns.ecdfplot(data=penguins,x='bill_length_mm',hue = 'species')
# plt.show()

# #rugplot()
# tips= sns.load_dataset('tips')
# print(tips)
# sns.set(style='darkgrid', rc={'figure.figsize':(4,4)})
# sns.rugplot(data=tips,x='tip')
# plt.show()

# #swarmplot()
# exercise= sns.load_dataset('exercise')
# print(exercise)
# sns.set(style='darkgrid', rc={'figure.figsize':(4,4)})
# sns.boxplot(data=exercise,x='kind',y='pulse', dodge=True)
# plt.show()

# #boxplot()
# exercise= sns.load_dataset('exercise')
# print(exercise)
# sns.set(style='darkgrid', rc={'figure.figsize':(4,4)})
# sns.boxplot(data=exercise,x='kind',y='pulse', dodge=True)
# plt.show()

# #sviolinplot()
# exercise= sns.load_dataset('exercise')
# print(exercise)
# sns.set(style='darkgrid', rc={'figure.figsize':(4,4)})
# sns.violinplot(data=exercise,x='kind',y='pulse', dodge=True)
# plt.show()

# #VISUALIZING THE TITANIC DATASET
filename = os.path.join(os.path.dirname(__file__),'final_dataset.csv')
final_data = pd.read_csv(filename)
# print(final_data)

# #DATA CORRELATION
# data_corelation = final_data.corr()
# print(data_corelation)

# class1 = final_data['Survived'].corr(final_data['Pclass'] == 1)
# print(class1)
# class2 = final_data['Survived'].corr(final_data['Pclass'] == 2)
# print(class2)
# class3 = final_data['Survived'].corr(final_data['Pclass'] == 3)
# print(class3)


# colormap = sns.diverging_palette(230,20, as_cmap=True)
# plt.figure(figsize=(10,8))
# sns.heatmap(final_data.corr(),cmap=colormap,linewidth=.5,annot=True)
# plt.show()

#UNIVARIATE ANALYSIS
# survivals = final_data['Survived'].value_counts()
# print(survivals)

# # sns.countplot(data=final_data, x='Survived',pallette=['#476a6f','#e63946'])
# # plt.show()

colors = ['lightsteelblue','silver']
# explode = [0,0.05]
# final_data['Survived'].value_counts().plot.pie(colors=colors,shadow=True,explode=explode)
# plt.show()

#Bivariate Analysis
survived_classe = final_data.groupby(['Survived','Pclass'])['Survived'].value_counts()
print(survived_classe)

# sns.catplot(data=final_data,x='Numerical Sex',y='Fare',palette=['#476a6f','#e63946'])
# plt.show()

# sex_age = sns.catplot(data=final_data,x='Numerical Sex', y='Age',hue='Survived',col='Pclass')
# plt.show()


mix_variables = sns.relplot(data=final_data,x='Age',y='Fare',col='Pclass',row='Numerical Sex')
plt.show()