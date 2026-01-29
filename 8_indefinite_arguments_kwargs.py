
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(**kwargs):
    return len(kwargs)

count1 = number_attributes(name="Karissa", age=16, city="Chicago", job="Sports doctor girl")
print(f"Number of attributes in count1: {count1}")





# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(**kwargs):
    return list(kwargs.values())

list_attribute = list_attributes(name="Karissa", age=16, city="Chicago", physocally_active=True)
print(list_attribute)









# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black

def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")
    for argument_name, argument_value in kwargs.items():
        print(f"{argument_name}: {argument_value}")

print(describe_person("Alexis", eye_color="brown", hair_color="brown"))