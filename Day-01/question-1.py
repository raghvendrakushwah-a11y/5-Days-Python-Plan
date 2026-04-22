#Swap without using third variable

a = 1
b = 2

print("*"*10, " Before Swap ", "*"*10)
print('a : ', a)
print('b : ', b)

a, b = b, a
print("*"*10, " After Swap ", "*"*10)
print('a : ', a)
print('b : ', b)
