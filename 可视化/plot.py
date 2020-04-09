import csv
import pandas as pd
import matplotlib.pylab as plt 
import numpy as np
import statsmodels.api as sm 
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
df = pd.read_csv('D://Python//test//predict.csv', header=0, names=["日期","房价"])
sns.distplot(df['房价'])