x = 7
print(x)
print(x + 3)
print(x)

x = 123.456
print(x)
x = "This is a string"
print(x + '!')

this_is_a_normal_name_123 = 7
print(this_is_a_normal_name_123)

# error variable names
# 123abc = 7
# a b  = 7

# Python is a case sensitive programming language.
# Thus, Lastname and lastname are two different variable names in Python.
Lastname = 1
lastname = 2
print(Lastname)
print(lastname)

#  use the del statement to remove a variable
foo = "a string"
del foo
# got NameError: name 'foo' is not defined
# print(foo) 

# take the value of the variable from the user input
foo = input("Enter a number: ")
print(foo)

# In-place operators allow you to write code
# like 'x = x + 3' more concisely, as 'x += 3'.
# The same thing is possible with other operators such as -, *, / and %.
x = 5
x += 5
x *= 2
x /= 5
print(x)
