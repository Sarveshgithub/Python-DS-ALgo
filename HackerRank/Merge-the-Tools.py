from collections import OrderedDict

s = "AABCAAADA"
f = 3
# f = len(s) // k
output = ["".join(OrderedDict.fromkeys(s[i : i + f])) for i in range(0, len(s), f)]
print("\n".join(output))
