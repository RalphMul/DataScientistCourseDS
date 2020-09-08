import pandas as pd

family = pd.read_csv('family.csv', sep=';')

females = family[family.Gender == 'Female']

print(females)
