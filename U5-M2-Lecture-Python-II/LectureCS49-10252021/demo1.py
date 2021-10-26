"""
Challenge #1:
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
- we need to get the last n (number of elements) and return them as a list to the caller
- possibly reverse the list and take the first n (number of elements)
- possibly use a slice of negative n to end of list

- check for the first 2 edge cases of n == 0 and n greater than the length of a

return the slice of a starting at -n and ending at the end of the list
"""


def last(a, n):  # linear time complexity
    if n == 0:
        return []
    if n > len(a):
        return "invalid"

    return a[-n:]  # O(n)


print(last([1, 2, 3, 4, 5], 1))  # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3))  # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7))  # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0))  # ➞ []
