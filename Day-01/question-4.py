
"""Convert temperature from Celsius to Fahrenheit and vice versa."""

def celcius_to_fahreniet(celcius):
    return (celcius * 9 / 5 ) + 32

def fahreniet_to_celcius(fahreniet):
    return (fahreniet - 32) * (5 / 9)

print("*"*10, " Conversion Options ", "*"*10)
print(""""Press 1 + Enter" : for Celcius to Fahreniet Conversion""")
print(""""Press 2 + Enter" : for Fahreniet to Celcius Conversion""")

option = int(input())

if option == 1:
    print(celcius_to_fahreniet(int(input())))
elif option == 2:
    print(fahreniet_to_celcius(int(input())))
else:
    print('Invalid Option.')