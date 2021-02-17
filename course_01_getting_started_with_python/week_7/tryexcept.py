largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            num = float(num)
            if largest == None and smallest == None:
                smallest = num
                largest = num
            #smallest = num
        except:
                print("Invalid input")
                continue
        if num > largest:
            largest = num
            continue
        elif num < smallest:
            smallest = num
            continue
    #print(num)

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
