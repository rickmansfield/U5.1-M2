"""
- Convert List to string for indexing advantages
- Create new empyt str to append as needed
- iterate string using for loop
- check each i for 7 (serach for possible built in fuction to do this)
- write conditionals to handle edge cases (existing 7 or empty list/array)
- append string as needed
- convert str back to list
- return appended list
"""

def csMakeItJazzy(chords):
    # chordsToString = ' '.join(chords)
    # print(chordsToString)
    print(chords)
    newChordsListofStr = []
    for eachChordStr in chords:
        if chords == []:
            return []
        if eachChordStr[1:2] == "7" or eachChordStr[2:3] == "7":
            newChordsListofStr.append(eachChordStr)
        elif eachChordStr[1:2] == "" or eachChordStr[2:3] == "":
            newChordsListofStr.append(eachChordStr + "7")
    # chordsToList = ', '.join(newChordsListofStr)
    return newChordsListofStr
    
print(csMakeItJazzy(["G", "F", "C"]))
print("----------------------")
print(csMakeItJazzy(["G", "F7", "C"]))
print("----------------------")
print(csMakeItJazzy(["Dm", "G", "E", "A"]))
print("----------------------")
print(csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print("----------------------")
print(csMakeItJazzy([]))
print("----------------------")

# csMakeItJazzy(["G", "F", "C"])
# csMakeItJazzy(["G", "F7", "C"])
# csMakeItJazzy(["Dm", "G", "E", "A"])
# csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])
# csMakeItJazzy([])