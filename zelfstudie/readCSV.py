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
    # r means read and is default
    reader = csv.reader(file)
    for row in reader:
        print(row)
    For
