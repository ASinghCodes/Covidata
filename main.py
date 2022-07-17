from audioop import mul
from matplotlib import style
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import scale

#Read in the data, specifically sheet 
dataSet = pd.read_excel(r'Covidata\WHO_COVID_Excess_Deaths_EstimatesByIncome.xlsx', "Deaths by year and month", usecols="A:J", skiprows=11)
#print(dataSet)
#What exists or does not exist within the dataset

info = dataSet.info()
nullInfo = dataSet.isnull()

#Lets make some terms more readable

dataSet.income.replace(['LIC', 'LMIC', 'UMIC', 'HIC'], ['Low-Income', 'Lower-Middle', 'Upper-Middle', 'High'], inplace=True)

#Now that we have cleaned up the data to be a bit more understandable, lets go for visualization
sns.set(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(10,10))
expMeanPlot = sns.histplot(data=dataSet, x= 'expected_mean', hue='year', kde=True, ax=axs[0,0], shrink=0.5)
acmMeanPlot = sns.histplot(data=dataSet, x= 'acm_mean', hue='year', kde=True, ax=axs[0,1], shrink=0.5)
excMeanPlot = sns.histplot(data=dataSet, x= 'excess_mean', hue='year', kde=True, ax=axs[1,0], shrink=0.5)
cExcMeanPlot = sns.histplot(data=dataSet, x= 'cumul_excess_mean', hue='year', kde=True, ax=axs[1,1], shrink=0.5)
plt.show()

#Lets look at the cumulative impact of excess deaths by country
sns.set(style="darkgrid")
plt.figure(figsize=(10,10))
plt.title('Excess mean deaths by country income due to COVID-19 (Cumulative)')
excMeanIncPlot = sns.histplot(data=dataSet, x= 'excess_mean', hue='income', multiple='dodge', kde=True, shrink=0.5)
plt.show()

sns.set(style="darkgrid")
plt.figure(figsize=(10,10))
plt.title('Excess mean deaths by month due to COVID-19 (Cumulative)')
excMeanMonPlot = sns.barplot(y=dataSet['excess_mean'], x=dataSet['month'])
plt.show()