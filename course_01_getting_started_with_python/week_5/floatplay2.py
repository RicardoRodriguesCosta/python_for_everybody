h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
if h > 40:
    rr = ((h - 40) * (1.5 * r)) + (40 * r)
else:
    rr = h * r

print(rr)
