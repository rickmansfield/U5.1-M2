import math
# print("---------math--------")
# print(help(dir(math)))

"""
find helper function
def function to iterate over lists
use fucntion to discover index position of bob
return idex
"""
# print("---------Contains--------")
# print(dir("contains"))

# print("-------Index----------")
# print(dir("index"))

# print("--------index.find---------")
# print(dir("index".find))

# print("--------index.find---------")
# print(help("index".find))

def csWhereIsBob(names):
    str1 = ' '.join(names)
    # print(str1)
    strIndex_position = str1.find("Bob")
    if strIndex_position >= 0:
        NamesIndex_position = names.index("Bob")
        return(NamesIndex_position)
    else: return(-1)
""" 
note YOU MUST USE PRINT instead of RETURN to see the answers first. Then replace "print" with "returnr" when submitting to codesignal. 
"""    
csWhereIsBob(["Jimmy", "Layla", "Bob"]) 
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"])
csWhereIsBob(["Jimmy", "Layla", "James"])
csWhereIsBob(["Bob", "Nathan", "Hayden"])
csWhereIsBob(["Jimmy", "Layla", "Mandy"])