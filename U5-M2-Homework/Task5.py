"""
    - initialize sum as 0
    - iterate over the list/arry of numbers with a for loop
    - if number is positive add it to the current sum
    - return final sum of completed iteration
    """


def csSumOfPositive(input_arr):
    sum = 0
    for eachNumber in input_arr:
        if eachNumber > 0:
            sum += eachNumber
    return sum

print(csSumOfPositive([1, 2, 3, -4, 5]))
print(csSumOfPositive([-3, -2, -1, 0, 1]))
print(csSumOfPositive([-3, -2]))
