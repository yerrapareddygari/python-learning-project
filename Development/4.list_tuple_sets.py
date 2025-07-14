"""List Tuple and set in python"""

"""
List and tuples are sequential form of data and sets are unordered form of data and sets won't allow duplicates

"""


my_list = [1,2,3,4,5,"yash","reddy"]
print(my_list)

#Accessing an item in list
print(my_list[0])

#len of the list
print(len(my_list))

#slicing in python
print(my_list[3:])
print(my_list[-1])
print(my_list[2:5])

#add an item using append
my_list.append("Chandu")
print(my_list)

#add an item using insert

my_list.insert(2,"Banglore")
print(my_list)
print(len(my_list))

#----------------------------------------------------
new_list = ["Yashu","Chandrika"]
my_list.insert(0,new_list)
print(my_list)
print(my_list[0][1])

#----------------------------------------------------
"""If we want to add to the same list we can use extend method"""
my_list.extend(new_list)
print(my_list)

#----------------------------------------------------
"""Remove the item in the list"""
deleted_item = my_list.pop(5)
print(deleted_item)
print(my_list)

#we can also we remove method to remove the specific item
print(my_list)
my_list.remove(5)
print(my_list)

#----------------------------------------------------
test_list = [1, 2, 3, 4, 5]
print("Before reverse:", test_list)
test_list.reverse()
print("After reverse (in-place):", test_list)

#----------------------------------------------------

"""Sorting the list - CORRECTED"""
print("\n--- SORTING OPERATIONS ---")
numbers = [5, 2, 8, 1, 9, 3]
print("Original numbers:", numbers)

numbers.sort()
print(numbers)

"""We can also use reversed method to sort the data in reverse order"""
"""Sorting the list - CORRECTED"""
print("\n--- SORTING OPERATIONS ---")
numbers = [5, 2, 8, 1, 9, 3]
print("Original numbers:", numbers)

numbers.sort(reverse=True)
print(numbers)

#----------------------------------------------------
"""We can use sorted directly"""

numbers = [1,2,3,4,5,8,1,35,11,35]
sorted_list = sorted(set(numbers))
print(sorted_list)

reverse_sorted = sorted(set(numbers), reverse=True)
print("Method 4 - Direct reverse sort:", reverse_sorted)

#----------------------------------------------------
"""Min and Max in lists"""

numbers  = [1,2,3,4,5,6,7,8]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#----------------------------------------------------
"""To find the item in the list using index"""
names = ["Yash","Chandu","Neha","Bhanu"]
print(names.index("Yash"))

#We can also use the in to find the item in list
print("Chandu" in names)

#----------------------------------------------------
"""Looping the list """
print("\n THIS IS A LOOP")
for name in names:
    print(name)

print("\n LOOP WITH INDEX")
for index , name in enumerate(names,start= 1):
    print(index,name)

#----------------------------------------------------
"""Using join method """

new_names = ',*'.join(names)
split_names = new_names.split('-')
print(new_names)
print(split_names)




#---------------------------------------------Tuples------------------------------------------------------

"""Tuples are similar to list which are ordered and we cannot modify them know as immutable"""

files = (1,2,3,4,5,6)
print(files[0])

#----------------------------------------------SETS------------------------------------------------------

"""Sets wont allow duplicate items and order is not preserved"""
set1 = {1,2,3,4,5}
set2 = {1,2,8,5,8,0}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

#----------------------------------PRACTISE----------------------------------------------------
numbering_list = [1,2,9,8,4,3,1,2,1,3,6,8]
ordered_list = sorted(numbering_list)
sorted_order_list = set(ordered_list)

print(f"ORIGINAL LIST: {numbering_list}")
print(f"SORTED LIST :{ordered_list}")
print(f"WITHOUT DUPLICATE VALUES LIST : {sorted_order_list}")
#-------------------------------Creating an empty list ,tuple ,sets ---------------------------

my_list  = []
new_list = list()

my_tuple = ()
new_tuple = tuple()

empty_set = set()


# ------------------------------------------------SUMMARY---------------------------------------------------
"""
1.Printing the list in python
2.len() method to get the length of the list.
3.append() method to add item to end of the list.
4.insert() method to add item at particular point.
5.pop() method to remove the item from the list.
6.extend() method to add the same sort of list to first list.
7.Slicing the list to get the required items.
8.max(),min(),sum() to the items from the list.
9.remove() method to remove the item from the list.
10.sort() and sorted() methods to sort the list items
11.reverse() method to reverse the list items.
12.reversed = true or false to reverse the order.
13.intersection(), union(),difference() methods to get the values from set.
14.Looping through the list.

"""



