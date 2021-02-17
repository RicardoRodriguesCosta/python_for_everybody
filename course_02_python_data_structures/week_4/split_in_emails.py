fh = open("mbox-short.txt")
count = 0
lista = []
for line in fh:
    #print(line)
    if line.find("From:") == 0:
        continue
    elif line.find("From") == 0 or line.find("from") == 0:
        resp = line.rstrip().split()
        lista.append(resp[1])
        count = count + 1
        continue
    else:
        continue
for email in lista:
    print(email)
print("There were", count, "lines in the file with From as the first word")
