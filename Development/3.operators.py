"""Will learn about conditional operators in python in this file"""

age = 10

if age == 18:
    print("You are 18 years old")
elif age >= 20:
    print("You are 20 years old")
else:
    print("NO match found")

"""and or not operations """

user = "Admin"
logged_in  = False

#and conditional operator should match all the conditions to true
if user == "Admin" and logged_in:
    print("Welcome Admin")
else:
    print("Login again !!")
#or operator conditional operator at least one condition should be true
if user == "Admin" or logged_in:
    print("Welcome Admin")
else:
    print("Login again !!")

#not operator reverse the condition
if not logged_in:
    print("Welcome Admin")
else:
    print("Login again !!")

#------------------------------------------------------------------------------------------------------------
# is and == example with id

a = [1,2,3,4,5]
# b = [1,2,3,4,5]
b = a


print(id(a))
print(id(b))
print(a is b)
print(a == b)
print(id(a) is id(b))
print(f"id(a) == id(b): {id(a) == id(b)}")
print(id(a) == id(b))
print(f"a is b: {a is b}")  # This is correct!

#----------------------------------------------------
"""
False
None
empty string , tuple,list,dict 
Zero of any numeric type
"""


# ------------------------------------------------SUMMARY---------------------------------------------------

"""
1.Conditional operators in python (if ,elif and else) conditions.
2.Logical operators in python(and ,or,not).
3.id() method in python.
4.False response when we assign the empty and False values to variable((),{},False). 
"""