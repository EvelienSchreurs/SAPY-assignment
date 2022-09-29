# Import pandas and numpy
import pandas as pd
import numpy as np
#%% Set working directory
import os
os.chdir('C:/Users/Evelien/Documents/Sustainability analysis in Python/data_assignment')
print("Current working directory: {0}".format(os.getcwd()))

#%% Import data
data = pd.read_csv('dataworldbankmethane.csv', skiprows = 4)

#%% Clean data
#Delete the columns where all data is missing. (years 1960-1990 and 2013-2021).
data = data.dropna(axis = 1, how = 'all')

#Delete the countries (rows) where the data from all years is missing
data = data.dropna(axis = 0, how = 'any')

#Delete columns with unnessecary data 
data= data.drop(['Indicator Name', 'Indicator Code'], axis = 1)

#%% Import metadata
metadata = pd.read_csv('metadata_country.csv')

#Throw out countries that aren't placed in an income group
metadata = metadata.dropna(subset = ['IncomeGroup'])

#%% Merging the datasets 
#Merged the two datasets on the joined column 'country code'
merged_data = pd.merge(data, metadata, on=["Country Code"]) 

#%% Making list of each seperate income group
list_high_income = merged_data.dropna()
