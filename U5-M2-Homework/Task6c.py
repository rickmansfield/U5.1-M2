import builtins
import math
"""
WARNING THIS CODE FAILS AND EDGE CASE
"""
"""
- initialize array/list of numbers using for loop
- initialize count to zero
- iterate over list 
- Use conditionals 
    - if edge case five pass
    - else add 1 to count for each number in the list
- return total count
-Resources 
    - https://www.youtube.com/watch?v=sGYRQ68XTbE&t=319s
    - list comprenesion forward to time 57:43 in https://www.youtube.com/watch?v=VchuKL44s6E


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
def findsFive(number):
    result = 0
    while number > 0:
        digit = number%10
        if digit == 5:
            result = result +1
        number = number//10
    while number <= -1:
        digit = number%10
        if digit == -5:
            result = result +1
        number = number//10
    return result


def csAnythingButFive(start, end):
    rangeBoundList = [i for i in range(start, end+1)] ## list comprenesion forward to time 57:43 in https://www.youtube.com/watch?v=VchuKL44s6E
    count = 0
    for eachNumber in rangeBoundList:
        Found = findsFive(eachNumber)
        if Found > 0:
            count = count + 0
        else:
            count = count + 1
    return count

print(csAnythingButFive(1, 5)) # 4
print(csAnythingButFive(1, 9)) # 8
print(csAnythingButFive(4, 17)) # 12
print(csAnythingButFive(1, 90)) #72
print(csAnythingButFive(100, 150)) #45
print(csAnythingButFive(108, 168)) #46
print(csAnythingButFive(101, 179)) #62
print(csAnythingButFive(63, 182)) #99
print(csAnythingButFive(-14, -6)) #9
print(csAnythingButFive(-14, -1)) #13