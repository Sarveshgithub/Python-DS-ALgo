# Maximum sum of i*arr[i] among all rotations of a given array
# Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.

# Examples :

# Input : arr[] = {8, 3, 1, 2}
# Output : 29
# Explanation : Let us see all rotations
# {8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
# {3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
# {1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
# {2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*1 = 17

# Input : arr[] = {3, 2, 1}
# Output : 7

# step first sort the array using .sort()
a = [8, 3, 1, 2]
max_element_index = a.index(max(a))
l, r = max_element_index, max_element_index + 1
i = len(a) - 1
count = 0
while l != r:
    count += a[l] * i
    i -= 1
    l = (l - 1) % len(a)
print(count)

