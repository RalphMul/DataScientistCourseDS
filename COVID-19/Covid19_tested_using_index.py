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
Covidfile = pd.read_csv('COVID-19_casus_landelijk.csv', sep=';')
'''
Recreate Agegroup 10-19 because microsoft interpretes it as 01-okt-19
'''
Covidfile = Covidfile.replace("okt-19","10-19")

'''
Fill out blanks with Unknown
'''
Covidfile['Hospital_admission'] = Covidfile['Hospital_admission'].fillna('Unknown')


'''
Filter for NH & Select columns Province','Hospital_admission','Sex','Agegroup and rename them to NH
'''
NH = Covidfile[Covidfile.Province == 'Noord-Holland']
#sexNH = sexNH[sexNH.Covid_count_source == 'Yes']
NH = pd.DataFrame(NH[['Province','Hospital_admission','Sex','Agegroup']])
NH = NH.rename(columns = {'Province':'Province NH','Hospital_admission':'hospitalisedNH','Agegroup':'AgeGroupNH' })

'''
Recreate Agegroup 10-19 because microsoft interpretes it as 01-okt-19
'''


'''
Count number of tested persons in NH deviated to sex, hosptilised and Agegroup#
'''
NHSex = NH.set_index(["AgeGroupNH"],drop=True)
NHSex = NHSex.set_index(["Sex", "hospitalisedNH"]).count(level="Sex")
NHHospital = NH.set_index(["AgeGroupNH"],drop=True)
NHHospital = NHHospital.set_index(["Sex", "hospitalisedNH"]).count(level="hospitalisedNH")
NHAgeGroup = NH.set_index(["Sex"],drop=True)
NHAgeGroup = NHAgeGroup.set_index(["hospitalisedNH","AgeGroupNH"]).count(level="AgeGroupNH")

'''
sum column
'''
NHSexTotal = NHSex.sum()
NHHospitalTotal = NHHospital.sum()
NHAgeGroupTotal = NHAgeGroup.sum()


'''
print result
'''

print(NHSex)
print(NHSexTotal)
print(NHHospital)
print(NHHospitalTotal)
print(NHAgeGroup)
print(NHAgeGroupTotal)

'''
Create csv file

'''
NHSex.to_csv('nh.csv')
NHHospital.to_csv('nh.csv',mode='a')
NHAgeGroup.to_csv('nh.csv',mode='a')

'''
How to drop a column example:
NHSex = NH.set_index(["AgeGroupNH"],drop=True)
NHHospital = NH.set_index(["AgeGroupNH"],drop=True)
NHAgeGroup = NH.set_index(["Sex"],drop=True)
'''

#hospitalisedNH = pd.DataFrame(NH[['Province','Covid_count_source','Sex']])
#hospitalisedNH = hospitalisedNH.rename(columns = {'Covid_count_source':'hospitalisedNH', 'Province':'Province NH'})
#hospitalisedNH = hospitalisedNH.set_index(["Sex", "hospitalisedNH"]).count(level="hospitalisedNH")
#print(hospitalisedNH)
