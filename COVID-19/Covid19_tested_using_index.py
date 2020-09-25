"""
Autor: Ralph Mul
File name: Zelf study Covid
Info: first attemt to read csv file using panda
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
rename option: https://www.datacamp.com/community/tutorials/python-rename-column?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9064573&gclid=Cj0KCQjwqrb7BRDlARIsACwGad5ZsIpHQwmFpuna2CDNW4O0LLoh8Q1O2qkJCyHREKnRPjlGvqec_dcaAso0EALw_wcB
Date: 25-09-2020
Version 0.1
"""
import pandas as pd
Covidfile = pd.read_csv('COVID-19_casus_landelijk_RM.csv', sep=';')

'''
Count number of tested persons in NH deviated to sex
'''

NH = Covidfile[Covidfile.Province == 'Noord-Holland']
#sexNH = sexNH[sexNH.Covid_count_source == 'Yes']
NH = pd.DataFrame(NH[['Province','Covid_count_source','Sex']])
NH = NH.rename(columns = {'Province':'Province NH','Covid_count_source':'hospitalisedNH' })
NHSex = NH.set_index(["Sex", "hospitalisedNH"]).count(level="Sex")
print(NHSex)
NHHospital = NH.set_index(["Sex", "hospitalisedNH"]).count(level="hospitalisedNH")
#nbrsexNH = nbrsexNH.rename(columns = {'Province':'Province NH'})
print(NHHospital)
#hospitalisedNH = pd.DataFrame(NH[['Province','Covid_count_source','Sex']])
#hospitalisedNH = hospitalisedNH.rename(columns = {'Covid_count_source':'hospitalisedNH', 'Province':'Province NH'})
#hospitalisedNH = hospitalisedNH.set_index(["Sex", "hospitalisedNH"]).count(level="hospitalisedNH")
#print(hospitalisedNH)
