my_dict = {"name": "Yash", "value_1": 1, 'number': 12345}
my_dict.update({'name':"Reddy","place":"Ap"}) #to update the values
print(my_dict.values()) #to print the values
print(my_dict['name'])
print(my_dict.get('bro'))   #will get None instead of Error if we use get
print(my_dict)
print(my_dict.keys())

#----------------------------------------------------------------------
del my_dict["value_1"]
print(my_dict)

#we can also use pop and save that popped value

deleted_value = my_dict.pop('number')
print(deleted_value)
print(my_dict)


print(len(my_dict)) # to get the length of the dictionary

#----------------------------------------------------------------------
print(my_dict.items()) #to print the values in item type

#----------------------------------------------------------------------
#looping the dict

my_dict = {'name': 'Yash', 'age': 25, 'city': 'Anantapur', 'state': 'Andhra Pradesh'}

print("=== CORRECT WAYS TO PRINT DICTIONARY WITH INDEXES ===\n")

# Method 1: Using enumerate with dict.items() - CORRECTED
print("Method 1 - Using enumerate(dict.items()):")
for index ,(key,value) in enumerate(my_dict.items()):
    print(f"Index {index} : {key} {value}")

print("\n" + "-"*50 + "\n")

print("\n" + "-"*50 + "\n")

# ------------------------------------------------SUMMARY---------------------------------------------------
"""
1.dictionaries in python
2.printing key and values of the list.
3.using index in the loop to print the index values at the start.
4.update() method to update the values in dict.
5.using get() method to print the None value without getting the error.
6.del keyword to delete the key and value from the dict.
7.using enumerate and index in the for looping to print the key and values 
  from the dict also use the items().
8.printing the - n number of times.
9.using pop() to delete the value and we can print the deleted value.
10.items() method to print the key and values from the dict.
  
"""
