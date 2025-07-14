"""
Slicing in python using lists and strings.
"""

test_list = [0,1,2,3,4,5,6,7,8,9]

print(test_list) #printing the list

#-------------------------------------------------------------
print(test_list[0])  #printing the single values in the list
print(test_list[-1])  #printing the single values in the list

#-------------------------------------------------------------
print(test_list[0:5:2])        #[start:end:step]
print(test_list[::-1])
print(test_list[2:8:2])
print(test_list[-1:2:-2])

#----------------------------------------------------------------


"""String slicing"""

name = "my name is yaswanth reddy "

print(name) #printing the name

print(name[::1])
print(name[::-1])
print(name[:-1:2])

# ---------------------------------------------SUMMARY------------------------------------------------------
"""
1.Printing the list.
2.Slicing the list.
3.Using the start end and step for list and string.
4.Using the negative slicing to print the reverse values for list and string.
5.Using :: etc to print the all values.
"""










