from sklearn import tree
import pandas as pd

#Read in the data, specifically sheet 
dataSet = pd.read_excel(r'Covidata\WHO_COVID_Excess_Deaths_EstimatesByIncome.xlsx', "Deaths by year and month", usecols="A:C,F:G", skiprows=11)
print(dataSet)
#Separate 