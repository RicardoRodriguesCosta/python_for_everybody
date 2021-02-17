import re

handle = open("regex_sum_1089813.txt")
total = 0
for line in handle:
    word_number = line.split()
    #print(word_number)
    for word in word_number:
        try:
            numbers = re.findall('[0-9]+',word)
            if len(numbers) >= 1:
                for number in numbers:
                    total = total + int(number)
                    #print(int(number))
        except:
            continue

print(total)
