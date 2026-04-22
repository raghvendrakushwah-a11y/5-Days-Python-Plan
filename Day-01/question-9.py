"""Check if two strings are anagrams of each other."""

str1 = input('Enter String 1 : ')
str2 = input('Enter String 2 : ')

if len(str1) != len(str2):
    print('Strings are not Anagram of each other.')

n = len(str1)
freq1 = [0]*26

for i in range(n):
    freq1[ord(str1[i]) - ord('a')] += 1
    freq1[ord(str2[i]) - ord('a')] -= 1

if all(c == 0 for c in freq1):
    print(f'String {str1} and {str2} are anagrams.')
else:
    print(f'String {str1} and {str2} are not anagrams.')