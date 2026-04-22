# Write a program to check if a number is even or odd using modulo operator.

integer = int(input('Enter the Number : '))

if integer == 0:
    print('Integer is Zero.')
elif integer % 2 == 0:
    print('Integer is Even.')
else:
    print('Integer is Odd.')