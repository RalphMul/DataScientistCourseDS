"""
Autor: Ralph Mul
File name: Zelf study Covid
Info: first attemt to use panda pivot option
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html
Date: 25-09-2020
Version 0.1
"""
import pandas as pd
import numpy as np
Covidfile = pd.read_csv('COVID-19_casus_landelijk_RM.csv', sep=';')

'''
Create pivot table for province = NH
'''

NH = Covidfile[Covidfile.Province == 'Noord-Holland']
NH = pd.DataFrame(NH[['Province','Covid_count_source','Sex']])
print(NH)
NH = pd.pivot_table(NH, index=['Covid_count_source'], aggfunc=pd.Series.nunique)

print(NH)
