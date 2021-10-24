# output = [1, "hello", 3.6, [12, 22, [2, 3, 6 [55, 66],543]]]
# output = list(1, 2, 3, 4)

# output[3][1]  # dills down to specific item in the list by index
# output[::-1]  # Slices the list from last to first
# result = [] # Creates a new list
# for i in range(len(output) - 1, -1, -1):  # iterating in a range
#   result.append(output[i]) #  appends the list
"""
 slicing from element 0 to last element stepping in increments of negative 1
"""
s = "this is a string"
print(s)
s_l = s.split()  # converts the string to a list []
s_l.reverse()  # reverses the list order
reversed_string = " ".join(s_l)  # converts it back to a string
print(reversed_string)