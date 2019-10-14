# Find the Rotation Count in Rotated Sorted array
# Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

# Examples:

# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after
# rotating the initial array twice.

# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0

# solution:
# find pivot(max > pivot< min)
# find the l and r
def findPivot(a):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] > a[m + 1]:
            l, r = 0, -1
            return m + 1
        elif a[m] < a[m + 1] and a[m] > a[m - 1]:
            l = m + 1
        else:
            r = m - 1


a = [15, 18, 2, 3, 6, 12]
print(findPivot(a))
