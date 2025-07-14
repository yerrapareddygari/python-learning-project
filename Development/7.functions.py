""" Functions in the python """

# Simple function without parameters
def greet():
    print("Hello from Apparacheruvu!")

# Call the function
greet()

print("-" * 30)

# Function with parameters
def greet_person(name):
    print(f"Hello {name}!")

# Call with argument
greet_person("Yash")
greet_person("Chandu")


# Function without return (returns None by default)
def say_hello():
    print("Hello!")

result = say_hello()
print(f"Result: {result}")  # None

print("-" * 30)

# Function with return
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple returns
def get_village_info():
    village = "Apparacheruvu"
    mandal = "Bathalapalli"
    district = "Anantapur"
    return village, mandal, district  # Returns a tuple

village, mandal, district = get_village_info()
print(f"Village: {village}, Mandal: {mandal}, District: {district}")


#--------------------------------------------------------------------------------------

# *args allows function to accept any number of positional arguments
def calculate_total(*numbers):
    print(f"Received numbers: {numbers}")  # numbers is a tuple
    total = 0
    for num in numbers:
        total += num
    return total

# Can pass any number of arguments
print(calculate_total(1, 2, 3))  # 6
print(calculate_total(10, 20, 30, 40))  # 100
print(calculate_total(5))  # 5
print(calculate_total())  # 0

print("-" * 30)

# Real-world example
def introduce_family(father, mother, *children):
    print(f"Father: {father}")
    print(f"Mother: {mother}")
    print("Children:")
    for child in children:
        print(f"  - {child}")

introduce_family("Ramu", "Lakshmi", "Yash", "Chandu", "Reddy")



#-------------------------------------------------------------------
# **kwargs allows function to accept any number of keyword arguments
def display_info(**info):
    print(f"Received info: {info}")  # info is a dictionary
    for key, value in info.items():
        print(f"{key}: {value}")

# Can pass any number of keyword arguments
display_info(name="Yash", age=25, city="Anantapur")
display_info(village="Apparacheruvu", mandal="Bathalapalli", district="Anantapur", state="AP")

print("-" * 30)

# Real-world example
def create_profile(name, **details):
    print(f"Creating profile for: {name}")
    print("Additional details:")
    for key, value in details.items():
        print(f"  {key.title()}: {value}")

create_profile("Yash", age=25, city="Anantapur", occupation="Developer", hobby="Coding")

#----------------------------------------------------------------------

# Example 1: Calculator with *args
def calculator(operation, *numbers):
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        return "Invalid operation"


print(calculator("add", 1, 2, 3, 4, 5))  # 15
print(calculator("multiply", 2, 3, 4))  # 24

print("-" * 30)


# Example 2: Student management with **kwargs
def add_student(name, grade, **subjects):
    print(f"Student: {name} (Grade: {grade})")
    print("Subjects and marks:")
    total_marks = 0
    for subject, marks in subjects.items():
        print(f"  {subject.title()}: {marks}")
        total_marks += marks

    average = total_marks / len(subjects) if subjects else 0
    print(f"Average: {average:.2f}")
    return average


add_student("Yash", "10th",
            math=85, science=90, english=78, social=82, hindi=75)

print("-" * 30)


# Example 3: Flexible logging function
def log_message(level, message, *tags, **metadata):
    print(f"[{level.upper()}] {message}")

    if tags:
        print(f"Tags: {', '.join(tags)}")

    if metadata:
        print("Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    print("-" * 20)


log_message("info", "User logged in", "auth", "security",
            user_id=123, ip_address="192.168.1.1", timestamp="2024-01-15")

log_message("error", "Database connection failed", "database", "critical")


#my example

def example_function(*args):
    print(f"args is: {args}")  # Shows it's a tuple
    print(f"Type of args: {type(args)}")
    return sum(args)

result = example_function(1, 2, 3, 4, 5, 6)
print(f"Result: {result}")

def another_example(**kwargs):
    print(f"{kwargs}")

another_example(name="Yash",age=25)

#example:
def testing_function(*numbers):
    return sum(numbers)

testing_function(1,2,3,4,5,6,7,8)

def testing_kwargs(**words):
    print(f"{words}")


testing_kwargs(name = "Yash",age = 26,)


#exanple to check the leap year
user_input = int(input("Enter any number"))

if user_input % 4 == 0 and (user_input % 100 != 0 or user_input % 400 == 0 ):
    print("The year was leap year !!")
else:
    print("Not a leap year!")
# ------------------------------------------------SUMMARY---------------------------------------------------

"""
1.Creation of the simple function.
2.Creation of function with parameters.
3. *args and **kwargs help create flexible functions that can accept any number of arguments instead 
   of being limited to a fixed number of parameters.
4. *args allows a function to receive multiple positional arguments and treats them as a tuple 
   inside the function.
5. **kwargs allows a function to receive multiple keyword arguments and treats them as a dictionary 
   inside the function.
"""

