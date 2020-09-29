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
Covidfile = pd.read_csv('COVID-19_casus_landelijk.csv', sep=';')

'''
Recreate Agegroup 10-19 because microsoft interpretes it as 01-okt-19
'''
Covidfile = Covidfile.replace("okt-19","10-19")

'''
Create pivot table for province = NH
'''

NH = Covidfile[Covidfile.Province == 'Noord-Holland']
NH = pd.DataFrame(NH[['Province','Hospital_admission','Sex']])
NH = NH.pivot_table(index='Province', columns='Hospital_admission', values='Sex')

#NH = pd.pivot_table(NH, index=['Hospital_admission'], aggfunc=pd.Series.nunique)

print(NH)
