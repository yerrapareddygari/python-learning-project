#strings in python

message = "Hello world"
print(message)

#This is a single line comment
"""This is a multiple line doc string to describe more information"""
print("\n To print the data in the new line")
print("\t To add the tab to the current line")

#----------------------------------------------
invitation = """Hello Yash
You are welcome to python practise session
"""
print(invitation)
#----------------------------------------------------
#using len function to get the length of the string

name = "Yaswanth Reddy"
print(len(name))

#----------------------------------------------------

#Accessing the indexing and slicing of the string

text = "Hello Yash"
print(text[0])
print(text[0:5])
print(text[:5])
print(text[6:])


#----------------------------------------------------
"""Some useful methods"""
name = "Yash reddy"
print(name.lower())
print(name.upper())
print(name.count('h'))
print(name.find("reddy"))

print(name.replace("reddy","Chandu"))

#string concatenation
greeting = "Hello"
print(greeting+" "+name)
print(f"{greeting} {name.upper()}")
print('{} {}'.format(greeting,name))

#----------------------------------------------------
print(dir(name))
print(help(str))
print(help(str.lower))

# ------------------------------------------------SUMMARY---------------------------------------------------
"""
1.Printing the strings.
2.Single and multi line comments.
3.\n,\t New line and Tab usage.
4.len() method to find the length of the string we can get length of the list and other data types.
5.Slicing in python.
6.lower(), upper() ,count(),find() , replace().
7.String concatenation in python.
8.Useful methods using help , eg: if we declare one variable with 
  some value we can get help on that by using dir(),help(),help(variable.method)). 
"""


