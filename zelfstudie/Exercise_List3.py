"""
Autor: Ralph Mul
File name: Exercise_List3
Info: This exersise is created based on the Python Data Structure Exercise for Beginners assignment as stated in https://pynative.com/python-data-structure-exercise-for-beginners/
Date: 16-08-2020
Version 0.1
"""
"""
#assignment: Given a list slice it into a 3 equal chunks and rever each list
originalList =  [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = originalList.copy()
del chunk1[3:9]
print("chunk1: " + str(chunk1))
chunk1.reverse()
print("chunk1 reverse: " + str(chunk1))

chunk2 = originalList.copy()
del chunk2[6:9]
#print(chunk2)
del chunk2[0:3]
print("chunk2: " + str(chunk2))
chunk2.reverse()
print("chunk2 reverse: " + str(chunk2))

chunk3 = originalList.copy()
del chunk3[0:6]
print("chunk3: " + str(chunk3))
chunk3.reverse()
print("chunk3 reverse: " + str(chunk3))
"""


"""
Expected output
Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
"""


#original solution:
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(sampleList)
print("length: " + str(length))
chunkSize  = int(length/3)
print("chunksize: " + str(chunkSize))
start = 0
end = chunkSize
for i in range(1, 4, 1):
  print("i: " + str(i))
  indexes = slice(start, end, 1)
  print("indexes: " + str(indexes))
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  print("start: " + str(start))
  print("end: " + str(end))
  print()
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize
