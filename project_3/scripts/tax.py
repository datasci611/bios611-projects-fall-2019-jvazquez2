# This python file will create the data for the first plot

# Importing packages 
import numpy as np
from scipy import stats
import scipy
import pandas as pd
import sys
import math

# Import Data Tax Data 
df = pd.read_csv(r'../data/IRS.csv')
df = df[df.Net >= 0]
data = df['Net']


# Counting the first digit
def count_first_digit(data_str):
    mask=df[data_str]>1.
    data=list(df[mask][data_str])
    for i in range(len(data)):
        while data[i]>10:
            data[i]=data[i]/10
    first_digits=[int(x) for x in sorted(data)]
    unique=(set(first_digits))#a list with unique values of first_digit list
    data_count=[]
    for i in unique:
        count=first_digits.count(i)
        data_count.append(count)
    total_count=sum(data_count)
    data_percentage=[(i/total_count)*100 for i in data_count]
    return  total_count,data_count, data_percentage

total_count, data_count_pre, data_percentage_pre = count_first_digit("Net")

# In this case data_count_pre and data_percentage_pre have the format of [1,3,4,5,6,8]. 
# Need to add zeros for 2, 7, 9 
data_count = []
data_percentage = []
numbers = []
j = 0
for i in range(1,10):
    numbers.append(i)
    if i in (2,7,9):
        data_count.append(0)
        data_percentage.append(0)
    else:
        data_count.append(data_count_pre[j])
        data_percentage.append(data_percentage_pre[j])
        j = j+1
            
            
# Benford's Law percentages for leading digits 1-9
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

# Get the expected number of counts
expected_counts=[round(p * total_count / 100) for p in BENFORD]

# Observed vs Expected  
chi_square_stat = 0  # chi square test statistic
for data, expected in zip(data_count,expected_counts):
    chi_square = math.pow(data - expected, 2)
    chi_square_stat += chi_square / expected

print("\nChi-squared Test Statistic = {:.3f}".format(chi_square_stat))
print("Critical value at a P-value of 0.05 is 15.51.")

print("actual counts are", data_count)
print("expected counts are", expected_counts)

# Wilxocon Rank-Sum Test
scipy.stats.mannwhitneyu(data_count,expected_counts)

# Save data and export to R-Studio to create graphs
out_tax = pd.DataFrame(columns=['Number', 'Empirical Percentage', 'Benford Distribution'])
out_tax['Number'] = numbers
out_tax['Empirical Percentage'] = data_percentage
out_tax['Benford Percentage'] = BENFORD

out_tax = pd.melt(out_tax, id_vars =['Number'], value_vars =['Empirical Percentage', 'Benford Percentage']) 

# Exporting data to folder data under projects
out_tax.to_csv('tax_data_graph.csv')
