s = "BANANA"
vowels = "AEIOU"

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        print(s[i], i)
        kevsc += len(s) - i
    else:
        stusc += len(s) - i
print(kevsc, stusc)
