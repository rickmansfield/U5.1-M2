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
- resources https://lambdaschool.instructure.com/courses/1739/pages/objective-05-use-list-comprehensions?module_item_id=622132
- ## list comprenesion forward to time 57:43 in https://www.youtube.com/watch?v=VchuKL44s6E

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
    rangeBoundList = [i for i in range(start, end+1)] ## list comprenesion forward to time 57:43 in https://www.youtube.com/watch?v=VchuKL44s6E
    count = 0
    for eachNumber in rangeBoundList:
        # while (eachNumber > 0):
            print("---number to check---")
            print(eachNumber)
            n = eachNumber%10 # isolate final number
            print("---%---")
            print(n)
            if n == 5:
                pass
            else:
                eachNumber = eachNumber//10 # floor division
                print("---floor---")
                print(eachNumber)
                count = count +1
                print("----count is---")
                print(count)
                print("---next number---")
    return count

# print(csAnythingButFive(1, 5)) # 4
# print(csAnythingButFive(1, 9)) # 8
# print(csAnythingButFive(4, 17)) # 12
print(csAnythingButFive(1, 90)) #72