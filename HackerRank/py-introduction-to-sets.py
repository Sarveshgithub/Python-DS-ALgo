s = input()
heights = input().split(" ")
heights = set([int(i) for i in heights])
print(sum(heights) / len(heights))
