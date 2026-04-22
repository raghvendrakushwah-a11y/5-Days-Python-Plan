"""Write a program to format a string using all three formatting methods (%, .format(), f-strings)."""

name = input('Enter your Name : ')

# Using %

print('Hello, %s'%(name))

# Using .format()

print('Hello, {}'.format(name))

# Using f-string

print(f'Hello, {name}')