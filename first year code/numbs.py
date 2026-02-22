import math

Numbers =[4,12,23,27,32,36]
index = 0
to_search = 27
lower = [Numbers[0],Numbers[1]]
start = 0
middle_index = Numbers[2]
upper = [Numbers[3],Numbers[4],Numbers[5]]

if middle_index == to_search:
    print(middle_index)

if Numbers[middle_index] > Numbers[1]:
    for num in upper:
        if to_search == num:
            print(num)
else:
    if Numbers[1] < Numbers[middle_index]:
        for num in lower:
            if to_search == num:
                print(num)