''''
Autor: Ralph Mul
File name: Exercise_List2
Info: This exersise is created based on the Python Data Structure Exercise for Beginners assignment as stated in https://pynative.com/python-data-structure-exercise-for-beginners/
Date: 15-08-2020
Version 0.1
'''
#assignment: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
originalList = [34, 54, 67, 89, 11, 43, 94]

'''
Expected output
Original list  [34, 54, 67, 89, 11, 43, 94]
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
'''

print(originalList)
index4 = originalList [4]
#print(index4)

originalList.remove(originalList[4])
print(originalList)
originalList.insert(2,index4)
print(originalList)
originalList.append(index4)
print(originalList)


""""
Oriinal solution:
sampleList = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print("List after Adding element at last ", sampleList)

"""
