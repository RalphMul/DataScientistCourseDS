"""
Autor: Ralph Mul
File name: Covid_tested_using_multiindex.py
File Info: attempt to create a multi index dataframe and create line graph
write csv to MultiIndex: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame
Count MultiIndex:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.value_counts.html


Date: 30-09-2020
Version 0.9
"""

'''
Import pandas for reading csv file and execute table expressions
Import matplotlib to create graphs
'''
import pandas as pd
import matplotlib.pyplot as plt
Covidfile = pd.read_csv('COVID-19_casus_landelijk.csv', sep=';', thousands='.')

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
create multi index
'''
NH = Covidfile[Covidfile.Province == 'Noord-Holland']
#sexNH = sexNH[sexNH.Covid_count_source == 'Yes']
NH = pd.DataFrame(NH[['Province','Hospital_admission','Sex','Agegroup']])
NH = NH.rename(columns = {'Province':'Province NH','Hospital_admission':'hospitalisedNH','Agegroup':'AgeGroupNH' })

'''
delete the column province NH, values unknonw & >50 for the column AgeGroupNH
'''
NH = NH.drop(columns=['Province NH'])
NHvalidage = NH[NH.AgeGroupNH != 'Unknown']
NHvalidage = NHvalidage[NHvalidage.AgeGroupNH != "<50"]
NHvalidage.to_csv('nh.csv')
NHvalidage = pd.MultiIndex.from_frame(NHvalidage, names=['AgeGroupNH', 'Sex', 'hospitalisedNH'])
print(NHvalidage)



'''
Now we will create graphs
'''


'''
plotting the points
but first create a list from the index as defined in line 54 & 55
'''
#df = NHAgeGroup(NHAgeGroup,columns=["AgeGroupNH","Province NH"])
NHvalidage.plot(x = 'AgeGroup', y = 'Province NH', kind = "line" )


'''
naming the x axis
'''
plt.xlabel('age group')

'''
naming the y axis
'''
plt.ylabel('number of Covid-19 people')

'''
giving a title to my graph
'''

plt.title('Covid-19 per age group for province NH')

'''
function to show the plot
'''

plt.show()
