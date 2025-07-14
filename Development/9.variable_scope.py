"""
LEGB : Local , Enclosing ,Global ,Built-in
"""

name = "Chandu is a global variable"

def test():
    global name
    name = "Yash is a local variable"
    print(f"{name}")
test()
print(f"{name}")


# ---------------------------------------------SUMMARY------------------------------------------------------

"""
1.Global Variable 🌍
    A variable that can be accessed everywhere in your program.
    Like a public announcement that everyone can hear.
    Created outside of any function.
2.Local Variable 🏠
    A variable that can only be accessed inside the function where it's created.
    Like a private conversation in a room - only people in that room can hear it.
    Created inside a function.
"""

