# size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


import string

alpha = string.ascii_lowercase
n = int(input())
w = 4 * n - 3
rangoli = [
    "-".join(list(alpha[n - i - 1 : n][1:][::-1] + alpha[n - i - 1 : n])).center(w, "-")
    for i in range(n)
]
print("\n".join(rangoli + rangoli[:-1][::-1]))

