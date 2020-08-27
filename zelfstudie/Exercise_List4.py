"""
Autor: Ralph Mul
File name: Exercise_List4
Info: This exersise is created based on the Python Data Structure Exercise for Beginners assignment as stated in
https://pynative.com/python-data-structure-exercise-for-beginners/
Date: 17-08-2020
Version 0.1

assignment:
Given a list iterate it and count the occurrence of each element
and create a dictionary to show the count of each element

Expected output:
Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""

"""
originalList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = 0
indexPlace = 0
for value in originalList:
    index = originalList[indexPlace]
    print('ik ben voor de if')
    print("value: " + str(value))
    print("index: " + str(index))
    print()
    if value == index:
        count = count + 1
    print("ik ben na de if")
    print("count: " + str(count))
    print()
    count = 0
"""

#original solution
sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)

countDict = dict()

for item in sampleList:
  print("ik ben voor de if")
  print("item: " + str(item))
  print("countDict: " + str(countDict))
  if(item in countDict):
    countDict[item] += 1
    print("ik ben in de if")
    print("item: " + str(item))
    print("countDict: " + str(countDict))
  else:
    print("ik ben in de else")
    countDict[item] = 1
    print("item: " + str(item))
    print("countDict: " + str(countDict))
print("Printing count of each item  ",countDict)
