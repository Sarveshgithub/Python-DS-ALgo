s = input()
o = input()
print(len([s[i : i + len(o)] for i in range(len(s)) if s[i : i + len(o)] == o]))

