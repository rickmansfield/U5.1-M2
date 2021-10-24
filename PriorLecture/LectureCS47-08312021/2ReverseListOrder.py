# output = [1, "hello", 3.6, [12, 22, [2, 3, 6 [55, 66],543]]]
# output = list(1, 2, 3, 4)

# output[3][1]
# output[::-1]
# result = []
# for i in range(len(output) - 1, -1, -1):
#   result.append(output[i])
"""
 slicing from element 0 to last element stepping in increments of negative 1
"""
s = "this is a string"
s_l = s.split()
s_l.reverse()
reversed_string = " ".join(s_l)
print(s)
print(reversed_string)