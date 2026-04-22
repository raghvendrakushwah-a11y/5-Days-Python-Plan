"""Count the frequency of each character in a string using a dictionary."""

# Using Hashmap
inp_string = input('Enter a String : ')

hash_map = {}

for i in inp_string:
    hash_map[i] = hash_map.get(i,0) + 1

for key, value in hash_map.items():
    print(f'Frequency of {key} : ', value)

# using frequency array

freq = [0]*26
for i in inp_string:
    freq[ord(i) - ord("a")] += 1

for key, value in enumerate(freq):
    if value != 0:
        print(f'Frequency of {chr(key + 97)} : ', value) 
