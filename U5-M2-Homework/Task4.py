import math
import builtins
"""
convert string of words into individual strings in a list
see researched dir for min(), and len()
get min() length of each string using len() as key i.e. key=len
return smallest string

NOTE
def length(s):
    l = map(len, s.split())
    return max(l), min(l)

NOTE 
s = "some strings"
l = s.split()
max(l, key=len)
min(l, key=len)
"""
print(dir(min))
print(help(min))
print(dir(max))
print(help(max))
print(dir(len))
print(help(len))

str1 = "This test finds the shortest sting of words or strings of words"
str2 = "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"
def csShortestWord(input_str):
    stringToList = input_str.split()
    min(stringToList, key=len)
    return len(min(stringToList, key=len))


print(csShortestWord(str1))
print(csShortestWord(str2))
