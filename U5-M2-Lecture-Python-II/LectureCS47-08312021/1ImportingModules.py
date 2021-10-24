"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the 
"math" module that start with the letters "is".
"""
# YOUR CODE HERE

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

""" my way is better as it's a reusable function"""

"""Professors Answer"""
import math
output = []
math_module_functions_list = dir(math)
for fucntion_string in math_module_functions_list:
    if fucntion_string[0:2] == "is":
        output.append(fucntion_string)
output.sort()
print(output)
