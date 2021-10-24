
List1 = [1, 2, 3, 4, 5]

def lastNItemsinAList(anyList, anyNumber):
    L = len(anyList)
    start = 0 - anyNumber
    if anyNumber > len(anyList):
        return "invalid"
    if anyNumber == 0:
        return []
    return anyList[start: L]

print(lastNItemsinAList(List1, 3))