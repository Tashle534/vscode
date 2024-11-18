file = open("file.txt","rt")

for line in file:
    print(line *2)

file.close()
