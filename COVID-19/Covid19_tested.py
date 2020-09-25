"""
Autor: Ralph Mul
File name: Zelf study Covid
Info: first attemt to read csv file using panda
https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
Date: 25-09-2020
Version 0.1
"""
import pandas as pd
Covidfile = pd.read_csv('COVID-19_casus_landelijk_RM.csv', sep=';')

'''
Count number of Females with Covid in NH
'''

sexNH = Covidfile[Covidfile.Province == 'Noord-Holland']
#sexNH = sexNH[sexNH.Covid_count_source == 'Yes']
sexNH = pd.DataFrame(sexNH)
nbrsexNH = sexNH.set_index(["Sex", "Covid_count_source"]).count(level="Sex")
print(nbrsexNH)

'''
Count number of Females with Covid in NH
'''

females = Covidfile[Covidfile.Sex == 'Female']
femalesNH = females[females.Province == 'Noord-Holland']
femalesNH = females[females.Covid_count_source == 'Yes']
NbrFemalesNH = pd.DataFrame(femalesNH)
NbrFemalesNH = NbrFemalesNH.count(axis='rows')
print(NbrFemalesNH)

'''
Count number of Males with Covid in NH
'''
males = Covidfile[Covidfile.Sex == 'Male']
malesNH = males[males.Province == 'Noord-Holland']
malesNH = males[males.Covid_count_source == 'Yes']
NbrMalesNH = pd.DataFrame(malesNH)
NbrMalesNH = NbrMalesNH.count(axis='rows')
print(NbrMalesNH)

'''
Count number of Unknonw with Covid in NH
'''
unknown = Covidfile[Covidfile.Sex == 'Unknown']
unknownNH = unknown[unknown.Province == 'Noord-Holland']
unknownNH = unknown[unknown.Covid_count_source == 'Yes']
NbrUnknownNH = pd.DataFrame(unknownNH)
NbrUnknownNH = NbrUnknownNH.count(axis='rows')
print(NbrUnknownNH)
