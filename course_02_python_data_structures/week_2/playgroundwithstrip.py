#Idk why is this on the 2nd week.
fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")
