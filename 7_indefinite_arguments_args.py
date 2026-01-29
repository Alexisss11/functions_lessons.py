# def tea_order(customer_name, tea_type, **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#        print("  - Add", key, ":", value)
# tea_order("Alice", "Chommile")
# tea_order("Joe", "Black", milk="Oat")
# tea_order("Bob", "green", milk="Oat", sweetner="honey")


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args): 
    sum = 0 #initiliaze sum to 0
    for num in args: #iterate through each argument
        sum += num ** 2 #Square  the number and add it to the sum
        #first time through: sum = 0 + 1^2 = 1
        # second time through: sum = 1 + 2^2 = 5
        # third time through: sum = 5 + 3^2 = 14
    return sum

print(sum_squares(1, 2 ,3))

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 #initil;iaze tpta; to 0
    for num in args: #iterate through each argument
        total += abs(num) # add the absoulute value of the number to total)
        # first time thorugh: total = 0 + abs(-1) = 1
        # sceond time through: total  = 1 + abs(-2) = 3
        #third time through: total = 3 + abs(3) = 6 
        return total
print(absolute_sum(-1, -2, 3)) # output: 6





# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg

    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("Karissa", 5, 10, 20))
print(personal_numbers("Alexis", 10, 20, 30))
print(personal_numbers("Lizbeth", 1, 2, 3))