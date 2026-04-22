"""Check if a given string is a palindrome (case-insensitive)."""

inp_string = input('Enter a String : ').lower()

if inp_string == inp_string[::-1]:
    print('String is a Pallindrome.')
else:
    print('String is not a Pallindrome.')
