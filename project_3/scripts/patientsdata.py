# Importing packages 
import numpy as np
from scipy import stats
import scipy
import pandas as pd
import sys
import math

# Import Data
my_client_original = pd.read_csv("https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project2_2019/CLIENT_191102.tsv", sep = '\t')
my_disability_entry_original = pd.read_csv("https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project2_2019/DISABILITY_ENTRY_191102.tsv", sep = '\t')
my_disability_exit_original = pd.read_csv("https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project2_2019/DISABILITY_EXIT_191102.tsv", sep = '\t')

# Keep only variables of interesta and merge all datasets
my_client = my_client_original[['Client ID', 'Client Age at Entry', 'Client Age at Exit', 'Client Gender', 'Client Primary Race', 'Client Ethnicity']]
my_disability_entry = my_disability_entry_original[['Client ID','Disability Determination (Entry)', 'Disability Type (Entry)']]
my_disability_entry.rename(columns = {'Disability Type (Entry)':'Disability Type'}, inplace = True)
my_disability_exit = my_disability_exit_original[['Client ID','Disability Determination (Exit)', 'Disability Type (Exit)']] 
my_disability_exit.rename(columns = {'Disability Type (Exit)':'Disability Type'}, inplace = True)

# Merge data by client ID
my_disability = pd.merge(my_disability_entry, my_disability_exit, on=['Disability Type','Client ID'], how = 'right')
my_disability.drop_duplicates(keep=False,inplace=True)

# Flag those patients who got a disability while at the UMD
my_disability['GotDisability'] = 0
my_disability.GotDisability[(my_disability['Disability Determination (Entry)'] == 'No (HUD)') & (my_disability['Disability Determination (Exit)'] == 'Yes (HUD)')] = 1
my_disability.mean()

#Making a subset of those who got a disability 
my_disability = my_disability[my_disability.GotDisability == 1]
my_disability.sort_values(by=['Client ID'], ascending=True)

#Getting the socio-demographic characteristics of patients
my_patients = pd.merge(my_disability, my_client, on = 'Client ID', how = 'left')
my_patients.to_csv('patients_data_graph.csv')
