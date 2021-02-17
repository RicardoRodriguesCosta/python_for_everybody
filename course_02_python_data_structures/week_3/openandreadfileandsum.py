# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0.0
n = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        s = s + float(line[line.find(" "):])
        n = n + 1

print("Average spam confidence: " + str(s/n))
