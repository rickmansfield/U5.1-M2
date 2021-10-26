"""
Challenge #3:
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20
Notes:
- Bonus: Try to complete this challenge in one line!
# s = "23, 56, 45"
# nums = s.split(", ")
# print(nums)
# sum = 1
# sum = sum * int(nums[0])
# sum = sum * int(nums[1])
# sum = sum * int(nums[2])
# print(sum)

create a sum variable and set it to 1
create a number_list by splitting the nums passing in a ", " as the sperator

iterate over the number_list
set the sum to the sum multiplied by the integer of the current number

return the sum to the caller

"""


def multiply_nums(nums):
    sum = 1
    number_list = nums.split(", ")
    for current_number in number_list:
        sum = sum * int(current_number)
    return sum
    # return eval(nums.replace(", ", "*"))


print(multiply_nums("2, 3"))  # ➞ 6
print(multiply_nums("1, 2, 3, 4"))  # ➞ 24
print(multiply_nums("54, 75, 453, 0"))  # ➞ 0
print(multiply_nums("10, -2"))  # ➞ -20
