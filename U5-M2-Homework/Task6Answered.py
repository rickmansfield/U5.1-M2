

def csAnythingButFive(start, end):
    counter = 0
    for num in range(start, end + 1):
        if "5" not in str(num):
            counter +=1
            
    return counter

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