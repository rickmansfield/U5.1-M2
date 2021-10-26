"""
Challenge #2:
Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.
Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
Notes:
- The input list will only contain integers.

 create a results list

 iterate over numbers using a range based for loop
  add the i to the numbers at the index of i and store it as the new_number variable
  append the new_number to the results list

return the results list to the caller

"""
# i = 4
# a = [1, 3, 5, 7, 9]
# a[i] += i
# print(a)

def add_indexes(numbers): # O(n) linear time complexity, O(1) constant space complexity
  for i in range(len(numbers)):
    numbers[i] += i
  return numbers


print(add_indexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]