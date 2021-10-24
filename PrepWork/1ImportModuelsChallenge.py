"""
1) import math module
2) Seach potential built in fuctions for helper
3) sort initial matth modules functions list
4) extract desired results with loop
    A) initialize empty string and convert list to string
    B) iterate over list extracting all elements starting with "is" using newly discovered startswith()
    C) append empty array/list
    D) print final sorted list/array
"""
import math
"""[summary]
print(dir(math))  # reveals isinf
print("-----------------")
print(dir("isinf"))  # reveals startswith
print("-----------------")
print(dir("isinf".startswith))
print("-----------------")
print(help("isinf".startswith))
"""
sortedList = (sorted(dir(math)))
# print(sortedList)
def sortListByIS(list):
    finalSort = []
    for x in list:
        if x.startswith("is"):
            finalSort.append(x)
    print(finalSort)

sortListByIS(sortedList)