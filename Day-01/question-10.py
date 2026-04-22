"""Create a CLI calculator that performs basic arithmetic operations based on user input with input validation."""

str_inp = input('Enter Input : ')

operand1 = "0"
operand2 = "0"
l = 0
n = len(str_inp)

while l < n and str_inp[l] == " ":
    l += 1

while l < n and str_inp[l] not in "+-/*":
    operand1+=str_inp[l]
    l+=1

while l < n and str_inp[l] == " ":
    l += 1

operator = str_inp[l]
l+=1

while l < n and str_inp[l] == " ":
    l += 1

while l < n:
    operand2+=str_inp[l]
    l+=1

try:
    operand1 = int(operand1)
    operand2 = int(operand2)
except TypeError:
    print('Invalid Input ')

if operator == "+":
    print(f"Calculation : {operand1 + operand2}")
elif operator == "-":
    print(f"Calculation : {operand1 - operand2}")
elif operator == "*":
    print(f"Calculation : {operand1 * operand2}")
elif operator == "/":
    print(f"Calculation : {operand1 / operand2}")
    