fh = open("romeo.txt")
lista = []
for line in fh:
    #print(line)
    line2 = line.rstrip().split()
    #print(line2)
    for word in line2:
        #print(word)
        try:
            lista.index(word)
            continue
        except:
            lista.append(word)
            continue

lista.sort()

print(lista)
