"""
Autor: Ralph Mul
File name: Zelf study to read csv
Info: first attemt to read csv file using panda
https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
Date: 28-08-2020
Version 0.1
"""
import pandas as pd
Familyfile = pd.read_csv('family.csv')
#column = Familyfile.column_name
for column in Familyfile:
    print (column)
