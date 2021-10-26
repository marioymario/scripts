#!/usr/bin/env python3

# Set up environment

import math
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data

diabetes = pd.read_csv("/home/gato/DATA/pima_grupo.csv")

# Get to know the data a bit

print(diabetes.info())

print(diabetes.head())
print('--------------------------------')
print('The final variable, outcome, \nindicates whether a patient has diabetes.\
\nA 1 is a yes and a 0 is a no. \nFor ease of analysis, \nsplit the data based on this variable.')
print('--------------------------------')
# Split up the dataset
diabetes_yes = diabetes[(diabetes['outcome'] == 1)]
diabetes_yes.info()

diabetes_no = diabetes[(diabetes['outcome'] == 0)]
diabetes_no.info()
print('--------------------------------')
print('''There are nearly twice the number of patients\
\nwithout diabetes as there are with diabetes.\
\nA difference in sample size isn't an issue for\
\nan independent samples t-test. Each sample is\
\nlarge enough and should give reliable estimates,\
\nas long as the data meets the rest of your\
\nassumptions. Now, continue with the analysis.''')
print('--------------------------------')

print('--------------------------------')
print('''1. Do patients with diabetes have higher\
\ninsulin levels on average than patients without diabetes?\
\nBefore running the t-test, check whether the samples are normally distributed.\
\nI will do that both visually and through descriptive statistics.\
\nUsing matplotlib.pyplot, I will plot a histogram of each sample.\
\nSetting alpha = .5 will reduce the transparency of each histogram\
\nso that you can more easily see overlapping areas.''')
print('--------------------------------')
print('--------------------------------')
plt.hist(diabetes_yes['insulin'], alpha = .5, label = "insulin yes")
plt.hist(diabetes_no['insulin'], alpha = .5, label = "insulin no")
plt.legend(loc="upper right")
plt.show()

print('''From the histograms, it appears that this\
\ndata doesn't fit a bell curve.
To confirm, also retrieve the exact measures of skewness and kurtosis.''')
print('--------------------------------')

print(stats.describe(diabetes_yes['insulin']))
print(stats.describe(diabetes_no['insulin']))
print('--------------------------------')
print('--------------------------------')
print('Based on both the histograms and the statistics, \
it appears that the samples of this variable are not \
normally distributed. no more analysis of that variable for now.')
print('--------------------------------')
print('--------------------------------')
print('2. Do patients with diabetes have higher\
\nglucose levels on average than patients\
\nwithout diabetes?')
print('--------------------------------')

plt.hist(diabetes_yes['glucose'], alpha = .5, label = "insulin yes")
plt.hist(diabetes_no['glucose'], alpha = .5, label = "insulin no")
plt.legend(loc="upper right")
plt.show()
print('--------------------------------')
print('--------------------------------')
print('These samples look at least somewhat more normally\
\ndistributed than the previous variable. Plotting the\
\nhistogram also has another benefit: it makes it easy\
\nto spot some misleading values. The histogram has\
\nplotted some values of `0` glucose. This is a small\
\nselection of the data, so you are safe simply dropping\
\nit and proceeding with the analysis.')
print('--------------------------------')

diabetes_yes_filtered_glucose = diabetes_yes[diabetes_yes['glucose']!= 0]
diabetes_no_filtered_glucose = diabetes_no[diabetes_no['glucose']!= 0]

plt.hist(diabetes_yes_filtered_glucose['glucose'], alpha = .5, label = "insulin yes")
plt.hist(diabetes_no_filtered_glucose['glucose'], alpha = .5, label = "insulin no")
plt.legend(loc="upper right")
plt.show()

print('The histogram looks cleaner now! But the\
\ndistributions are still questionably normal.\
\nSo get the skewness and kurtosis as well:')

print(stats.describe(diabetes_yes_filtered_glucose['glucose']))
print(stats.describe(diabetes_no_filtered_glucose['glucose']))
print('--------------------------------')
print('These results are workable!\
\nBecause the data meets the assumptions,\
\nI can proceed to the t-test.\
\nWe will use ttest_ind() from\
\nscipy.stats. The two arguments will be the\
\ntwo arrays representing the glucose levels\
\nof patients with and without diabetes')
print('--------------------------------')
print('--------------------------------')
print(stats.ttest_ind(diabetes_yes_filtered_glucose['glucose'], diabetes_no_filtered_glucose['glucose']))
print('--------------------------------')
print('--------------------------------')
print('We reject the Null hipotesis from both of these results:\
\nthe T-statistics is greater than 1.96\
\nand the p value is lesser than 0.05')
print('--------------------------------')
print('There the p-value *100% chances of observing a\
\ndifference as large as what is observed, even if the\
\ntwo population means are identical (the null hypothesis is true\
\nand our p-value is tinny tinny')
print('--------------------------------')
print('--------------------------------')
print('Now I"m going to calculate the confidence\
/ninterval at 95%:')
print('--------------------------------')
def get_95_ci(array_1, array_2):
    sample_1_n = array_1.shape[0]
    sample_2_n = array_2.shape[0]
    sample_1_mean = array_1.mean()
    sample_2_mean = array_2.mean()
    sample_1_var = array_1.var()
    sample_2_var = array_2.var()
    mean_difference = sample_2_mean - sample_1_mean
    std_err_difference = math.sqrt((sample_1_var/sample_1_n)+(sample_2_var/sample_2_n))
    margin_of_error = 1.96 * std_err_difference
    ci_lower = mean_difference - margin_of_error
    ci_upper = mean_difference + margin_of_error
    return("The difference in means at the 95% confidence interval (two-tail) is between "+str(ci_lower)+" and "+str(ci_upper)+".")

print(get_95_ci(diabetes_yes_filtered_glucose['glucose'], diabetes_no_filtered_glucose['glucose']))
print('--------------------------------')
print('--------------------------------')
print('with 95% confidence, patients without\
\ndiabetes have glucose levels that are on\
\naverage between 35.84 mg/dL and 27.50 mg/dL\
\nLower than patients with diabetes.')

g = sns.pointplot(data=[diabetes_yes_filtered_glucose['glucose'],
                        diabetes_no_filtered_glucose['glucose']], join=False)
                        
g.set(xticklabels = ['diabetes_yes', 'diabetes_no'])
plt.show()
print('--------------------------------')
print('--------------------------------')