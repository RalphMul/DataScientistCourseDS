''''
Autor: Ralph Mul
File name: Exercise_List1
Info: This exersise is created based on the Python Data Structure Exercise for Beginners assignment as stated in https://pynative.com/python-data-structure-exercise-for-beginners/
Date: 15-08-2020
Version 0.1
'''

#assignment: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
'''
Expected output:
Element at odd-index positions from list one [6, 12, 18]
Element at even-index positions from list two [4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''

def CreateListThree(variable):
    listThree.append(variable)
    return

#Pic odd index
x = 0
for variable in listOne:
    x = x + 1
    mod = x % 2
    if mod > 0:
        CreateListThree(variable)

x = 0
for variable in listTwo:
    x = x + 1
    mod = x % 2
    if mod == 0:
        CreateListThree(variable)

print (listThree)


"""
This code is the official solution

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)
"""
