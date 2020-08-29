"""
Autor: Ralph Mul
File name: Zelf study to read csv
Info: first attemt to read csv file
I took a pick at https://www.programiz.com/python-programming/file-operation
Date: 28-08-2020
Version 0.1
"""
import csv
with open('family.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    gender = 'Female'
    print (gender)
    for row in csv_reader:
        for e in row:
            if str(e) == gender:
                print(row)
