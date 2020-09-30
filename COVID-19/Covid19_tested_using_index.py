"""
Autor: Ralph Mul
File name: Covid_tested_using_index.py
Info: first attemt to read csv file using panda and extract data and finally create graph with the data extracted
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
rename option: https://www.datacamp.com/community/tutorials/python-rename-column?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9064573&gclid=Cj0KCQjwqrb7BRDlARIsACwGad5ZsIpHQwmFpuna2CDNW4O0LLoh8Q1O2qkJCyHREKnRPjlGvqec_dcaAso0EALw_wcB
Graph: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
use dataframe for graph: https://datatofish.com/plot-dataframe-pandas/
Read dataframe form csv file: https://www.geeksforgeeks.org/creating-a-dataframe-using-csv-files/
Date: 30-09-2020
Version 0.9
"""

'''
Import pandas for reading csv file and execute table expressions
Import matplotlib to create graphs
'''
import pandas as pd
import matplotlib.pyplot as plt
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
#NHAgeGroup = pd.DataFrame(NHAgeGroup[['AgeGroupNH', 'Province NH']])


'''
#sum column
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
Now we will create graphs
x = x axis values
y = y axis values

x = [1,2,3]
y = [2,4,1]

df = DataFrame(Data,columns=['Year','Unemployment_Rate'])
df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')
plt.show()

'''

'''
first convert column AgegroupNH to string
'''
print('finding the keys')
print(NHAgeGroup.keys())
NHAgeGroup['AgeGroupNH'] = NHAgeGroup['AgeGroupNH'].astype(str)

'''
plotting the points
'''
#df = NHAgeGroup(NHAgeGroup,columns=["AgeGroupNH","Province NH"])
NHAgeGroup.plot(x = 'AgeGroupNH', y = 'Province NH', kind = "line" )

'''
naming the x axis
'''
plt.xlabel('x - number of Covid-19 people')

'''
naming the y axis
'''
plt.ylabel('y - age group')

'''
giving a title to my graph
'''

plt.title('Covid-19 per age group for province NH')

'''
function to show the plot
'''

plt.show()
