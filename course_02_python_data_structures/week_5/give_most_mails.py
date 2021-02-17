name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    list_line = line.split()
    if len(list_line) > 1 and list_line[0] == "From":
        emails[list_line[1]] = emails.get(list_line[1], 0) + 1
    else:
        continue

mostemails_key = None
mostemails_value = 0

for x,y in emails.items():
    if y > mostemails_value:
        mostemails_value = y
        mostemails_key = x
    else:
        continue

print(mostemails_key, mostemails_value)
