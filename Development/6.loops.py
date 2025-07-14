"""Loops in python for and while loops """
from operator import index

# numbers = [1,2,3,4,5,6,7,8]

#Normal loop to print the numbers

# for num in numbers:
#     print(num)

#Break the loop
# for num in numbers:
#     if num == 3:
#         print("Found the number")
#         break
#     print(num)

#Continue the loop to skip the number and move to next number
# for num in numbers:
#     if num == 3:
#         print("Found the number")
#         continue
#     print(num)

#loop inside the loop

# for num in numbers:
#     for letter in "Yash reddy":
#         print(num,letter)

#using range in the for loop

# for num in range(10):
#     print(num+1)

#-------------------------------------------------------WHILE LOOPS----------------------------------------
#while loop goes on until the value is false
# number = 0
#
# while number <10:
#     print(number)
#     number += 1


name = "Yash"
numbers = [1,2,3,4]


# Your first loop is correct - nested loops
for x in name:
    for y in numbers:
        print(x,y)

print("\n" + "="*30 + "\n")

# ✅ CORRECTED - Use zip() to pair elements
for x, y in zip(name, numbers):
    print(x, y)


# Example: Using enumerate() to get index and value
village_info = ["Apparacheruvu", "Bathalapalli", "Anantapur", "Andhra Pradesh"]

print("Using enumerate() for index:")
for index, place in enumerate(village_info):
    print(f"Index {index}: {place}")

print("\nWith custom starting index:")
for index, place in enumerate(village_info, start=1):
    print(f"{index}. {place}")


# ------------------------------------------------SUMMARY---------------------------------------------------
"""
1.Using the for loop in python with break,continue,loop inside the loop.
2,Using the while loop in python along with break , continue.
3.zip() method can be used to zip the two variables.
4.using the index,enumerate in loop to print the values using the start as well.
"""