# # n = int(input())
# # width = "{0:b}".format(n)
# # print(width)

# m = {}
# alpha = "a"
# for i in range(0, 26):
#     m[i] = alpha
#     alpha = chr(ord(alpha) + 1)
# print(m)
# import string

# alpha = string.ascii_lowercase
# print(alpha[2:3])
# s = "cbwqqwq"
# print(s[:-1])

# Python3 code to demonstrate working of
# Get all substrings of string
# Using list comprehension + string slicing


test_str = "BANANA"
anup = {}
res = {
    test_str[i:j]: test_str.count(test_str[i:j])
    for i in range(len(test_str))
    for j in range(i + 1, len(test_str) + 1)
    if test_str[i:j][:1] != "A"
}

# print(res, len(res), sum(res.values()))

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
# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")
