# import math
# sort initial list and convert to string
# extract desired results with loop
# initialize empty string and convert list to string
# create new (now sorted as desired) string of desired result in loop

import math

# sortedList = ' '.join(sorted(dir(math)))
# print(sortedList)

sortedList = sorted(dir(math))

def sortListByIS(list):
    finalSort = ""
    for x in list:
        if x == "i":
            finalSort = finalSort + x
    print(finalSort)

sortListByIS(sortedList)