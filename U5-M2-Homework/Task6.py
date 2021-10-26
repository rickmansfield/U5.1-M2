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
print(dir("isinF"))
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
        # while (eachNumber > 0):
            n = eachNumber%10 # isolate final number
            # print("---%---")
            # print(eachNumber)
            if n == 5:
                pass
            else:
                eachNumber = eachNumber//10 # floor division
                # print("---floor---")
                # print(eachNumber)
                count = count +1
                print(count)
    return count

# print(csAnythingButFive(1, 5)) # 4
# print(csAnythingButFive(1, 9)) # 8
# print(csAnythingButFive(4, 17)) # 12
print(csAnythingButFive(1, 90)) #72