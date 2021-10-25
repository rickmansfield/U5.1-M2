"""
- define alphabet list [a, ..., z]
- create empty list
- slice given groups as length
- iterate over alphabet list with a while loop using years as iterations
- append list with each additional pair
- convert list to string

1 <= years <= 10
1 <= groups <=26
"""
from typing import Mapping
# print(dir(Mapping))
def csSchoolYearsAndGroups(years, groups):
    alphaGroups = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    slicedGroups = alphaGroups[:groups]
    print(slicedGroups)
    finalList = []
    count = 0
 
    while count < years:
        count += 1
        # print(count)
        for i in slicedGroups:
            countToString = str(count)
            # print(countToString) 
            finalList.append(countToString+i)
    return(', '.join(finalList))

csSchoolYearsAndGroups(4, 7)