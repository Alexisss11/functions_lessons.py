# Notes for python
# functions = a block of resuable codes
# place () after the function to invoke it
# #peramteter
# def happy_birthday(name, age):
#     print(f"happy Birthday to you {name}!")
#     print(f"You are {age} years old!")
#     print("Happy Birthday to you!")
#     print()
# # happy_birthday()
# # happy_birthday()
# # happy_birthday() 

# # call this defining function 3 times
# happy_birthday("Bro", 20)
# happy_birthday("Steve",15)
# happy_birthday("Joe", 45)
# #positon of perameter does matter as it switches the place

# def display_invoice(username, amount, due_date):
#     print(f"Hello{username}")
#     print(f"Your bill of {amount} is due {due_date}")

# display_invoice("Brocode", 42.50, "01/01")
# display_invoice("Karissa", 100000000000, "01/21")
# display_invoice("Lizbeth", 1.50, "02/21")

# return = statament used to end a function
# and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(multiply(1, 2))
# print(subtract(1, 2))
# print(divide(1, 2))

def create_name(First, Last):
    First = First.capitalize()
    Last = Last.capitalize()
    return First + " " + Last

full_name = create_name("Spongebob", "squarepants")





# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:

# ,

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.

