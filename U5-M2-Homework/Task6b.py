import builtins
import math

"""
- initialize array/list of numbers using for loop
- initialize count to zero
- iterate over list 
- Use conditionals 
    - if edge case five pass
    - else add 1 to count for each number in the list
- return total count


print("-------dir of math----------")
print(dir(math))  # reveals isinf

print("-------isinf----------")
print(dir("isinf"))
print(help("isinf"))  # reveals startswith not helpful

print("-------Builtins----------")
print(dir(builtins)) # reveals min

print("--------Range---------")
print(help(range))

print("-------isdigit----------")
print(dir("isdigit"))
print("-------isdigit HELP----------")
print(help("isdigit"))

print("--------sum---------")
print(help(sum))
"""


def csAnythingButFive(start, end):
    rangeBoundList = [i for i in range(start, end+1)]
    count = 0
    for eachNumber in rangeBoundList:
        def findsFive(number):
            result = 0
            while number > 0:
                digit = number%10
                if digit == 5:
                    result = result +1
                number = number//10
            return result
        Found = findsFive(eachNumber)
        if Found >0:
            count = count + 0
        else:
            count = count + 1
    return count

print(csAnythingButFive(1, 5)) # 4
print(csAnythingButFive(1, 9)) # 8
print(csAnythingButFive(4, 17)) # 12
print(csAnythingButFive(1, 90)) #72
print(csAnythingButFive(100, 150)) #72