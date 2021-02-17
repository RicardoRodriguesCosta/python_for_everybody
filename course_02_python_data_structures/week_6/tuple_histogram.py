name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:
    list_line = line.split()
    if len(list_line) > 1 and list_line[0] == "From":
        a = list_line[5].split(":")
        hours[a[0]] = hours.get(a[0], 0) + 1
    else:
        continue
final = sorted([(k,v) for k,v in hours.items() ])

for k,v in final:
    print(k,v)
