'''
An array is a data structure that stores values of same data type.
While python lists can contain values corresponding to different data types, arrays in python can only contain values of the same data type!
'''

#creating an array of multiple things
subjects = ["history", "math", "english", "pottery", "physics", "band"]

'''
an index is the number which refers to the value in the array. The first value has an index of 0,
the second has an index of 1 and so on
'''

#to get the first value in an array, you would print the value at the index of 0:
print(subjects[0])

#to modify a value at a specific index:
subjects[1] = "chemistry"
# ^^ this changed math (at the index of 1) to chemistry

#the len() method returns the length of an array. For the 'subjects' array, the length should be 3.
print(len(subjects))

#loops can be used for arrays as well
#this code should print every element in the array:
for sub in subjects:
    print(sub)

#You can use the append() method to add an element to an array
subjects.append("ceramics")

#You can use the pop() method to remove an element from the array using index
subjects.pop(3)

#You can use the remove() method to remove an element from the array using name
subjects.remove("history")

#for more array learning: https://www.w3schools.com/python/python_arrays.asp